#!/usr/bin/env python3
"""
Script to fix absolute paths to relative paths for GitHub Pages deployment.
"""

import os
import re
from pathlib import Path

def get_depth(file_path, base_dir):
    """Calculate the depth of a file relative to base directory."""
    relative = os.path.relpath(file_path, base_dir)
    return relative.count(os.sep)

def get_prefix(depth):
    """Get the relative path prefix based on depth."""
    if depth == 0:
        return "./"
    else:
        return "../" * depth

def fix_html_file(file_path, base_dir):
    """Fix all absolute paths in an HTML file to relative paths."""

    depth = get_depth(file_path, base_dir)
    prefix = get_prefix(depth)

    print(f"Fixing {file_path} (depth: {depth}, prefix: {prefix})")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Fix CSS links
    content = re.sub(
        r'href="/static/css/',
        f'href="{prefix}static/css/',
        content
    )

    # Fix JS scripts
    content = re.sub(
        r'src="/static/js/',
        f'src="{prefix}static/js/',
        content
    )

    # Fix static images
    content = re.sub(
        r'src="/static/images/',
        f'src="{prefix}static/images/',
        content
    )

    # Fix meta refresh for CV page
    content = re.sub(
        r'content="0;url=/static/',
        f'content="0;url={prefix}static/',
        content
    )

    # Fix anchor links to /static/
    content = re.sub(
        r'href="/static/',
        f'href="{prefix}static/',
        content
    )

    # Fix navigation links - home
    content = re.sub(
        r'href="/"(\s+class="(logo|nav-link|mobile-link|error-link)")',
        f'href="{prefix}"\\1',
        content
    )

    # Fix breadcrumb home links
    content = re.sub(
        r'<a href="/">Home</a>',
        f'<a href="{prefix}">Home</a>',
        content
    )

    # Fix navigation links - projects
    content = re.sub(
        r'href="/projects"(\s+class="(nav-link|mobile-link|btn-outline)")',
        f'href="{prefix}projects/"\\1',
        content
    )

    # Fix navigation links - writings
    content = re.sub(
        r'href="/writings"(\s+class="(nav-link|mobile-link|btn-outline)")',
        f'href="{prefix}writings/"\\1',
        content
    )

    # Fix navigation links - resources
    content = re.sub(
        r'href="/resources"(\s+class="(nav-link|mobile-link)")',
        f'href="{prefix}resources/"\\1',
        content
    )

    # Fix navigation links - contact
    content = re.sub(
        r'href="/contact"(\s+class="(nav-link|mobile-link|btn-outline)")',
        f'href="{prefix}contact/"\\1',
        content
    )

    # Fix navigation links - cv
    content = re.sub(
        r'href="/cv"',
        f'href="{prefix}cv/"',
        content
    )

    # Fix project detail links (e.g., /projects/0, /projects/1)
    for i in range(10):
        content = re.sub(
            rf'href="/projects/{i}"',
            f'href="{prefix}projects/{i}/"' if depth == 0 else f'href="{"../" * (depth - 1)}{i}/"' if 'projects' in file_path else f'href="{prefix}projects/{i}/"',
            content
        )

    # Fix writings category links
    for category in ['articles', 'poems', 'essays', 'tips', 'creative-thinking', 'tech-news']:
        # For category links from writings index
        if 'writings/index.html' in file_path:
            content = re.sub(
                rf'href="/writings/{category}"',
                f'href="./{category}/"',
                content
            )
        else:
            content = re.sub(
                rf'href="/writings/{category}"',
                f'href="{prefix}writings/{category}/"',
                content
            )

    # Fix specific writing detail pages
    # This is more complex - we'll handle these with specific patterns
    # For now, fix obvious patterns
    content = re.sub(
        r'href="/writings/([^"]+)"',
        lambda m: f'href="{prefix}writings/{m.group(1)}/"' if not m.group(1).endswith('/') else f'href="{prefix}writings/{m.group(1)}"',
        content
    )

    # Fix "All Projects" links
    content = re.sub(
        r'href="/projects"',
        f'href="{prefix}projects/"' if depth != 1 or 'projects' not in file_path else 'href="../projects/"',
        content
    )

    # Special case: within projects folder
    if 'projects' in file_path and depth == 2:
        # Links to other projects
        content = re.sub(
            r'href="/projects/',
            'href="../',
            content
        )
        # "All Projects" link
        content = re.sub(
            r'href="\.\./projects/"',
            'href="../"',
            content
        )

    # Write back only if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [OK] Updated {file_path}")
        return True
    else:
        print(f"  [-] No changes needed for {file_path}")
        return False

def main():
    base_dir = Path(__file__).parent / 'docs'

    html_files = list(base_dir.rglob('*.html'))

    print(f"Found {len(html_files)} HTML files to process\n")

    fixed_count = 0
    for html_file in sorted(html_files):
        if fix_html_file(str(html_file), str(base_dir)):
            fixed_count += 1

    print(f"\n[DONE] Complete! Fixed {fixed_count} out of {len(html_files)} files")

if __name__ == '__main__':
    main()
