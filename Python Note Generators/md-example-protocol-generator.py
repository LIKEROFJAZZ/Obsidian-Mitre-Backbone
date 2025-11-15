#!/usr/bin/env python3
"""
protocols_generator.py

Writes protocol .md files into a top-level "protocols/" directory.
Each file contains YAML frontmatter (aliases, tags, title, id, tactic, related_tactic),
a short synopsis, and references.

Tags include: protocol, references, normalized tactic name.
"""

import os
import re

protocols_dir = "protocols"

def normalize_tag(name: str) -> str:
    return name.lower().replace(" ", "_")

def sanitize_filename(name: str) -> str:
    """Replace invalid filename characters with underscores."""
    return re.sub(r'[<>:"/\\|?*]', "_", name)

protocols = [
    {
        "id": "PR0001",
        "title": "SMB",
        "aliases": ["Server Message Block", "SMBv1", "SMBv2", "SMBv3"],
        "tactic": {"name": "Lateral Movement", "id": "TA0008"},
        "synopsis": "SMB is a network file sharing protocol often abused for lateral movement and remote code execution in Windows environments.",
        "references": ["https://attack.mitre.org/techniques/T1021/002/", "https://en.wikipedia.org/wiki/Server_Message_Block"],
    },
    {
        "id": "PR0002",
        "title": "RDP",
        "aliases": ["Remote Desktop Protocol", "RDP"],
        "tactic": {"name": "Lateral Movement", "id": "TA0008"},
        "synopsis": "RDP allows remote graphical logins to Windows systems. It is commonly targeted for credential brute force, lateral movement, and persistence.",
        "references": ["https://attack.mitre.org/techniques/T1021/001/", "https://en.wikipedia.org/wiki/Remote_Desktop_Protocol"],
    },
    {
        "id": "PR0003",
        "title": "LDAP",
        "aliases": ["Lightweight Directory Access Protocol", "LDAP"],
        "tactic": {"name": "Discovery", "id": "TA0007"},
        "synopsis": "LDAP is widely used in Active Directory environments and can be abused for enumeration of users, groups, and sensitive attributes.",
        "references": ["https://attack.mitre.org/techniques/T1018/", "https://ldap.com/"],
    },
    {
        "id": "PR0004",
        "title": "Kerberos",
        "aliases": ["Kerberos Authentication"],
        "tactic": {"name": "Credential Access", "id": "TA0006"},
        "synopsis": "Kerberos is an authentication protocol used in Active Directory. Attackers abuse it for credential theft (e.g., Kerberoasting, Golden Ticket).",
        "references": ["https://attack.mitre.org/techniques/T1558/", "https://en.wikipedia.org/wiki/Kerberos_(protocol)"],
    },
    {
        "id": "PR0005",
        "title": "DNS",
        "aliases": ["Domain Name System"],
        "tactic": {"name": "Command and Control", "id": "TA0011"},
        "synopsis": "DNS can be abused for tunneling, data exfiltration, or establishing command and control channels.",
        "references": ["https://attack.mitre.org/techniques/T1071/004/", "https://en.wikipedia.org/wiki/Domain_Name_System"],
    },
    {
        "id": "PR0006",
        "title": "HTTP/S",
        "aliases": ["Hypertext Transfer Protocol", "HTTP", "HTTPS"],
        "tactic": {"name": "Command and Control", "id": "TA0011"},
        "synopsis": "HTTP and HTTPS are commonly abused for C2 communication due to their ubiquity and ability to blend with normal traffic.",
        "references": ["https://attack.mitre.org/techniques/T1071/001/", "https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol"],
    },
    {
        "id": "PR0007",
        "title": "WinRM",
        "aliases": ["Windows Remote Management", "WinRM"],
        "tactic": {"name": "Lateral Movement", "id": "TA0008"},
        "synopsis": "WinRM is a Windows protocol for remote management. Attackers abuse it to execute commands remotely in domain environments.",
        "references": ["https://attack.mitre.org/techniques/T1021/006/", "https://learn.microsoft.com/en-us/windows/win32/winrm/portal"],
    },
]

def generate_protocol_markdown(proto: dict) -> str:
    aliases_formatted = "\n".join([f"  - {alias}" for alias in proto["aliases"]])
    references_formatted = "\n".join([f"- {ref}" for ref in proto["references"]])
    tactic_tag = normalize_tag(proto["tactic"]["name"])
    return (
        f"---\n"
        f"aliases:\n{aliases_formatted}\n"
        f"tags:\n"
        f"  - protocol\n"
        f"  - references\n"
        f"  - {tactic_tag}\n"
        f"title: {proto['title']}\n"
        f"id: {proto['id']}\n"
        f"tactic: {proto['tactic']['name']}\n"
        f"related_tactic: {proto['tactic']['id']}\n"
        f"---\n\n"
        f"## Synopsis\n"
        f"{proto['synopsis']}\n\n"
        f"## References\n"
        f"{references_formatted}\n"
    )

def main():
    os.makedirs(protocols_dir, exist_ok=True)

    created = 0
    for proto in protocols:
        safe_title = sanitize_filename(proto['title'])
        filename = f"{proto['id']} - {safe_title}.md"
        filepath = os.path.join(protocols_dir, filename)

        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write(generate_protocol_markdown(proto))
        created += 1

    print(f"Done. Created {created} protocol files in '{protocols_dir}/'.")

if __name__ == "__main__":
    main()
