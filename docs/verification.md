# Verification record — 21 October 2026

This record distinguishes completed tests from launch tasks. It is not a claim that the custom domain is live.

## Initial design checks (superseded visually by the revision below)

- Inspected the reference homepage and its actual CSS and logo. Verified the four linked external destinations (homepage, gift-list directory, account login and contact page) each returned HTTP 200 over HTTPS.
- Verified the existing `https://chaimsbooks.com/` response: HTTP 301 to `https://www.thebarmitzvahlist.com`. No forwarding or DNS changes were made.
- Confirmed GitHub access as the repository owner. Source repository: https://github.com/solomonr/chaimsbooks
- Static production and preview checks passed: local links/anchors, image dimensions/alt attributes, font/CSS references, unique IDs, single H1/main, metadata, JSON-LD, canonical, robots and sitemap behavior. The site assets total approximately 218 KB uncompressed, including the social image; no performance score or field loading-speed claim is made.
- Browser visual inspection at desktop 1440 × 1000, tablet 768 × 1024, and phone 390 × 844. Additional overflow checks at 320, 768 and 1024 CSS pixels; all reported document width equal to viewport width.
- Both page images loaded. All three native FAQ disclosures opened and closed using Enter.
- Fixed skip-link visibility when navigating from a scrolled page and added a focus target to main. Re-tested: skip link is fixed at 12px from the viewport top when focused; activation focuses `main` and updates the fragment to `#main`.
- Browser error/warning log was empty during the local functional checks.
- Calculated text contrast: blue on white 4.87:1; blue on cream 4.56:1; muted text on cream 5.37:1; navy on gold 7.05:1; category numbers on white 5.02:1. These checks are not a complete WCAG conformance audit.
- Initial GitHub automated build/check workflow completed successfully: https://github.com/solomonr/chaimsbooks/actions/runs/39629195297

Screenshots are retained locally in ignored `qa/`, not published as website assets. Public source contains no credentials. Neither the production site nor preview requires any runtime JavaScript.

## Initial Netlify publication

- The owner approved Netlify's GitHub connection with repository scope limited to `solomonr/chaimsbooks`. The actual account billing screen confirmed the Free plan; no paid services were enabled.
- Published commit `fe93ac8ece78a6d0c1a21097b1d82d348a33491d`. Netlify deploy `6ad8dfbe5a779ff16e6a307a` completed successfully in 34 seconds on 21 October 2026. Project ID: `540c965a-e830-42c2-8e81-1d208029a465`.
- Renamed the project to `chaimsbooks`. Public URL: https://chaimsbooks.netlify.app/. The initial private production setting returned HTTP 401; it was changed to Public and unauthenticated access was then verified. Deploy Previews remain Private.
- Verified HTTPS with normal certificate validation, HTTP 200 homepage/CSS/fonts/images/robots, working security headers and `X-Robots-Tag: noindex, follow`. The homepage also contains the noindex meta tag. A nonexistent path returned the branded page with HTTP 404. The preview sitemap is intentionally absent (404).
- Visually checked the deployed desktop 1440px and mobile 390px layouts; no horizontal overflow, both images loaded, fonts loaded and browser error/warning log was empty. Screenshots and HTTP results are in ignored `qa/`.
- GitHub checks passed for the deployed commit: https://github.com/solomonr/chaimsbooks/actions/runs/39629453365
- Assigned `chaimsbooks.com` as Netlify's primary domain, with `www.chaimsbooks.com` redirecting to it. These assignments do not alter GoDaddy DNS. Both are pending DNS verification, and the custom-domain certificate is not yet provisioned.
- Read Netlify's exact DNS instructions: apex A `75.2.60.5`; www CNAME `chaimsbooks.netlify.app`. No automated DNS connection or nameserver change was used.
- Saved all 18 GoDaddy zone records, authoritative DNS query results, and existing permanent (301) forwarding to `https://www.thebarmitzvahlist.com` under ignored `private/dns-backup-2026-10-21/`.
- Added the `chaimsbooks.com` domain property in the signed-in Search Console account. Google displayed **Ownership auto verified**, method **Domain name provider**, using existing DNS. The property overview is accessible and currently says data is processing. No DNS verification record was added or changed.

## Outstanding at this checkpoint

- Explicit owner approval for the exact GoDaddy forwarding/A/CNAME changes is still required. No registrar changes have been made.
- After approval: publish the indexable production build, switch only web records, provision and verify HTTPS for apex/www, test redirects and compare preserved email records.
- Sitemap submission and indexing request must wait until the custom domain serves the new indexable site over verified HTTPS. Ownership verification is not proof of indexing or ranking.

## Reference-matching revision — 21 October 2026

The owner requested that the page look identical to thebarmitzvahlist.com and include Chaims Books in the description. This replaces the earlier distinct Chaims Books layout. The visible homepage wording, title, logo, Calibri typeface, gold buttons and fixed icon navigation now match the reference. The search description ends “In association with Chaims Books.” Basket, login and gift-list navigation opens the original service.

- Desktop 1440 × 1000 and mobile 390 × 844 were compared against the live reference. Logo, heading, description and button positions and sizes matched the measured reference geometry (logo width differs by less than 0.01 CSS pixels).
- Captured screenshot comparison at an 8/255 per-channel tolerance found 0.029% of desktop pixels and 0.160% of mobile pixels different, mostly small icon/rendering details. This is a same-browser snapshot comparison, not a guarantee for every platform.
- Checks at 320, 390, 768, 1024 and 1440 CSS pixels found no horizontal overflow. The logo and all fonts loaded, and the local browser warning/error log was empty.
- Kept accessible navigation names, focus styles, a skip link, a main landmark and one H1. Reference colours are intentionally retained; earlier distinct-design contrast numbers do not describe this revision.
- Default deployment remains noindex. GoDaddy forwarding, DNS and email settings remain unchanged; the owner requested to review this revised preview before approving launch.

### Revised preview publication

- Published source commit `ae1fd13e46cb7bbb585b936acc3af4da0125a02a` in Netlify deploy `6ad8e3214bc596d23afebce2`. The dashboard visibly confirmed successful publication of this exact commit.
- GitHub checks passed: https://github.com/solomonr/chaimsbooks/actions/runs/39631705756
- Auto publishing was shown as enabled, but no new automatic build appeared after the push. Used Netlify's existing **Trigger deploy → Deploy project** control, which fetched and published the correct GitHub commit. Automatic push-triggered build behavior remains unverified.
- Verified https://chaimsbooks.netlify.app/ returns the revised homepage with valid HTTPS, HTTP 200 and noindex. CSS, fonts, favicon and logo returned HTTP 200 and byte-for-byte matched the tested local assets. The branded error page returned HTTP 404.
- Reopened the public preview and verified the logo/fonts loaded, the matching desktop/mobile layout, and the Chaims Books search description. Public screenshot: ignored `qa/matching-public-desktop.png`; mobile: `qa/matching-public-mobile.png`. Preview assets total about 304 KB uncompressed.
- Verified the newly added basket destination returns HTTP 200 over HTTPS. Keyboard skip-link activation focuses `main`. All five footer links have accessible names.
- No domain switch is approved. The owner requested to see the corrected preview before deciding.

## Visible association line — 21 October 2026

After approving the matching preview design, the owner requested a visible Chaims Books mention. Added “In association with Chaims Books” directly below the welcome heading, with the existing search/social descriptions and organization data retained. Design approval does not authorize the pending GoDaddy domain switch.
