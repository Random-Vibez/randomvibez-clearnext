# ClearNext — RandomVibez.ai public-safe edition

ClearNext is a browser-local reading and planning aid: paste a notice, extract a bounded summary/date, and keep an editable action card. This directory is a separate static edition; the original `/srv/example-app/original-clearnext` is preserved and untouched.

## Boundary

- Static files only: no backend, API, database, accounts, cookies, analytics, service worker, external assets, or network calls.
- Cards stay in this browser's `localStorage`; they are not synchronized or shared. LocalStorage is not encryption.
- TXT/HTML input is bounded and HTML is converted to text with `DOMParser`; no submitted notice is sent anywhere.
- JSON export is unencrypted and may contain private text. Import is explicit, size-limited, schema-validated, duplicate-ID checked, and atomic.
- Cards, fields, files, and saved state are bounded. Untrusted values are rendered with `textContent`, not HTML interpolation.

## Safety

ClearNext does not contact organisations, submit forms, make payments, determine whether a notice is valid, or replace legal, medical, financial, or emergency advice. If a message indicates immediate danger, contact local emergency services directly. Do not enter passwords, full account numbers, government IDs, or other secrets.

## Local verification

```sh
node --check app.js
python3 tests/test_static.py
python3 -m http.server 4174
```

No deployment is included in this edition.
