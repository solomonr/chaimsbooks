"""Dependency-free checks for local assets, semantic HTML, SEO and launch mode."""
import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def matching(self, tag):
        return [attrs for name, attrs in self.tags if name == tag]

parser = argparse.ArgumentParser()
parser.add_argument("directory", nargs="?", default="site")
parser.add_argument("--preview", action="store_true")
args = parser.parse_args()
root = Path(args.directory).resolve()
errors = []

def check(condition, message):
    if not condition:
        errors.append(message)

for file in root.rglob("*.html"):
    source = file.read_text()
    page = Page(source)
    ids = [attrs["id"] for _, attrs in page.tags if "id" in attrs]
    check(len(ids) == len(set(ids)), f"{file.name}: duplicate IDs")
    check(len(page.matching("h1")) == 1, f"{file.name}: needs one H1")
    check(len(page.matching("main")) == 1, f"{file.name}: needs one main landmark")
    check(page.matching("html")[0].get("lang") == "en-GB", f"{file.name}: language")
    for tag, attrs in page.tags:
        if tag == "img":
            check("alt" in attrs, f"{file.name}: missing image alt")
            check("width" in attrs and "height" in attrs, f"{file.name}: image dimensions")
        if tag == "script":
            check(attrs.get("type") == "application/ld+json", f"{file.name}: unexpected executable script")
        for attribute in ("href", "src"):
            value = attrs.get(attribute)
            if not value:
                continue
            url = urlsplit(value)
            if url.scheme or url.netloc:
                check(url.scheme in ("https", "mailto", "tel"), f"{file.name}: insecure URL {value}")
                continue
            target = (root / unquote(url.path.lstrip("/"))) if url.path.startswith("/") else (file.parent / unquote(url.path))
            if not url.path:
                target = file
            elif target.is_dir():
                target /= "index.html"
            check(target.is_file(), f"{file.name}: missing asset {value}")
            if url.fragment and target.is_file() and target.suffix == ".html":
                target_ids = [a.get("id") for _, a in Page(target.read_text()).tags]
                check(url.fragment in target_ids, f"{file.name}: missing anchor {value}")
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', source, re.S):
        data = json.loads(block)
        check(data.get("@context") == "https://schema.org", "schema context")
    check(not re.search(r"lorem ipsum|TODO|PLACEHOLDER", source, re.I), f"{file.name}: unfinished content")

source = (root / "index.html").read_text()
home = Page(source)
meta = {a.get("name", a.get("property")): a.get("content") for a in home.matching("meta")}
expected = "noindex, follow" if args.preview else "index, follow"
check(meta.get("robots") == expected, f"Homepage robots should be {expected}")
check(110 <= len(meta.get("description", "")) <= 165, "Meta description length")
check(meta.get("og:url") == "https://chaimsbooks.com/", "Open Graph URL")
check(meta.get("og:image") == "https://chaimsbooks.com/assets/bar-mitzvah-list-logo.png", "Social image URL")
check(any(a.get("rel") == "canonical" and a.get("href") == "https://chaimsbooks.com/" for a in home.matching("link")), "Canonical URL")
check("<title>The Bar Mitzvah List | Personalised Bar Mitzvah Gift Lists</title>" in source, "Reference page title")
check("Chaims Books" in meta.get("description", ""), "Business name in search description")
check("Disallow: /" not in (root / "robots.txt").read_text(), "Crawler must be able to discover noindex or index content")
if args.preview:
    check(not (root / "sitemap.xml").exists(), "Preview sitemap must be omitted")
    check("X-Robots-Tag: noindex" in (root / "_headers").read_text(), "Preview response noindex header")
else:
    tree = ET.parse(root / "sitemap.xml")
    locations = [n.text for n in tree.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    check(locations == ["https://chaimsbooks.com/"], "Sitemap URL")
    check("noindex" not in (root / "_headers").read_text(), "Production response must be indexable")
    check("Sitemap: https://chaimsbooks.com/sitemap.xml" in (root / "robots.txt").read_text(), "Robots sitemap reference")

for css in root.rglob("*.css"):
    for reference in re.findall(r'url\([\"\']?([^\"\')]+)', css.read_text()):
        check((css.parent / reference).is_file(), f"Missing CSS asset {reference}")

total = sum(f.stat().st_size for f in root.rglob("*") if f.is_file())
check(total < 500_000, f"Site exceeds 500 KB budget: {total} bytes")
if errors:
    print("\n".join(f"FAIL: {error}" for error in errors))
    sys.exit(1)
print(f"PASS: HTML, local links, images, CSS assets, structured data, SEO and {'preview' if args.preview else 'production'} mode; {total:,} total bytes")
