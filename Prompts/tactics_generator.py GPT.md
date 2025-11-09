Generate a Python script called **`tactics_generator.py`**.  

### Requirements:  
- Creates a folder named `mitre_tactics`.  
- Inside, creates a subfolder for each MITRE ATT&CK Enterprise tactic (14 total).  
- Inside each folder, writes a markdown file named `{TacticID} - {TacticName}.md`.  
- Each markdown file must contain YAML frontmatter with:  
  - `aliases` list (provided per tactic).  
  - `tags` list containing:  
    - `"tactic"`  
    - the **tactic name normalized** (lowercase, spaces replaced with underscores, e.g., `credential_access`).  
  - `title` set to the tactic name.  
  - `id` set to the tactic ID (e.g., `TA0006`).  
  - `references` list (with at least the MITRE ATT&CK tactic page link).  
- Do **not** include tactic IDs in the tags.  
- Do not include any body text beyond the YAML frontmatter.  
- Must be runnable as a standalone script with a `main()` function and `if __name__ == "__main__": main()`.  
- Include all 14 ATT&CK Enterprise tactics with their official IDs, names, common aliases, and MITRE ATT&CK references.  
