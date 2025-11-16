#!/usr/bin/env python3
"""
Transform Obsidian markdown files to GitHub Wiki format.
Adapted from ObsiWiki: https://github.com/ObsiWiki/ObsiWiki
"""

import re
import os
import shutil
from pathlib import Path


def transform_page_links(text):
    """
    Transform Obsidian page links to GitHub Wiki format.
    Obsidian: [[Page Name|Link Text]] or [[Page Name]]
    GitHub Wiki: [[Link Text|Page-Name]] or [[Page-Name]]
    """
    # Handle links with custom text: [[Page Name|Link Text]] -> [[Link Text|Page-Name]]
    # Negative lookbehind to exclude image links (![[) and header links ([[#)
    # Negative lookahead to exclude already-transformed image links ([[images/)
    pattern = r'(?<!!)(?<!\[)\[\[(?!#)(?!images/)([^|\]]+)\|([^\]]+)\]\]'

    def replace_link(match):
        page_name = match.group(1).strip()
        link_text = match.group(2).strip()
        # Convert spaces to hyphens in page name for GitHub Wiki
        wiki_page_name = page_name.replace(' ', '-')
        return f'[[{link_text}|{wiki_page_name}]]'

    text = re.sub(pattern, replace_link, text)

    # Handle simple links: [[Page Name]] -> [[Page-Name]]
    # Negative lookbehind to exclude image links (![[) and header links ([[#)
    # Negative lookahead to exclude already-transformed image links ([[images/)
    pattern = r'(?<!!)(?<!\[)\[\[(?!#)(?!images/)([^\]|]+)\]\]'

    def replace_simple_link(match):
        page_name = match.group(1).strip()
        wiki_page_name = page_name.replace(' ', '-')
        return f'[[{wiki_page_name}]]'

    text = re.sub(pattern, replace_simple_link, text)

    return text


def transform_header_links(text):
    """
    Transform Obsidian header links to standard markdown.
    Obsidian: [[#Some Header|link text]]
    Markdown: [link text](#some-header)
    """
    pattern = r'\[\[#([^\]|]+)\|([^\]]+)\]\]'

    def replace_header(match):
        header = match.group(1).strip()
        link_text = match.group(2).strip()
        # Convert to lowercase and replace spaces with hyphens
        anchor = header.lower().replace(' ', '-')
        return f'[{link_text}](#{anchor})'

    return re.sub(pattern, replace_header, text)


def transform_image_links(text):
    """
    Transform Obsidian image links to GitHub Wiki format.
    Obsidian: ![[image.png]] or ![[path/image.png]] or ![[image.png | center]]
    GitHub Wiki: [[images/image.png]]
    """
    # Pattern handles optional parameters after pipe (e.g., | center, | 300)
    pattern = r'!\[\[([^\]|]+\.(png|jpg|jpeg|gif|svg|webp))(?:\s*\|[^\]]*)?\]\]'

    def replace_image(match):
        image_path = match.group(1).strip()
        # Extract just the filename, preserving spaces in the filename
        filename = os.path.basename(image_path)
        return f'[[images/{filename}]]'

    return re.sub(pattern, replace_image, text, flags=re.IGNORECASE)


def run_all_transformations(text):
    """Apply all transformations to convert Obsidian markdown to GitHub Wiki format."""
    text = transform_image_links(text)
    text = transform_header_links(text)
    text = transform_page_links(text)
    return text


def process_markdown_file(source_path, dest_path):
    """Process a single markdown file and write the transformed version."""
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    transformed = run_all_transformations(content)

    # Create parent directory if needed
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(transformed)


def sync_to_wiki():
    """Main function to sync Obsidian vault to GitHub Wiki."""
    # Paths
    repo_root = Path.cwd()
    ai_dir = repo_root / 'AI'
    media_dir = ai_dir / 'media'
    wiki_dir = repo_root / 'wiki'
    wiki_images_dir = wiki_dir / 'images'

    # Ensure wiki images directory exists
    wiki_images_dir.mkdir(parents=True, exist_ok=True)

    # Copy and transform all markdown files from AI/
    print("Processing markdown files...")
    for md_file in ai_dir.rglob('*.md'):
        # Get relative path from AI directory
        rel_path = md_file.relative_to(ai_dir)

        # Destination path in wiki (flatten structure or preserve?)
        # Option 1: Flatten - all files in wiki root
        # dest_path = wiki_dir / md_file.name

        # Option 2: Preserve directory structure
        dest_path = wiki_dir / rel_path

        print(f"  {rel_path} -> {dest_path.relative_to(wiki_dir)}")
        process_markdown_file(md_file, dest_path)

    # Copy all images from AI/media/ to wiki/images/
    print("\nCopying images...")
    if media_dir.exists():
        for image_file in media_dir.iterdir():
            if image_file.is_file() and image_file.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp']:
                dest_image = wiki_images_dir / image_file.name
                print(f"  {image_file.name} -> images/{image_file.name}")
                shutil.copy2(image_file, dest_image)

    # Also check for images in AI/media subdirectories
    for image_file in ai_dir.rglob('media/**/*'):
        if image_file.is_file() and image_file.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp']:
            dest_image = wiki_images_dir / image_file.name
            print(f"  {image_file.relative_to(ai_dir)} -> images/{image_file.name}")
            shutil.copy2(image_file, dest_image)

    print("\nSync complete!")


if __name__ == '__main__':
    sync_to_wiki()
