# Verification record — 21 October 2026

This record distinguishes historical checkpoints from the latest launch results at the end of the file.

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

## Outstanding at the initial checkpoint (historical)

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

## Approved custom-domain launch — 21 October 2026

- The owner explicitly approved the final live switch: “Yes, launch at chaimsbooks.com”.
- Production indexing is enabled only in Netlify's production context through `netlify.toml`; branch/deploy preview contexts remain noindex.
- Source commit `6932de16657ce906a7b0e34a0ef0ca41a039aab0` was published in Netlify deploy `6ad8e7b05a6f0352a7f5bbd5`, with dashboard confirmation. Build and publication completed in 9 seconds. GitHub checks passed: https://github.com/solomonr/chaimsbooks/actions/runs/39634518231
- Removed GoDaddy's old permanent forwarding. GoDaddy replaced its managed forwarding addresses with a parked record; edited that record to the approved apex A `75.2.60.5`, retaining a one-hour TTL. Changed only the `www` CNAME to `chaimsbooks.netlify.app` with a one-hour TTL.
- The resulting zone has 17 records. Compared every backed-up non-web record on both `ns05.domaincontrol.com` and `ns06.domaincontrol.com`: Google MX, SPF, DKIM, DMARC, verification TXT, `_domainconnect`, nameservers and other unchanged sets matched. The SOA serial changed automatically. No email delivery test was performed.
- Cloudflare `1.1.1.1` and Google `8.8.8.8` both returned the new apex A and www CNAME. Netlify's DNS verification succeeded. HTTP served the approved homepage with the visible association line.
- Let’s Encrypt issued a certificate covering both apex and www, expiring 19 January 2027. Normal certificate validation succeeded on both hosts. The homepage returns HTTPS 200; HTTP apex redirects 301 to HTTPS apex; HTTP www redirects 301 to HTTPS www, then 301 to HTTPS apex, without a loop.
- All published static files byte-match the tested `dist` build. `/robots.txt` and `/sitemap.xml` return 200; canonical metadata identifies the live apex; the homepage has `index, follow` and no HTTP noindex header. A nonexistent path returns the branded HTTP 404 page. Security headers are present.
- Live desktop 1440 × 1000 and mobile 390 × 844 checks passed: no horizontal overflow, logo and fonts loaded, visible Chaims Books association line, and empty browser warning/error log. Screenshots: ignored `qa/live-desktop.png` and `qa/live-mobile.png`. HTTP and certificate evidence: `qa/live-verification.json`.
- Search Console live homepage test at 17:33 London time reported “URL is available to Google”, “Page can be indexed”, crawl allowed **Yes**, page fetch **Successful**, indexing allowed **Yes**, and user-declared canonical `https://chaimsbooks.com/`.
- Requested indexing for the homepage; Google visibly confirmed “Indexing requested” and addition to its priority crawl queue. This is not a claim that Google has indexed or ranked the site.
- Submitted `https://chaimsbooks.com/sitemap.xml`; Google confirmed submission, but the Sitemaps table reported “Couldn’t fetch”. Retried submission once after the successful live homepage test; the table still showed that status. The file returns HTTPS 200 and validates as XML. Google’s live sitemap URL test at 17:35 London time returned “URL is available to Google”, crawl allowed **Yes**, and page fetch **Successful**. No indexing request was made for the XML file. The sitemap report has not yet confirmed successful processing; recheck that report later. The successful live fetch is evidence of accessibility, not completed sitemap processing.


## Remaining external follow-up

- Recheck the Sitemaps report for successful processing of `https://chaimsbooks.com/sitemap.xml`, then the homepage’s indexing and Performance reports. Google’s processing schedule and search ranking are outside the site’s control; no ranking or completed indexing is claimed.
- DNS caches outside the resolvers checked may take time to expire. Email DNS was preserved, but the owner can perform a normal inbound/outbound mail smoke test to verify delivery separately.
- No recurring monitoring, paid plan, analytics service or notification automation was created.
