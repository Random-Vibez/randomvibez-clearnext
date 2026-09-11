#!/usr/bin/env python3
"""Static contract checks for the public-safe ClearNext edition."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / "index.html").read_text()
js = (ROOT / "app.js").read_text()
css = (ROOT / "styles.css").read_text()
readme = (ROOT / "README.md").read_text()
security = (ROOT / "SECURITY.md").read_text()
required = {"index.html", "app.js", "styles.css", "README.md", "SECURITY.md", ".htaccess", "randomvibez-logo.jpg"}
assert required.issubset({p.name for p in ROOT.iterdir()})
assert 'src="app.js"' in html and 'href="styles.css"' in html
assert 'randomvibez-logo.jpg' in html and 'https://randomvibez.ai/' in html
assert "A RandomVibez.ai Project" in html and "ONLINE TOOLS. BUILT BY AI. FOR EVERYONE." in html
assert all(term in (html + readme + security).lower() for term in ("medical", "financial", "emergency", "localstorage"))
assert 'localStorage' in js and 'MAX_FILE=500000' in js and 'MAX_CARDS=100' in js
assert "c.date.certainty!=='found'" in js and "new Set" in js
assert "replace(/[;,]/g" in js and "cards=previous" in js
assert 'DOMParser' in js and 'textContent' in js and 'innerHTML' not in js
assert not re.search(r"(?:fetch\s*\(|XMLHttpRequest|\baxios\b|navigator\.sendBeacon|document\.cookie|indexedDB|serviceWorker)", html + js, re.I)
urls = re.findall(r"https?://[^\"'\\s<]+", html + js + css)
assert all(url.rstrip('/') == "https://randomvibez.ai" for url in urls)
assert not re.search(r"//cdn|google-analytics|plausible", html + js + css, re.I)
ht = (ROOT / ".htaccess").read_text()
for header in ("Strict-Transport-Security", "Content-Security-Policy", "connect-src 'none'", "X-Content-Type-Options", "X-Frame-Options", "Options -Indexes"):
    assert header in ht
assert "no encryption" in readme.lower() or "not encryption" in readme.lower()
assert "unencrypted" in security.lower() and "no backend" in readme.lower()
print("PASS: ClearNext public static contract")
print("PASS: bounds, schema validation, safe text rendering, and local-only boundary")
print("PASS: branding, disclaimers, and security headers present")
