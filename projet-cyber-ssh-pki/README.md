# Secure Remote Administration Platform — SSH + PKI + Ansible

A lab project for a systems/network administration portfolio. It demonstrates:
- SSH key-based administration and safer SSH server settings.
- A small private Certificate Authority (CA) and certificate requests (CSR).
- Certificate signing and verification for a lab HTTPS service.
- Ansible automation with a preview-first workflow.
- OpenSSL validation, audit scripts, and incident-response documentation.

**Scope:** isolated VMs or localhost only. This is a learning lab, not a production-ready PKI.
Never reuse the lab CA, keys, passwords, or certificates in production.

## Architecture

```text
Admin workstation
  ├── SSH key pair ───────────────> Linux server VM
  ├── CSR request ────────────────> Lab Certificate Authority
  └── Ansible over SSH ───────────> Lab Linux server
                                      └── Nginx HTTPS using signed lab certificate
```

## Suggested lab

- 1 Linux VM for the server (Ubuntu Server or Debian).
- 1 Linux workstation/VM for the administrator (can be the same VM for a simplified demo).
- OpenSSH, OpenSSL, Python 3, Ansible and optionally Docker.
- Use a private host-only or NAT network. Do not expose SSH or the lab CA to the public internet.

## Project milestones

1. Build the lab and document IPs/hostnames.
2. Create an administrator SSH key and install its public key on the lab server.
3. Disable password authentication only after verifying key-based login in a second terminal.
4. Create a private lab CA and a certificate signing request (CSR).
5. Sign the CSR with the lab CA and validate the certificate chain and SAN.
6. Automate the web server setup with Ansible in check mode first.
7. Run the audit scripts and collect evidence.
8. Simulate a key/certificate incident and write a short incident report.

## Quick start

1. Read `docs/01-lab-setup.md`.
2. Copy `inventory.ini.example` to `inventory.ini` and replace the example address.
3. Review all commands in `docs/`.
4. Start with the scripts under `scripts/`; inspect them before executing.
5. For Ansible, always preview first:
   `ansible-playbook -i inventory.ini playbooks/site.yml --check --diff`

## Directory map

- `docs/` — detailed setup, operations, security and incident response.
- `scripts/` — audit and certificate helper scripts.
- `pki/` — sample OpenSSL configuration only; generated keys/certs should remain untracked.
- `playbooks/` — Ansible automation.
- `templates/` — SSH hardening example and Nginx TLS site config.
- `.github/workflows/` — basic syntax checks.

## Important safety notes

- The included `inventory.ini.example` uses documentation-only IP `192.0.2.20`. Replace it with your lab VM address.
- Do not commit `inventory.ini`, private keys, issued private material, `.env`, passwords, or real host data.
- The SSH configuration is a review template, not an automatic replacement for `/etc/ssh/sshd_config`.
- Certificate revocation and CRL distribution are described as a design exercise; this lab does not implement a production revocation service.
- Some commands require `sudo`; understand each command before running it.
