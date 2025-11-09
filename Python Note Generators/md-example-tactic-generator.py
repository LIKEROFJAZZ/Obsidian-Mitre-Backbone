import os

"""
tactics_generator.py

Creates MITRE tactic folders and one markdown file per tactic.
Each file contains aliases, tags (tactic + normalized tactic name), title, and ID.
"""

import os

tactics = [
    {"id": "TA0043", "title": "Reconnaissance", "aliases": ["Reconnaissance", "Recon"]},
    {"id": "TA0042", "title": "Resource Development", "aliases": ["Resource Development"]},
    {"id": "TA0001", "title": "Initial Access", "aliases": ["Initial Access"]},
    {"id": "TA0002", "title": "Execution", "aliases": ["Execution"]},
    {"id": "TA0003", "title": "Persistence", "aliases": ["Persistence"]},
    {"id": "TA0004", "title": "Privilege Escalation", "aliases": ["Privilege Escalation"]},
    {"id": "TA0005", "title": "Defense Evasion", "aliases": ["Defense Evasion"]},
    {"id": "TA0006", "title": "Credential Access", "aliases": ["Credential Access"]},
    {"id": "TA0007", "title": "Discovery", "aliases": ["Discovery"]},
    {"id": "TA0008", "title": "Lateral Movement", "aliases": ["Lateral Movement"]},
    {"id": "TA0009", "title": "Collection", "aliases": ["Collection"]},
    {"id": "TA0011", "title": "Command and Control", "aliases": ["Command and Control", "C2"]},
    {"id": "TA0010", "title": "Exfiltration", "aliases": ["Exfiltration"]},
    {"id": "TA0040", "title": "Impact", "aliases": ["Impact"]},
]

output_dir = "mitre_tactics"
os.makedirs(output_dir, exist_ok=True)

def normalize_tag(name: str) -> str:
    return name.lower().replace(" ", "_")

def generate_markdown(tactic: dict) -> str:
    aliases_formatted = "\n".join([f"  - {alias}" for alias in tactic["aliases"]])
    return f"""---
aliases:
{aliases_formatted}
tags:
  - tactic
  - {normalize_tag(tactic['title'])}
title: {tactic['title']}
id: {tactic['id']}
---
"""

def main():
    for tactic in tactics:
        folder_name = f"{tactic['id']} - {tactic['title']}"
        folder_path = os.path.join(output_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        filename = f"{tactic['id']} - {tactic['title']}.md"
        filepath = os.path.join(folder_path, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(generate_markdown(tactic))

    print(f"Tactic folders + files created under: {output_dir}")

if __name__ == "__main__":
    main()