# Sqrock Cybersecurity Internship — Day 1 Report

## OSINT & Passive Reconnaissance

**Intern:** __________________________  
**Internship:** Sqrock IT Solution — Cybersecurity Internship Program  
**Program:** Alpha 2 — Cybersecurity Track  
**Day:** 1  
**Date:** __________________________  
**Authorized Practice Domain:** __________________________  

---

## 1. Objective

The objective of Day 1 is to understand passive information gathering and implement a Python OSINT scanner that collects WHOIS, DNS/IP, and IP geolocation information for an authorized practice domain.

## 2. Scope and Authorization

This assessment must be restricted to an authorized practice domain, a domain owned by the intern, or a target explicitly approved by the supervisor.

No active vulnerability scanning, port scanning, exploitation, authentication attempts, or unauthorized interaction is performed.

## 3. Tools Used

| Tool | Purpose |
|---|---|
| Python | Automation |
| `socket` | DNS/IP resolution |
| `python-whois` | WHOIS metadata |
| `requests` | Geolocation API request |
| ipwho.is / ipapi.co | Approximate IP geolocation |

## 4. Methodology

1. Accept the authorized domain as input.
2. Resolve the domain to IP address(es).
3. Query publicly available WHOIS registration information.
4. Query approximate geolocation information for resolved public IPs.
5. Save findings as JSON.
6. Generate a Markdown report.
7. Review findings from both attacker and defender perspectives.

## 5. Execution

Run:

```bash
python -m pip install -r requirements.txt
python src/osint_scanner.py example.com --json output/osint_result.json --report output/osint_report.md
```

Replace `example.com` with the approved lab/practice domain.

## 6. Results

Paste the generated `output/osint_report.md` content here or attach it as evidence after executing the scan.

### DNS/IP
- Resolved IP(s): __________________________
- DNS result: ______________________________

### WHOIS
- Registrar: _______________________________
- Creation date: ___________________________
- Expiration date: _________________________
- Name servers: ____________________________

### Geolocation
- IP: _____________________________________
- Approximate country/region/city: __________
- ISP/organization: _________________________

## 7. Attacker Perspective

Public DNS, WHOIS, and IP metadata can provide useful reconnaissance information. An attacker may correlate these data points with other public sources to understand an organization's external footprint.

The security significance is not necessarily in one individual data point, but in how multiple public sources can be combined.

## 8. Defender Perspective

Organizations should regularly review their public-facing information and remove unnecessary exposure. DNS records, public documentation, repositories, and registration information should be considered part of the external attack surface.

Recommended controls:
- Maintain an external asset inventory.
- Review DNS records periodically.
- Avoid unnecessary internal naming disclosure.
- Use WHOIS privacy where appropriate.
- Review public repositories for accidental information exposure.
- Include OSINT exposure in security awareness and threat modeling.

## 9. Limitations

- WHOIS fields differ by registrar/TLD.
- IP geolocation is approximate.
- DNS information can change.
- Passive OSINT does not establish whether a host is vulnerable.
- The results are valid only for the observation time.

## 10. Evidence Checklist

- [ ] Terminal screenshot showing successful execution
- [ ] JSON output
- [ ] Generated Markdown report
- [ ] No unauthorized target data
- [ ] Scope/authorization documented

## 11. Conclusion

The Day 1 exercise demonstrates a controlled passive reconnaissance workflow. The Python implementation automates DNS/IP resolution, WHOIS collection, and approximate IP geolocation while avoiding active probing. The results can be used to understand how publicly available information contributes to social-engineering reconnaissance and how defenders can reduce unnecessary exposure.
