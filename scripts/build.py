"""Copy the static site; previews are noindex until an explicit launch flag is set."""
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "dist"
production = os.environ.get("SITE_PRODUCTION", "false").lower() == "true"
if DEST.exists():
    shutil.rmtree(DEST)
shutil.copytree(ROOT / "site", DEST)
if not production:
    homepage = DEST / "index.html"
    homepage.write_text(homepage.read_text().replace('content="index, follow"', 'content="noindex, follow"'))
    with (DEST / "_headers").open("a") as headers:
        headers.write("  X-Robots-Tag: noindex, follow\n")
    # Allow crawling so search engines can discover the noindex directive.
    (DEST / "robots.txt").write_text("User-agent: *\nAllow: /\n")
    (DEST / "sitemap.xml").unlink()
print(f"Built {'production (indexable)' if production else 'preview (noindex)'} site in {DEST}")
