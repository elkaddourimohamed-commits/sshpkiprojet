# 05 — Validation and portfolio evidence

Capture sanitized outputs (no private keys, tokens, public IPs or personal usernames):
- SSH public-key login succeeds.
- SSH audit output and `sshd -T` settings review.
- CSR details and CSR self-signature verification.
- Certificate subject, issuer, SAN and validity dates.
- `openssl verify` success for the lab server certificate.
- Ansible `--check --diff` output followed by a successful lab run.
- HTTPS response from the test endpoint.
- A brief before/after table and known limitations.

## Example acceptance criteria
- [ ] SSH key login works after opening a new terminal.
- [ ] No private key is stored in the Git repository.
- [ ] CSR contains the intended DNS SAN.
- [ ] Certificate validates against the lab CA.
- [ ] Certificate hostname matches `web.lab.test`.
- [ ] HTTPS endpoint responds in the lab.
- [ ] Ansible playbook is repeatable and has been reviewed.
- [ ] Recovery steps are documented.
