# Chaims Books

A lightweight, responsive homepage matching [The Bar Mitzvah List](https://thebarmitzvahlist.com/), with **Chaims Books** included in its search and social descriptions. The owner requested this exact visual direction after reviewing the initial distinct design. HTML and CSS only; there is no application JavaScript, database, checkout, analytics or form processing. The gift-list service remains on its existing website.

## Project status

Published and tested on **Netlify Free**, with source in [GitHub](https://github.com/solomonr/chaimsbooks). The public preview is **https://chaimsbooks.netlify.app/** and deliberately remains noindex pending launch approval. GoDaddy remains the registrar and DNS provider; its live forwarding and DNS have not been changed. Search Console verified the `chaimsbooks.com` domain property using an existing DNS record. The custom-domain launch requires the owner's explicit approval immediately before forwarding or DNS changes. See `docs/verification.md` for the recorded results and remaining steps.

The user selected Netlify because [GitHub Pages restricts online business/commercial transaction hosting](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits). GitHub Pages is not the deployment target. Netlify's [Free plan](https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/) currently includes 300 monthly credits, with a hard limit and no automatic recharge. Traffic and production deploys consume credits; exhaustion can pause the site. Check the actual account plan before publishing and do not enable paid services without approval.

## Files

| Path | Purpose |
| --- | --- |
| `site/index.html` | Homepage, copy, links and SEO metadata |
| `site/assets/style.css` | Responsive layout and colours |
| `site/assets/bar-mitzvah-list-logo.png` | Existing association logo, preserved without modification |
| `site/assets/calibri.woff` | Original homepage typeface |
| `site/assets/*icons.woff2` | Subsets of the original navigation icon fonts |
| `site/assets/ASSET-NOTICES.txt` | Source asset and font notices |
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

Netlify shows auto publishing enabled for `main`, but an automatic deployment was not observed for the matching-homepage push. That revision was successfully published through **Deploys → Trigger deploy → Deploy project**, which fetched the latest GitHub commit. Check the deployment status after future pushes and use that command if needed. Production deployments use Netlify credits. Group small changes, check them locally, and use previews before publishing. For documentation-only commits, Netlify supports `[skip netlify]` in the commit message to avoid an unnecessary deployment ([documentation](https://docs.netlify.com/deploy/manage-deploys/manage-deploys-overview/)). No GitHub-to-Netlify secrets are stored in this repository.

## Editing and maintenance

Edit content in `site/index.html`. Keep the business name **Chaims Books** consistent. The legacy association logo contains its original spelling and remains unaltered. Avoid inventing an address, opening hours, company history, customer reviews or stock availability. No unconfirmed business details are included in structured data.

Run the checks after edits and inspect desktop, tablet and mobile layouts. Confirm focus outlines and the skip link work, every icon link has an accessible label, links work, and the logo and icon fonts load. The GitHub check workflow validates both production and preview builds.

For a local production build:

```sh
SITE_PRODUCTION=true python3 scripts/build.py
python3 scripts/check.py dist
```

The original association logo is also the social-sharing image. The original favicon and Calibri font are preserved. Navigation fonts contain only the five required glyphs. Assets are self-hosted; the text font uses `font-display: swap`.

## SEO

The source retains the reference homepage title and a description ending “In association with Chaims Books.” It includes one H1, main/navigation landmarks, canonical URL `https://chaimsbooks.com/`, Open Graph and Twitter metadata, favicon and touch icon, `Organization`, `WebSite` and `WebPage` JSON-LD, robots.txt and sitemap.xml. Organization schema is used instead of inventing the address required for a useful local store listing. No review or product schema is fabricated. The associated service is linked but is not marked `sameAs`, because it has a distinct role and name.

There are no runtime content dependencies. A working site, sitemap submission or indexing request does not guarantee indexing or rankings. Follow the Search Console procedure only after the live domain serves the indexable production version over HTTPS.

## Branding and asset provenance

Reference inspected on 21 October 2026: [The Bar Mitzvah List](https://thebarmitzvahlist.com/). The current design reproduces its logo, Calibri typography, centred copy, gold pill buttons, responsive spacing and five fixed footer icons. The visible copy remains the same; Chaims Books is included in the search/social descriptions and organization data. Shopping, account and gift-list links lead to the existing service, including its basket.

The association logo, favicon and font files are sourced from the owner's existing website under the matching-homepage instruction. The Calibri font is unchanged. Navigation icon fonts are subset to the required symbols. Source URLs and embedded font notices are in `site/assets/ASSET-NOTICES.txt`; Font Awesome's OFL is included separately. Brand artwork and proprietary fonts retain their existing rights; this repository grants no new licence to those assets.

Keyboard focus, accessible icon labels, a skip link and zoom support are retained. Colours deliberately match the requested reference, including its low-contrast gold/white buttons and gold navigation icons; this is not a full WCAG conformance claim. No original executable scripts, analytics IDs, product catalogue or customer data are copied.
