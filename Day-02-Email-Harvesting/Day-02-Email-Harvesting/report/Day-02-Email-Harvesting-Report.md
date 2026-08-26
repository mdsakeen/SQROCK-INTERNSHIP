# Day 02 Report

## Objective
Ethically extract email-shaped strings from an authorized lab webpage and explain their social-engineering relevance.

## Methodology
1. Served a synthetic HTML page locally.
2. Retrieved it with Python requests.
3. Used a regular expression to identify email patterns.
4. Removed duplicates and saved results as JSON.

## Attacker Perspective
Public email addresses can help build contact lists and support later social-engineering attempts.

## Defender Perspective
Minimize unnecessary public exposure, review websites and repositories, prefer role-based addresses where appropriate, and train users to verify unexpected requests.

## Limitations
Regex matching does not prove that an address is active and can produce false positives.

## Evidence
Attach script, JSON output, and terminal screenshot.
