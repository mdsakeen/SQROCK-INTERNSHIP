# Sqrock Cybersecurity Internship — Day 1
## OSINT & Passive Reconnaissance

### Objective
Build a Python OSINT scanner that collects publicly available information about an authorized practice domain:
- WHOIS registration information
- DNS/IP resolution
- IP geolocation

This project follows the Day 1 requirement in the Sqrock Cybersecurity Internship Phase 1 document.

> **Scope:** Use only a practice domain, your own domain, or a domain for which you have explicit authorization. Do not use this tool against systems you are not authorized to assess.

### Project structure

```text
Day-01-OSINT/
├── README.md
├── requirements.txt
├── src/
│   └── osint_scanner.py
├── output/
│   ├── osint_result.json
│   └── osint_report.md
├── report/
│   └── Day-01-Report.md
└── screenshots/
    └── README.md
```

### Requirements

- Python 3.10+
- Internet connection for WHOIS/IP geolocation
- A domain you are authorized to assess

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

### Run

From this directory:

```bash
python src/osint_scanner.py example.com
```

For a real internship submission, replace `example.com` with your approved lab/practice domain.

Optional JSON output:

```bash
python src/osint_scanner.py example.com --json output/osint_result.json
```

Generate a Markdown report automatically:

```bash
python src/osint_scanner.py example.com --json output/osint_result.json --report output/osint_report.md
```

### What the tool collects

**Passive sources**
1. DNS resolution through the local resolver
2. WHOIS registration data through the `python-whois` library
3. IP geolocation through HTTPS providers (`ipwho.is`, with `ipapi.co` as a fallback)

The tool does not perform port scanning, vulnerability scanning, exploitation, login attempts, or direct interaction with the target application. If a geolocation provider returns an error such as HTTP 403, the scanner automatically tries the fallback provider and records provider/error details.

### Error handling

The scanner continues when an individual data source is unavailable. For example, WHOIS may be unavailable for a particular TLD or the geolocation API may be unreachable. The JSON output records the error rather than crashing the complete scan.

### Evidence for submission

Capture a terminal screenshot showing:

```text
[+] Target domain
[+] Resolved IP
[+] WHOIS status
[+] Geolocation status
[+] Output JSON path
[+] Report path
```

Do not include personal information, private domains, API keys, credentials, or sensitive internal infrastructure in screenshots.

### Suggested submission

Submit:
- `src/osint_scanner.py`
- `requirements.txt`
- `output/osint_result.json`
- `output/osint_report.md`
- screenshot of the terminal execution
- `report/Day-01-Report.md`

### Security/ethics

Sqrock's internship document states that all tasks must be performed only in authorized lab environments, that real targets must not be scanned/harvested, and that collected OSINT data must be anonymized or deleted after analysis.
