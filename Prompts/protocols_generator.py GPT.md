Generate a Python script called **`protocols_generator.py`**.  

### Requirements:  
- Creates a top-level folder named `protocols`.  
- For each protocol in a predefined list, writes a markdown file named `{ProtocolID} - {ProtocolName}.md` inside `protocols/`.  
- **Sanitize filenames** by replacing invalid characters (e.g., `/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`) with underscores. For example, `HTTP/S` should become `HTTP_S.md`.  
- Each markdown file must contain YAML frontmatter with:  
  - `aliases` list (provided per protocol).  
  - `tags` list containing:  
    - `"protocol"`  
    - `"references"`  
  - `title` set to the protocol name.  
  - `id` set to the protocol ID (e.g., `PR0004`).  
  - `references` list of relevant links (MITRE ATT&CK, Wikipedia, RFCs, etc.).  
- After the YAML frontmatter, include:  
  - `## Synopsis` section with a short description of how the protocol is abused.  
- Do **not** include a `## Basic Usage` section.  
- Must be runnable as a standalone script with a `main()` function and `if __name__ == "__main__": main()`.  
- Include at least the following protocols:  
  - **SMB**  
  - **RDP**  
  - **LDAP**  
  - **Kerberos**  
  - **DNS**  
  - **HTTP/S**  
  - **WinRM**  

