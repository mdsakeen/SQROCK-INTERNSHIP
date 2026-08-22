# Day 1 — OSINT & Passive Reconnaissance Report

## 1. Executive Summary

This exercise implemented a passive OSINT scanner for an authorized practice domain. The tool collected DNS/IP resolution data, publicly available WHOIS registration metadata, and IP geolocation metadata.

No port scanning, vulnerability scanning, exploitation, authentication attempts, or direct application testing was performed.

## 2. Scope

- **Target:** `example.com`
- **Authorization:** Practice/lab domain only
- **Timestamp (UTC):** `2026-08-22T09:16:53Z`
- **Assessment type:** Passive reconnaissance

## 3. Methodology

### DNS / IP Resolution
The Python `socket` library was used to resolve the domain through the configured DNS resolver.

### WHOIS
The `python-whois` library was used to request publicly available registration information.

### IP Geolocation
The resolved IP addresses were submitted to the public IP geolocation API used by the lab script. Geolocation is approximate and should not be treated as a physical address.

## 4. Findings

### DNS
- Status: **SUCCESS**
- Resolved IPs: `104.20.23.154, 172.66.147.243`
- Error: `None`

### WHOIS
- Status: **SUCCESS**
- Registrar: `RESERVED-Internet Assigned Numbers Authority`
- Creation date: `1995-08-14T04:00:00+00:00`
- Expiration date: `2027-08-13T04:00:00+00:00`
- Updated date: `2026-08-14T08:01:43+00:00`
- Name servers: `elliott.ns.cloudflare.com, hera.ns.cloudflare.com`
- Error: `None`

### IP Geolocation
- **104.20.23.154** — San Francisco, California, United States; ISP: Cloudflare, Inc.; Organization: Cloudflare, Inc.
- **172.66.147.243** — San Francisco, California, United States; ISP: Cloudflare, Inc.; Organization: Cloudflare, Inc.

## 5. Attacker Perspective

An attacker can use public DNS, registration, and IP metadata as initial reconnaissance to understand an organization's internet-facing footprint. This information can help identify naming conventions, hosting providers, geographic regions, and infrastructure relationships.

The important security lesson is that passive information can become useful when combined with other publicly available information.

## 6. Defender Perspective

Defenders should understand what information their organization exposes publicly and minimize unnecessary disclosure. Recommended controls include:

1. Keep WHOIS registration privacy options enabled where appropriate and legally available.
2. Review DNS records periodically for unnecessary exposure.
3. Avoid publishing internal hostnames, IP addresses, or sensitive infrastructure details.
4. Monitor public repositories and documentation for accidental information disclosure.
5. Maintain an inventory of internet-facing assets.
6. Treat public IP and DNS information as reconnaissance data and incorporate it into threat modeling.

## 7. Limitations

- WHOIS availability and returned fields vary by registrar and TLD.
- IP geolocation is approximate.
- DNS results can change over time.
- The scanner does not determine whether a discovered service is vulnerable.
- Results represent a point-in-time observation.

## 8. Conclusion

The Day 1 objective was achieved by implementing a passive OSINT workflow that collects DNS/IP, WHOIS, and IP geolocation information while avoiding active probing. The exercise demonstrates how publicly available information can contribute to an attacker's reconnaissance process and why defenders should continuously review their external information footprint.

## 9. Evidence

Attach a terminal screenshot showing the completed scan and generated JSON/report files.

**Do not include credentials, private information, or unauthorized target data in the submitted evidence.**
