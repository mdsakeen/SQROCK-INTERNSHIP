# Day 07 Report

## Objective
Understand brute-force/credential-stuffing concepts and demonstrate why rate limiting and account controls matter.

## Lab
A localhost-only Flask login service was used. The simulator sent a small fixed set of synthetic passwords.

## Defense
The server rate-limits repeated attempts and returns HTTP 429 after the configured threshold.

## Additional Controls
MFA, lockout, CAPTCHA, credential-breach monitoring, and strong password policy.
