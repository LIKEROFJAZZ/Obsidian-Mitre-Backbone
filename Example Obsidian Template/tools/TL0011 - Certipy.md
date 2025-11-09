---
aliases:
  - Certipy
tags:
  - tool
  - reconnaissance
  - credential_access
title: Certipy
id: TL0011
tactic: Reconnaissance, Privilege Escalation
---

## Synopsis
certipy is a comprehensive toolkit for enumerating, identifying, and exploiting AD CS misconfigurations. It automates the discovery of vulnerable CAs and templates, streamlining attacks involving ESCs, certificate requests over multiple protocols

## Basic Usage
```bash
certipy find -u 'domain\\user' -p 'password' -dc-ip <domain_controller_ip>
```

## References
- https://github.com/ly4k/Certipy
