#!/usr/bin/env python3
"""
tools_generator.py

Writes tool .md files into a top-level "tools/" directory.
Each file contains YAML frontmatter (aliases, tags, title, id, tactic, related_tactic),
a short synopsis, usage code block, and references.

Tags include: tool, references, normalized tactic name.
"""

import os

tools_dir = "tools"

def normalize_tag(name: str) -> str:
    return name.lower().replace(" ", "_")

tools = [
    {
        "id": "TL0001",
        "title": "Nmap",
        "aliases": ["Nmap"],
        "tactic": {"name": "Reconnaissance", "id": "TA0043"},
        "synopsis": "Nmap is a network scanner used to discover hosts, services, and vulnerabilities.",
        "usage": "nmap -sV target.com",
        "references": ["https://nmap.org/", "https://github.com/nmap/nmap"],
    },
    {
        "id": "TL0002",
        "title": "Metasploit",
        "aliases": ["Metasploit Framework", "MSF"],
        "tactic": {"name": "Initial Access", "id": "TA0001"},
        "synopsis": "Metasploit is a penetration testing framework that provides exploits, payloads, and auxiliary modules.",
        "usage": "msfconsole",
        "references": ["https://www.metasploit.com/", "https://github.com/rapid7/metasploit-framework"],
    },
    {
        "id": "TL0003",
        "title": "Cobalt Strike",
        "aliases": ["Cobalt Strike"],
        "tactic": {"name": "Command and Control", "id": "TA0011"},
        "synopsis": "Cobalt Strike is a commercial red team platform for adversary simulation and post-exploitation.",
        "usage": "./teamserver <ip> <password>",
        "references": ["https://www.cobaltstrike.com/"],
    },
    {
        "id": "TL0004",
        "title": "Mimikatz",
        "aliases": ["Mimikatz"],
        "tactic": {"name": "Credential Access", "id": "TA0006"},
        "synopsis": "Mimikatz is a tool for extracting plaintexts, hashes, PIN codes, and Kerberos tickets from memory.",
        "usage": 'mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords"',
        "references": ["https://github.com/gentilkiwi/mimikatz"],
    },
    {
        "id": "TL0005",
        "title": "Empire",
        "aliases": ["Empire"],
        "tactic": {"name": "Execution", "id": "TA0002"},
        "synopsis": "Empire is a post-exploitation framework that provides PowerShell and Python agents for red team operations.",
        "usage": "python empire.py",
        "references": ["https://github.com/EmpireProject/Empire"],
    },
    {
        "id": "TL0006",
        "title": "BloodHound",
        "aliases": ["BloodHound"],
        "tactic": {"name": "Discovery", "id": "TA0007"},
        "synopsis": "BloodHound maps Active Directory relationships to identify attack paths and privilege escalation opportunities.",
        "usage": "bloodhound --no-sandbox",
        "references": ["https://github.com/BloodHoundAD/BloodHound"],
    },
    {
        "id": "TL0007",
        "title": "Responder",
        "aliases": ["Responder"],
        "tactic": {"name": "Credential Access", "id": "TA0006"},
        "synopsis": "Responder is an LLMNR, NBT-NS, and MDNS poisoner that captures NTLMv1/NTLMv2 hashes on Windows networks.",
        "usage": "responder -I eth0",
        "references": ["https://github.com/lgandx/Responder"],
    },
    {
        "id": "TL0008",
        "title": "Impacket",
        "aliases": ["Impacket"],
        "tactic": {"name": "Lateral Movement", "id": "TA0008"},
        "synopsis": "Impacket is a collection of Python classes for working with network protocols, widely used for lateral movement.",
        "usage": "psexec.py DOMAIN/user:password@target",
        "references": ["https://github.com/fortra/impacket"],
    },
    {
        "id": "TL0009",
        "title": "Sliver",
        "aliases": ["Sliver C2"],
        "tactic": {"name": "Command and Control", "id": "TA0011"},
        "synopsis": "Sliver is an open-source C2 framework that supports implants and operators for red team operations.",
        "usage": "./sliver-server",
        "references": ["https://github.com/BishopFox/sliver"],
    },
    {
        "id": "TL0010",
        "title": "CrackMapExec",
        "aliases": ["CME", "CrackMapExec"],
        "tactic": {"name": "Discovery", "id": "TA0007"},
        "synopsis": "CrackMapExec is a Swiss army knife for pentesting Active Directory networks, supporting SMB, RDP, and WinRM.",
        "usage": "crackmapexec smb 192.168.1.0/24 -u user -p password",
        "references": ["https://github.com/byt3bl33d3r/CrackMapExec"],
    },
]

def generate_tool_markdown(tool: dict) -> str:
    aliases_formatted = "\n".join([f"  - {alias}" for alias in tool["aliases"]])
    references_formatted = "\n".join([f"- {ref}" for ref in tool["references"]])
    tactic_tag = normalize_tag(tool["tactic"]["name"])
    fence = "`" * 3
    usage_block = f"{fence}bash\n{tool['usage']}\n{fence}"
    return (
        f"---\n"
        f"aliases:\n{aliases_formatted}\n"
        f"tags:\n"
        f"  - tool\n"
        f"  - references\n"
        f"  - {tactic_tag}\n"
        f"title: {tool['title']}\n"
        f"id: {tool['id']}\n"
        f"tactic: {tool['tactic']['name']}\n"
        f"related_tactic: {tool['tactic']['id']}\n"
        f"---\n\n"
        f"## Synopsis\n"
        f"{tool['synopsis']}\n\n"
        f"## Basic Usage\n"
        f"{usage_block}\n\n"
        f"## References\n"
        f"{references_formatted}\n"
    )

def main():
    os.makedirs(tools_dir, exist_ok=True)

    created = 0
    for tool in tools:
        filename = f"{tool['id']} - {tool['title']}.md"
        filepath = os.path.join(tools_dir, filename)

        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write(generate_tool_markdown(tool))
        created += 1

    print(f"Done. Created {created} tool files in '{tools_dir}/'.")

if __name__ == "__main__":
    main()