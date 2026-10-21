# Domain launch and Search Console

## Approval boundary

Do not remove forwarding, add/change/delete DNS records, change nameservers, or connect the domain through an automated DNS wizard until the owner explicitly approves the exact live changes. Existing instructions to build and publish a preview do not authorize that switch. Leave GoDaddy as DNS provider.

## Before requesting approval

1. Complete deployment in the owner's Netlify Free account and record the actual temporary URL and deploy identifier.
2. Verify its HTTPS certificate, homepage, CSS, fonts, images, external links, FAQ, mobile layout and real 404 response. Verify the preview is noindex.
3. Record the current full GoDaddy zone and forwarding configuration in a local **ignored** `private/` folder. Public DNS queries alone cannot discover every DKIM selector or custom subdomain. Compare the complete zone in GoDaddy.
4. In Netlify, add `chaimsbooks.com` to the project without using automatic DNS setup or changing nameservers. Retain `www.chaimsbooks.com` as an alias and use `chaimsbooks.com` as primary, matching the canonical metadata. Review the exact DNS instructions shown for this site. Domain assignment in Netlify alone does not switch live traffic, but it may affect the temporary URL's redirects, so finish preview testing first.
5. Prepare an exact before/after record list and rollback plan, then request the owner's explicit approval immediately before the GoDaddy changes.

## Expected web-only changes (reconfirm against Netlify)

- Remove the existing permanent forwarding to `https://www.thebarmitzvahlist.com` only after approval.
- Replace the forwarding service's two apex A records, observed on 21 October 2026 as `3.33.251.168` and `15.197.225.128`, with the apex target specified in this project's Netlify domain instructions. Do not guess from old documentation or another project.
- Change the `www` CNAME from `chaimsbooks.com` to this site's exact Netlify hostname (no protocol or path).
- Check for conflicting web AAAA records before switching. None was returned by the initial public lookup, but recheck at launch.
- Preserve all Google MX records, SPF, DKIM, DMARC, Google verification TXT entries, `_domainconnect`, other subdomains, NS and SOA. Do not consolidate or replace existing TXT records.
- Do not create a root CNAME: it would conflict with the mail and verification records.

Keep the DNS backup local; it is not part of the public website or repository. Compare all non-web records before and after. DNS comparison protects configuration but does not by itself prove email delivery: have the owner perform an inbound/outbound email smoke test after the launch.

## Launch verification

1. After approval, make only the agreed forwarding and web-record changes.
2. Set `SITE_PRODUCTION=true` for Netlify's production context and publish the verified production build. Keep branch/deploy preview settings false.
3. Check propagation with authoritative DNS and public resolvers. Netlify must successfully provision a certificate for both apex and www before HTTPS is claimed verified.
4. Confirm `https://chaimsbooks.com/` returns 200 with the new homepage and a valid certificate; `https://www.chaimsbooks.com/` redirects to the canonical apex. Both HTTP forms should redirect to HTTPS without a loop. Check valid TLS on www before its redirect.
5. Check `/robots.txt` and `/sitemap.xml` return 200, canonical and social URLs use the live domain, the homepage has no meta or HTTP `noindex`, and no old forwarding remains. Request a nonexistent path and confirm HTTP 404 rather than a soft 404.
6. Recheck desktop/mobile rendering on the public domain, all assets and links, and the non-web DNS records. Record actual results and any propagation or certificate delays.

Netlify external DNS documentation: https://docs.netlify.com/manage/domains/configure-domains/configure-external-dns/

## Rollback

If the live site or certificates cannot be made functional, restore the exact recorded forwarding configuration and original web records only, then verify the old destination works again. Do not alter mail DNS. Restore a previous successful Netlify deploy for content problems. DNS rollback may take time because resolvers cache records; do not promise an instant reversal.

## Google Search Console

1. Use the owner's signed-in Search Console account and look for an existing `chaimsbooks.com` domain property. Existing Google verification TXT records were observed; do not delete them and do not assume they prove access for the currently signed-in account.
2. If there is no verified property, prefer a Domain property for `chaimsbooks.com`. Obtain its exact TXT verification value. Adding it at GoDaddy is a live DNS change and requires explicit approval. Add it alongside existing TXT records. A URL-prefix property with an HTML file or meta tag is an alternative that avoids DNS changes, but only covers that exact prefix.
3. Once the real domain is live, indexable and HTTPS verified, submit `https://chaimsbooks.com/sitemap.xml` in the matching property. Record Google's visible acceptance/result, not merely the button click.
4. Inspect `https://chaimsbooks.com/`, run the live URL test, and request indexing if the account and current quota permit. Record whether the request was accepted. Do not use the Indexing API for this ordinary website.
5. Later inspect the Page indexing and Performance reports for actual crawl/index status and searches for “Chaims Books”. A submitted sitemap or accepted request is not proof of indexing, ranking or a first-place result. Future monitoring is not scheduled unless the owner asks for it.

Official guidance:
- https://support.google.com/webmasters/answer/9008080
- https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl

## Separate pre-existing mail observation

The initial public DMARC response began with the literal text `Value: v=DMARC1; ...`, rather than starting directly with `v=DMARC1`. This may be a pre-existing configuration error. Record it for the owner, but **do not change it as part of the website launch**. It is unrelated to the web records and needs separate consideration.
