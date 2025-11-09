"""
md_file_tool_generator.py

Generate a Markdown file with YAML frontmatter via the command line.

Required:
  -T, --title        Title of the tool

Optional:
  -a, --aliases      Comma-separated aliases
  -t, --tags         Comma-separated tags (must not contain spaces)
  -i, --id           Unique ID for the tool
  -ta, --tactic      Tactic name (human-readable)
  -r, --references   Comma-separated reference URLs
  -s, --synopsis     Custom synopsis text
  -u, --usage        Custom usage command (will be wrapped in bash code block)

Help:
  -h, --help         Show this help message and exit
"""

import argparse
import os
import re
import sys

def parse_csv(value: str):
    """Split a comma-separated string into a list, trimming whitespace and ignoring empties."""
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]

def sanitize_filename_component(name: str) -> str:
    """Sanitize a string for safe filename usage (replace os.sep, control chars)."""
    if name is None:
        return ""
    name = name.replace(os.path.sep, "_")
    name = re.sub(r"[:<>\"/\\|?*\x00-\x1f]", "_", name)
    name = name.strip()
    return name

def validate_tags(tags: list):
    """Ensure tags do not contain spaces."""
    for t in tags:
        if " " in t:
            print(f"Error: tag '{t}' contains spaces. Tags must be single words (use underscores if needed).", file=sys.stderr)
            sys.exit(1)

def generate_markdown(title: str, aliases: list, tags: list, tool_id: str, tactic: str, references: list, synopsis: str, usage: str) -> str:
    """Build the markdown content (YAML frontmatter + body)."""
    aliases_block = "aliases:\n" + "\n".join(f"  - {a}" for a in aliases) if aliases else "aliases: []"
    tags_block = "tags:\n" + "\n".join(f"  - {t}" for t in tags) if tags else "tags: []"
    references_body = "\n".join(f"- {r}" for r in references) if references else ""

    fence = "`" * 3
    usage_block = f"{fence}bash\n{usage}\n{fence}" if usage else f"{fence}bash\n# Add example usage here\n{fence}"

    frontmatter = (
        f"---\n"
        f"{aliases_block}\n"
        f"{tags_block}\n"
        f"title: {title}\n"
        f"id: {tool_id if tool_id else ''}\n"
        f"tactic: {tactic if tactic else ''}\n"
        f"---\n\n"
    )

    body = (
        "## Synopsis\n"
        f"{synopsis if synopsis else '(Add synopsis here)'}\n\n"
        "## Basic Usage\n"
        f"{usage_block}\n\n"
        "## References\n"
        f"{references_body}\n"
    )

    return frontmatter + body

def build_parser():
    p = argparse.ArgumentParser(
        prog="md_file_tool_generator.py",
        description="Generate a Markdown file for a tool with YAML frontmatter.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    p.add_argument("-T", "--title", dest="title", required=True,
                   help="Title of the tool (required). Example: -T \"Mimikatz\"")
    p.add_argument("-a", "--aliases", dest="aliases", required=False,
                   help="Comma-separated aliases. Example: -a \"MT,mytool\"")
    p.add_argument("-t", "--tags", dest="tags", required=False,
                   help="Comma-separated tags (must not contain spaces). Example: -t \"tool,references,credential_access\"")
    p.add_argument("-i", "--id", dest="id", required=False,
                   help="Unique ID for the tool. Example: -i TL0004")
    p.add_argument("-ta", "--tactic", dest="tactic", required=False,
                   help="Tactic name (human-readable). Example: -ta \"Credential Access\"")
    p.add_argument("-r", "--references", dest="references", required=False,
                   help="Comma-separated reference URLs. Example: -r \"https://github.com/example\"")
    p.add_argument("-s", "--synopsis", dest="synopsis", required=False,
                   help="Custom synopsis text for the tool.")
    p.add_argument("-u", "--usage", dest="usage", required=False,
                   help="Custom usage command (will be wrapped in a bash code block).")

    return p

def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    title = args.title.strip()
    tool_id = args.id.strip() if args.id else ""

    aliases = parse_csv(args.aliases) if args.aliases else []
    tags = parse_csv(args.tags) if args.tags else []
    references = parse_csv(args.references) if args.references else []
    tactic = args.tactic.strip() if args.tactic else ""
    synopsis = args.synopsis.strip() if args.synopsis else ""
    usage = args.usage.strip() if args.usage else ""

    validate_tags(tags)

    safe_title = sanitize_filename_component(title)
    safe_id = sanitize_filename_component(tool_id) if tool_id else "NOID"
    filename = f"{safe_id} - {safe_title}.md"

    content = generate_markdown(
        title=title,
        aliases=aliases,
        tags=tags,
        tool_id=tool_id,
        tactic=tactic,
        references=references,
        synopsis=synopsis,
        usage=usage
    )

    try:
        with open(filename, "w", encoding="utf-8") as fh:
            fh.write(content)
    except OSError as e:
        print(f"Error writing file '{filename}': {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Markdown file created: {filename}")

if __name__ == "__main__":
    main()