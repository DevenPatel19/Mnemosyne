import re
import yaml


def extract_frontmatter(content: str):
    """
    Extract YAML frontmatter metadata from markdown.
    """

    frontmatter_pattern = r"^---\s*\n(.*?)\n---\s*\n"
    match = re.search(frontmatter_pattern, content, re.DOTALL)

    metadata = {}

    if match:
        yaml_content = match.group(1)

        try:
            metadata = yaml.safe_load(yaml_content) or {}
        except Exception as e:
            print(f"YAML parse error: {e}")

        content = content[match.end():]

    return metadata, content


def extract_wikilinks(content: str):
    """
    Extract Obsidian wikilinks.
    Example: [[Distributed Systems]]
    """

    pattern = r"\[\[(.*?)\]\]"
    matches = re.findall(pattern, content)

    return matches


def extract_tags(content: str):
    """
    Extract inline Obsidian tags.
    Example: #ai #systems
    """

    pattern = r"#([a-zA-Z0-9_\-/]+)"
    matches = re.findall(pattern, content)

    return matches