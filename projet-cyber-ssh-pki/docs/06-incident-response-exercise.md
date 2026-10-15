# 06 — Incident response tabletop

## Scenario
A team member reports that the private SSH key for a lab administrator may have been copied. A second alert indicates that the TLS certificate for `web.lab.test` is approaching expiry.

## Tasks
1. Record the timeline, affected hosts, and available evidence.
2. Restrict access to the lab server while preserving logs.
3. Remove the compromised public key from `authorized_keys`; verify another trusted access path first.
4. Create a new administrator key and validate access.
5. For the TLS certificate, verify the hostname owner, create a new CSR, review it, and sign only after approval.
6. If the certificate private key is compromised, plan replacement and document the limitations of revocation in this lab.
7. Rotate related credentials if there is evidence they were exposed.
8. Write a post-incident report: impact, root cause, actions, residual risk, and prevention.

Do not test this scenario on systems you do not own or administer.
