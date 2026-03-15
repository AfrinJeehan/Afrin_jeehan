"""
build.py — Freeze the Flask portfolio into static HTML for GitHub Pages.

Usage:
  python build.py                        # For user/org sites  (username.github.io)
  python build.py /Afrin_jeehan          # For project sites   (username.github.io/Afrin_jeehan)

Output goes to the  docs/  folder.  Configure GitHub Pages to serve from /docs on the main branch.
"""

import os
import re
import sys
import shutil
from run import app, projects, writings, writing_categories

DOCS = "docs"


# ── helpers ──────────────────────────────────────────────────────────────────

def save(html: str, *path_parts):
    """Write *html* to  docs/<path_parts>/index.html  (or direct filename)."""
    dest = os.path.join(DOCS, *path_parts)
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  + {dest}")


def fetch(client, url: str) -> str:
    """GET *url* via Flask test client, return decoded HTML."""
    resp = client.get(url)
    if resp.status_code != 200:
        print(f"  ! {url} → {resp.status_code} (skipped)")
        return ""
    return resp.data.decode("utf-8")


def rebase(html: str, base: str) -> str:
    """Rewrite absolute internal paths so they work under a sub-path on GitHub Pages.

    e.g. href="/projects" → href="/Afrin_jeehan/projects"
         src="/static/css/style.css" → src="/Afrin_jeehan/static/css/style.css"
    """
    # Match href="/" or src="/" exactly (home link)
    html = html.replace('href="/"', f'href="{base}"')

    # Match href/src/content pointing to known internal prefixes
    internal = r'(href|src|content)="(/(?:static|projects|writings|contact|cv|api|resources)(?:/[^"]*)?)"'
    html = re.sub(
        internal,
        lambda m: f'{m.group(1)}="{base}{m.group(2).lstrip("/")}"',
        html,
    )
    return html


# ── main build ───────────────────────────────────────────────────────────────

def build(base_path="/"):
    # Normalise base_path  →  "/" or "/Afrin_jeehan/"
    if base_path != "/":
        base_path = "/" + base_path.strip("/") + "/"

    print(f"\n{'=' * 50}")
    print(f"  Building static site  →  {DOCS}/")
    print(f"  Base path: {base_path}")
    print(f"{'=' * 50}\n")

    # 1. Clean previous build
    if os.path.exists(DOCS):
        shutil.rmtree(DOCS)
    os.makedirs(DOCS)

    # 2. Render every route via Flask's test client
    with app.test_client() as c:

        # ── Home ──
        html = fetch(c, "/")
        if html:
            if base_path != "/":
                html = rebase(html, base_path)
            save(html, "index.html")

        # ── Projects list ──
        html = fetch(c, "/projects")
        if html:
            if base_path != "/":
                html = rebase(html, base_path)
            save(html, "projects", "index.html")

        # ── Individual projects ──
        for i in range(len(projects)):
            html = fetch(c, f"/projects/{i}")
            if html:
                if base_path != "/":
                    html = rebase(html, base_path)
                save(html, "projects", str(i), "index.html")

        # ── Contact ──
        html = fetch(c, "/contact")
        if html:
            if base_path != "/":
                html = rebase(html, base_path)
            save(html, "contact", "index.html")

        # ── Resources / Knowledge Hub ──
        html = fetch(c, "/resources")
        if html:
            if base_path != "/":
                html = rebase(html, base_path)
            save(html, "resources", "index.html")

        # ── Writings hub ──
        html = fetch(c, "/writings")
        if html:
            if base_path != "/":
                html = rebase(html, base_path)
            save(html, "writings", "index.html")

        # ── Writing categories & individual writings ──
        for cat_key in writing_categories:
            html = fetch(c, f"/writings/{cat_key}")
            if html:
                if base_path != "/":
                    html = rebase(html, base_path)
                save(html, "writings", cat_key, "index.html")

            for w in writings.get(cat_key, []):
                wid = w["id"]
                html = fetch(c, f"/writings/{cat_key}/{wid}")
                if html:
                    if base_path != "/":
                        html = rebase(html, base_path)
                    save(html, "writings", cat_key, wid, "index.html")

    # 3. 404 page (rendered directly, not via a route)
    with app.test_request_context():
        from flask import render_template
        html_404 = render_template("404.html")
        if base_path != "/":
            html_404 = rebase(html_404, base_path)
        save(html_404, "404.html")

    # 4. Copy all static assets (css, js, images, PDF, etc.)
    shutil.copytree("static", os.path.join(DOCS, "static"))
    print(f"  + {DOCS}/static/  (all assets)")

    # 5. CV redirect  —  /cv  →  opens the PDF
    cv_pdf_url = f"{base_path}static/Afrin_Jeehan_CV.pdf"
    cv_redirect = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0;url={cv_pdf_url}">
  <title>CV — Afrin Jeehan</title>
</head>
<body>
  <p>Redirecting to <a href="{cv_pdf_url}">CV (PDF)</a>…</p>
</body>
</html>"""
    save(cv_redirect, "cv", "index.html")

    # 6. .nojekyll  —  tells GitHub Pages to skip Jekyll processing
    open(os.path.join(DOCS, ".nojekyll"), "w").close()
    print(f"  + {DOCS}/.nojekyll")

    # ── Summary ──
    total = sum(len(f) for _, _, f in os.walk(DOCS))
    print(f"\n{'=' * 50}")
    print(f"  Done!  {total} files in {DOCS}/")
    print(f"  Configure GitHub Pages → Source: main branch, /docs folder")
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    base = sys.argv[1] if len(sys.argv) > 1 else "/"
    build(base)
