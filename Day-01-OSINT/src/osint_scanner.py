#!/usr/bin/env python3
"""
Sqrock Cybersecurity Internship - Day 1
OSINT & Passive Reconnaissance

Authorized lab / practice domains only.

Collects:
- DNS/IP resolution
- WHOIS information
- IP geolocation

Does NOT perform:
- port scanning
- vulnerability scanning
- exploitation
- authentication attempts
"""

from __future__ import annotations

import argparse
import json
import socket
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any

import requests
import whois


USER_AGENT = "Sqrock-Day1-OSINT-Lab/1.0"
GEO_API = "https://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,lat,lon,isp,org,as,query"


def json_safe(value: Any) -> Any:
    """Convert WHOIS/date/set/other values into JSON-safe objects."""
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, (list, tuple, set)):
        return [json_safe(v) for v in value]
    if isinstance(value, dict):
        return {str(k): json_safe(v) for k, v in value.items()}
    return value


def resolve_dns(domain: str) -> dict[str, Any]:
    """Resolve the domain using the system DNS resolver."""
    result: dict[str, Any] = {
        "status": "error",
        "hostname": domain,
        "ip_addresses": [],
        "canonical_name": None,
        "error": None,
    }

    try:
        _, aliases, addresses = socket.gethostbyname_ex(domain)
        result["status"] = "success"
        result["ip_addresses"] = sorted(set(addresses))
        result["aliases"] = aliases
        try:
            result["canonical_name"] = socket.getfqdn(domain)
        except socket.error:
            pass
    except socket.gaierror as exc:
        result["error"] = f"DNS resolution failed: {exc}"

    return result


def lookup_whois(domain: str) -> dict[str, Any]:
    """Retrieve publicly available WHOIS registration data."""
    result: dict[str, Any] = {
        "status": "error",
        "registrar": None,
        "creation_date": None,
        "expiration_date": None,
        "updated_date": None,
        "name_servers": [],
        "status_codes": [],
        "error": None,
    }

    try:
        data = whois.whois(domain)

        def first(value: Any) -> Any:
            if isinstance(value, (list, tuple)):
                return value[0] if value else None
            return value

        result["status"] = "success"
        result["registrar"] = first(data.registrar)
        result["creation_date"] = json_safe(first(data.creation_date))
        result["expiration_date"] = json_safe(first(data.expiration_date))
        result["updated_date"] = json_safe(first(data.updated_date))
        result["name_servers"] = sorted(
            {str(x).lower() for x in (data.name_servers or [])}
        )
        result["status_codes"] = sorted(
            {str(x) for x in (data.status or [])}
        )
    except Exception as exc:  # library can raise different exceptions by TLD
        result["error"] = f"WHOIS lookup failed: {exc}"

    return result


def geolocate_ip(ip: str) -> dict[str, Any]:
    """Query IP geolocation using HTTPS providers with safe fallbacks.

    Primary provider: ipwho.is
    Fallback provider: ipapi.co

    If all providers fail, the result records the failure rather than
    fabricating location data.
    """
    result: dict[str, Any] = {
        "status": "error",
        "ip": ip,
        "country": None,
        "region": None,
        "city": None,
        "latitude": None,
        "longitude": None,
        "isp": None,
        "organization": None,
        "asn": None,
        "provider": None,
        "error": None,
    }

    providers = [
        (
            "ipwho.is",
            f"https://ipwho.is/{ip}",
            lambda data: {
                "country": data.get("country"),
                "region": data.get("region"),
                "city": data.get("city"),
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude"),
                "isp": (data.get("connection") or {}).get("isp"),
                "organization": (data.get("connection") or {}).get("org"),
                "asn": (data.get("connection") or {}).get("asn"),
            },
        ),
        (
            "ipapi.co",
            f"https://ipapi.co/{ip}/json/",
            lambda data: {
                "country": data.get("country_name"),
                "region": data.get("region"),
                "city": data.get("city"),
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude"),
                "isp": data.get("org"),
                "organization": data.get("org"),
                "asn": data.get("asn"),
            },
        ),
    ]

    errors = []

    for provider, url, parser in providers:
        try:
            response = requests.get(
                url,
                headers={
                    "User-Agent": USER_AGENT,
                    "Accept": "application/json",
                },
                timeout=10,
            )
            response.raise_for_status()
            data = response.json()

            if provider == "ipwho.is" and data.get("success") is False:
                raise RuntimeError(data.get("message", "Provider returned failure"))

            if provider == "ipapi.co" and data.get("error"):
                raise RuntimeError(data.get("reason", "Provider returned failure"))

            result.update(parser(data))
            result["status"] = "success"
            result["provider"] = provider
            return result

        except (requests.RequestException, ValueError, RuntimeError) as exc:
            errors.append(f"{provider}: {exc}")

    result["error"] = " | ".join(errors)
    return result


def run_scan(domain: str) -> dict[str, Any]:
    """Run the complete passive OSINT workflow."""
    domain = domain.strip().lower()

    scan: dict[str, Any] = {
        "project": "Sqrock Cybersecurity Internship - Day 1",
        "task": "OSINT & Passive Reconnaissance",
        "scope_note": "Authorized practice/lab domain only",
        "scan_timestamp_utc": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "target": {
            "domain": domain,
        },
        "dns": {},
        "whois": {},
        "geolocation": [],
    }

    print("=" * 68)
    print("SQROCK CYBERSECURITY INTERNSHIP - DAY 1")
    print("OSINT & PASSIVE RECONNAISSANCE")
    print("=" * 68)
    print(f"[+] Target domain : {domain}")
    print("[+] Scope         : Passive / authorized practice use only\n")

    print("[*] Resolving DNS...")
    scan["dns"] = resolve_dns(domain)

    if scan["dns"]["status"] == "success":
        print(f"[+] DNS status    : SUCCESS")
        print(f"[+] IP addresses  : {', '.join(scan['dns']['ip_addresses'])}")
    else:
        print(f"[!] DNS status    : ERROR - {scan['dns']['error']}")

    print("\n[*] Querying WHOIS...")
    scan["whois"] = lookup_whois(domain)

    if scan["whois"]["status"] == "success":
        print("[+] WHOIS status  : SUCCESS")
        print(f"[+] Registrar     : {scan['whois']['registrar'] or 'Not disclosed'}")
    else:
        print(f"[!] WHOIS status  : ERROR - {scan['whois']['error']}")

    print("\n[*] Querying IP geolocation...")
    for ip in scan["dns"].get("ip_addresses", []):
        geo = geolocate_ip(ip)
        scan["geolocation"].append(geo)

        if geo["status"] == "success":
            print(
                f"[+] {ip} -> "
                f"{geo['city'] or 'N/A'}, {geo['region'] or 'N/A'}, "
                f"{geo['country'] or 'N/A'}"
            )
        else:
            print(f"[!] {ip} -> ERROR - {geo['error']}")

    print("\n[+] Scan complete.")
    return scan


def write_json(data: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(json_safe(data), indent=2),
        encoding="utf-8",
    )


def write_report(data: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    dns = data["dns"]
    whois_data = data["whois"]
    geos = data["geolocation"]

    geo_lines = []
    for geo in geos:
        if geo["status"] == "success":
            geo_lines.append(
                f"- **{geo['ip']}** — {geo['city'] or 'N/A'}, "
                f"{geo['region'] or 'N/A'}, {geo['country'] or 'N/A'}; "
                f"ISP: {geo['isp'] or 'N/A'}; "
                f"Organization: {geo['organization'] or 'N/A'}"
            )
        else:
            geo_lines.append(f"- **{geo['ip']}** — lookup failed: {geo['error']}")

    report = f"""# Day 1 — OSINT & Passive Reconnaissance Report

## 1. Executive Summary

This exercise implemented a passive OSINT scanner for an authorized practice domain. The tool collected DNS/IP resolution data, publicly available WHOIS registration metadata, and IP geolocation metadata.

No port scanning, vulnerability scanning, exploitation, authentication attempts, or direct application testing was performed.

## 2. Scope

- **Target:** `{data['target']['domain']}`
- **Authorization:** Practice/lab domain only
- **Timestamp (UTC):** `{data['scan_timestamp_utc']}`
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
- Status: **{dns.get('status', 'unknown').upper()}**
- Resolved IPs: `{', '.join(dns.get('ip_addresses', [])) or 'None'}`
- Error: `{dns.get('error') or 'None'}`

### WHOIS
- Status: **{whois_data.get('status', 'unknown').upper()}**
- Registrar: `{whois_data.get('registrar') or 'Not disclosed'}`
- Creation date: `{whois_data.get('creation_date') or 'Not disclosed'}`
- Expiration date: `{whois_data.get('expiration_date') or 'Not disclosed'}`
- Updated date: `{whois_data.get('updated_date') or 'Not disclosed'}`
- Name servers: `{', '.join(whois_data.get('name_servers', [])) or 'Not disclosed'}`
- Error: `{whois_data.get('error') or 'None'}`

### IP Geolocation
{chr(10).join(geo_lines) if geo_lines else '- No IP addresses were available for geolocation.'}

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
"""

    path.write_text(report, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Passive OSINT scanner for authorized practice domains."
    )
    parser.add_argument("domain", help="Authorized practice/lab domain")
    parser.add_argument(
        "--json",
        default="output/osint_result.json",
        help="JSON output path",
    )
    parser.add_argument(
        "--report",
        default="output/osint_report.md",
        help="Markdown report output path",
    )
    args = parser.parse_args()

    if any(ch in args.domain for ch in "/\\ @"):
        print("[!] Invalid domain format.")
        return 2

    data = run_scan(args.domain)
    write_json(data, Path(args.json))
    write_report(data, Path(args.report))

    print(f"[+] JSON saved    : {args.json}")
    print(f"[+] Report saved  : {args.report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
