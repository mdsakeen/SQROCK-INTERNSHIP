# Day 02 - Email Harvesting & Social Engineering Prep

Purpose: extract email-shaped strings from an authorized lab webpage. Use only local/lab pages or systems explicitly authorized by Sqrock.

Run:
```powershell
python -m http.server 8000 --directory data
python src/email_harvester.py http://127.0.0.1:8000/lab_page.html
```
Deliverable: script, sanitized JSON list, screenshot, short attacker/defender write-up.
