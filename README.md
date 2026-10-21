# Chaims Books

A lightweight, responsive website introducing **Chaims Books** and its association with [The Bar Mitzvah List](https://thebarmitzvahlist.com/). HTML and CSS only; there is no application JavaScript, database, checkout, analytics or form processing. The gift-list service remains on its existing website.

## Project status

Published and tested on **Netlify Free**, with source in [GitHub](https://github.com/solomonr/chaimsbooks). The public preview is **https://chaimsbooks.netlify.app/** and deliberately remains noindex pending launch approval. GoDaddy remains the registrar and DNS provider; its live forwarding and DNS have not been changed. Search Console verified the `chaimsbooks.com` domain property using an existing DNS record. The custom-domain launch requires the owner's explicit approval immediately before forwarding or DNS changes. See `docs/verification.md` for the recorded results and remaining steps.

The user selected Netlify because [GitHub Pages restricts online business/commercial transaction hosting](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits). GitHub Pages is not the deployment target. Netlify's [Free plan](https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/) currently includes 300 monthly credits, with a hard limit and no automatic recharge. Traffic and production deploys consume credits; exhaustion can pause the site. Check the actual account plan before publishing and do not enable paid services without approval.

## Files

| Path | Purpose |
| --- | --- |
| `site/index.html` | Homepage, copy, links and SEO metadata |
| `site/assets/style.css` | Responsive layout and colours |
| `site/assets/books.svg` | Original decorative book illustration |
| `site/assets/bar-mitzvah-list-logo.png` | Existing association logo, preserved without modification |
| `site/assets/social-card.svg` and `.png` | Editable social-sharing artwork and raster export |
| `site/404.html` | Real 404 error page |
| `site/robots.txt`, `site/sitemap.xml` | Production crawler configuration |
| `site/_headers` | Netlify security headers |
| `scripts/build.py` | Copies the static files; applies preview indexing protection |
| `scripts/check.py` | Checks local links, HTML structure, SEO and preview/production modes |
| `netlify.toml` | Build and publish settings |
| `docs/launch.md` | Domain launch, email preservation, rollback and Search Console procedure |

## Preview locally

Requires Python 3. No dependencies need installing.

```sh
python3 scripts/check.py site
python3 scripts/build.py
python3 scripts/check.py dist --preview
python3 -m http.server 4173 --bind 127.0.0.1 --directory dist
```

Open `http://127.0.0.1:4173/`. Stop the server with Ctrl+C. Python's development server does not apply Netlify headers or return the custom 404 page; verify those on the deployed host.

## Netlify deployment

The repository is connected to [Netlify project chaimsbooks](https://app.netlify.com/projects/chaimsbooks/overview). It uses branch `main`, build command `python3 scripts/build.py`, and publish directory `dist`, as configured in `netlify.toml`. Production visibility is Public; Deploy Preview visibility is Private. Do not add a database, functions, paid analytics, forms or AI features.

**Initially leave `SITE_PRODUCTION` unset.** This produces a preview with `noindex, follow` in the HTML and an `X-Robots-Tag` header, while allowing crawlers to read those directives. It omits the sitemap. Canonical URLs still identify the intended final domain. Preview is public, not password protected.

After the temporary Netlify URL is tested and explicit domain-change approval is obtained, follow `docs/launch.md`. Set `SITE_PRODUCTION=true` only for the production deployment context, then rebuild. Branch and pull-request previews retain `SITE_PRODUCTION=false`. The production homepage is indexable and serves the sitemap. Keep the 404 page noindex.

Source pushes on `main` trigger production deployments and use Netlify credits. Group small changes, check them locally, and use previews before publishing. For documentation-only commits, Netlify supports `[skip netlify]` in the commit message to avoid an unnecessary deployment ([documentation](https://docs.netlify.com/deploy/manage-deploys/manage-deploys-overview/)). No GitHub-to-Netlify secrets are stored in this repository.

## Editing and maintenance

Edit content in `site/index.html`. Keep the business name **Chaims Books** consistent. The legacy association logo contains its original spelling and remains unaltered. Avoid inventing an address, opening hours, company history, customer reviews or stock availability. No unconfirmed business details are included in structured data.

Run the checks after edits and inspect desktop, tablet and mobile layouts. Confirm the FAQ opens with keyboard controls, focus outlines are visible, links work, and images load. The GitHub check workflow validates both production and preview builds.

For a local production build:

```sh
SITE_PRODUCTION=true python3 scripts/build.py
python3 scripts/check.py dist
```

Regenerate PNG icons and the social image from the corresponding SVG files with an SVG-capable image renderer when those designs change. Preserve the 1200 × 630 social image dimensions. Font files are self-hosted and use `font-display: swap`.

## SEO

The source includes a unique title and description, one H1, semantic sections, canonical URL `https://chaimsbooks.com/`, Open Graph and Twitter metadata, favicon and touch icon, `Organization`, `WebSite` and `WebPage` JSON-LD, robots.txt and sitemap.xml. Organization schema is used instead of inventing the address required for a useful local store listing. No review or product schema is fabricated. The associated service is linked but is not marked `sameAs`, because it has a distinct role and name.

There are no runtime content dependencies. A working site, sitemap submission or indexing request does not guarantee indexing or rankings. Follow the Search Console procedure only after the live domain serves the indexable production version over HTTPS.

## Branding and asset provenance

Reference inspected on 21 October 2026: [The Bar Mitzvah List](https://thebarmitzvahlist.com/). Reused its navy/blue identity, gold buttons, white space and Open Sans typography. The original full association logo came from `https://thebarmitzvahlist.com/img/site/site__site-ll-2__q-90.png?m=1791926878` and is used under the business owner's project instruction. Brand artwork remains the property of its owner; it is not granted an open-source licence by this repository.

The book illustration, navigation symbol and social card are new decorative vector artwork, not photographs or depictions of specific stock. Open Sans is distributed under the included `site/assets/OFL-Open-Sans.txt` licence. No original site's executable scripts, analytics IDs, product catalogue or customer data were copied.
