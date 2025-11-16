#!/usr/bin/env python3
"""
Transform Obsidian markdown files to GitHub Wiki format.
Adapted from ObsiWiki: https://github.com/ObsiWiki/ObsiWiki
"""

import re
import os
import shutil
from pathlib import Path


def transform_page_links(text, page_mapping=None):
    """
    Transform Obsidian page links to GitHub Wiki format with flattened names.
    Obsidian: [[Page Name|Link Text]] or [[Page Name]]
    GitHub Wiki: [[Link Text|Flattened-Page-Name]] or [[Flattened-Page-Name]]
    """
    if page_mapping is None:
        page_mapping = {}

    # Handle links with custom text: [[Page Name#Section|Link Text]] -> [[Link Text|Flattened-Page-Name#Section]]
    # Negative lookbehind to exclude image links (![[) and header links ([[#)
    # Negative lookahead to exclude already-transformed image links ([[images/)
    pattern = r'(?<!!)(?<!\[)\[\[(?!#)(?!images/)([^|\]]+)\|([^\]]+)\]\]'

    def replace_link(match):
        full_ref = match.group(1).strip()  # Could be "Page Name" or "Page Name#Section"
        link_text = match.group(2).strip()

        # Split page name and section anchor if present
        if '#' in full_ref:
            page_name, section = full_ref.split('#', 1)
            page_name = page_name.strip()
            section = section.strip()
        else:
            page_name = full_ref
            section = None

        # Use mapping if available, otherwise just replace spaces with hyphens
        if page_name in page_mapping:
            wiki_page_name = page_mapping[page_name]
        else:
            wiki_page_name = page_name.replace(' ', '-')

        # Reconstruct with section if present
        if section:
            wiki_ref = f'{wiki_page_name}#{section.replace(" ", "-")}'
        else:
            wiki_ref = wiki_page_name

        return f'[[{link_text}|{wiki_ref}]]'

    text = re.sub(pattern, replace_link, text)

    # Handle simple links: [[Page Name]] or [[Page Name#Section]]
    pattern = r'(?<!!)(?<!\[)\[\[(?!#)(?!images/)([^\]|]+)\]\]'

    def replace_simple_link(match):
        full_ref = match.group(1).strip()

        # Split page name and section anchor if present
        if '#' in full_ref:
            page_name, section = full_ref.split('#', 1)
            page_name = page_name.strip()
            section = section.strip()
        else:
            page_name = full_ref
            section = None

        # Use mapping if available
        if page_name in page_mapping:
            wiki_page_name = page_mapping[page_name]
        else:
            wiki_page_name = page_name.replace(' ', '-')

        # Reconstruct with section if present
        if section:
            wiki_ref = f'{wiki_page_name}#{section.replace(" ", "-")}'
        else:
            wiki_ref = wiki_page_name

        return f'[[{wiki_ref}]]'

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
    GitHub Wiki: ![](images/image.png) (standard markdown)
    """
    # Pattern handles optional parameters after pipe (e.g., | center, | 300)
    pattern = r'!\[\[([^\]|]+\.(png|jpg|jpeg|gif|svg|webp))(?:\s*\|[^\]]*)?\]\]'

    def replace_image(match):
        image_path = match.group(1).strip()
        # Extract just the filename, preserving spaces in the filename
        filename = os.path.basename(image_path)
        # URL-encode spaces for markdown
        filename_encoded = filename.replace(' ', '%20')
        return f'![](images/{filename_encoded})'

    return re.sub(pattern, replace_image, text, flags=re.IGNORECASE)


def fix_latex_spacing(text):
    """
    Add spacing around LaTeX equations when adjacent to other characters.
    $...$) doesn't render, but $...$ ) does
    """
    # Add space after closing $ if followed by punctuation/parentheses
    text = re.sub(r'\$([^\$]+)\$([)\],;:])', r'$\1$ \2', text)
    # Add space before opening $ if preceded by punctuation/parentheses
    text = re.sub(r'([(\[,])\$([^\$]+)\$', r'\1 $\2$', text)
    return text


def run_all_transformations(text, page_mapping=None):
    """Apply all transformations to convert Obsidian markdown to GitHub Wiki format."""
    text = fix_latex_spacing(text)
    text = transform_image_links(text)
    text = transform_header_links(text)
    text = transform_page_links(text, page_mapping)
    return text


def process_markdown_file(source_path, dest_path, page_mapping=None):
    """Process a single markdown file and write the transformed version."""
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    transformed = run_all_transformations(content, page_mapping)

    # Create parent directory if needed
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(transformed)


def build_page_mapping(ai_dir):
    """
    Build a mapping of page names to their flattened wiki names.
    Returns dict: {original_stem: flattened_name}
    """
    mapping = {}
    for md_file in ai_dir.rglob('*.md'):
        rel_path = md_file.relative_to(ai_dir)
        path_parts = list(rel_path.parts[:-1])
        filename_stem = rel_path.stem

        if path_parts:
            flat_name = '-'.join(path_parts + [filename_stem])
            flat_name = flat_name.replace(' ', '-')
        else:
            flat_name = filename_stem.replace(' ', '-')

        # Map original filename (without extension) to flattened name
        mapping[filename_stem] = flat_name

    return mapping


def sync_to_wiki():
    """Main function to sync Obsidian vault to GitHub Wiki."""
    # Paths
    repo_root = Path.cwd()
    ai_dir = repo_root / 'AI'
    readme_file = repo_root / 'README.md'
    media_dir = ai_dir / 'media'
    wiki_dir = repo_root / 'wiki'
    wiki_images_dir = wiki_dir / 'images'

    # Ensure wiki images directory exists
    wiki_images_dir.mkdir(parents=True, exist_ok=True)

    # Build page name mapping first
    print("Building page name mapping...")
    page_mapping = build_page_mapping(ai_dir)

    # Copy README.md to Home.md (GitHub Wiki homepage)
    if readme_file.exists():
        print("\nCopying README.md to Home.md...")
        home_path = wiki_dir / 'Home.md'
        process_markdown_file(readme_file, home_path, page_mapping)

    # Copy and transform all markdown files from AI/
    # GitHub Wiki doesn't support subdirectories, so flatten with meaningful names
    print("\nProcessing markdown files...")
    for md_file in ai_dir.rglob('*.md'):
        # Get relative path from AI directory
        rel_path = md_file.relative_to(ai_dir)

        # Flatten directory structure by converting path to filename
        # e.g., "Machine Learning & Data Science/PCA.md" -> "Machine-Learning-&-Data-Science-PCA.md"
        # Convert path parts to filename, replacing spaces and slashes with hyphens
        path_parts = list(rel_path.parts[:-1])  # All parts except filename
        filename_stem = rel_path.stem  # Filename without extension

        if path_parts:
            # Join path parts and filename with hyphens
            flat_name = '-'.join(path_parts + [filename_stem])
            flat_name = flat_name.replace(' ', '-')
            dest_path = wiki_dir / f'{flat_name}.md'
        else:
            # File is in AI root directory
            dest_path = wiki_dir / md_file.name

        print(f"  {rel_path} -> {dest_path.relative_to(wiki_dir)}")
        process_markdown_file(md_file, dest_path, page_mapping)

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
