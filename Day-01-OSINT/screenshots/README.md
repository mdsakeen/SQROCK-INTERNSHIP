# Screenshot instructions

For your internship evidence, run the scanner against your **approved practice/lab domain** and capture one clean terminal screenshot.

Recommended command:

```bash
python src/osint_scanner.py YOUR_APPROVED_DOMAIN --json output/osint_result.json --report output/osint_report.md
```

Your screenshot should show:
1. Sqrock Day 1 title
2. Target domain
3. DNS result
4. WHOIS result
5. IP geolocation result
6. "Scan complete"
7. JSON saved path
8. Report saved path

Do not expose credentials, private IP ranges, personal information, or unauthorized infrastructure.
