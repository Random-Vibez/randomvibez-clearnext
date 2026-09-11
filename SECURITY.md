# ClearNext public security boundary

This edition is intentionally browser-local and static. It has no server persistence, authentication, API, database, cookie, analytics, external asset, service worker, or network request. The `.htaccess` supplies HSTS, CSP with `connect-src 'none'`, frame denial, MIME sniffing protection, restrictive referrer/permissions policy, directory-listing prevention, and no-store caching when Apache headers are enabled.

The application treats localStorage as untrusted input: it caps serialized state and card counts, validates and normalizes allowlisted fields, and falls back safely on malformed data. File sizes are checked before reading; imports are checked before parsing/commit. Exported JSON is unencrypted. Keep backups private and do not store passwords, government IDs, full account numbers, diagnoses, or other sensitive secrets.

The deterministic extraction is not professional review and can miss or misread dates. Dates, summaries, and suggested steps must be checked against the original notice. This is not legal, medical, financial, or emergency advice and does not provide monitoring, dispatch, or guaranteed availability.

Serve only this directory as static content. Do not add routes, remote scripts, uploads, credentials, shared storage, or analytics without a new security review. Live HTTPS/header and browser checks remain hosting-side release work and were not performed here.
