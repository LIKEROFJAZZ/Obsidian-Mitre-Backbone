---
aliases:
  - Responder
tags:
  - tool
  - credential_access
title: Responder
id: TL0007
tactic: Credential Access
related_tactic: TA0006
---

## Synopsis
Responder is an LLMNR, NBT-NS, and MDNS poisoner that captures NTLMv1/NTLMv2 hashes on Windows networks.

## Basic Usage
```bash
responder -I eth0
```

## References
- https://github.com/lgandx/Responder
