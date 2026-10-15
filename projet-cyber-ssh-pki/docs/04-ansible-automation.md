# 04 — Automate with Ansible

## Prerequisites
Install Ansible on the control machine and ensure SSH key login works first. Replace `192.0.2.20` in your local, untracked `inventory.ini`.

## Preview
```bash
ansible -i inventory.ini lab -m ping
ansible-playbook -i inventory.ini playbooks/site.yml --check --diff
```

Review the planned changes. Only then apply to the disposable VM:
```bash
ansible-playbook -i inventory.ini playbooks/site.yml
```

The playbook installs Nginx on Debian-family hosts and deploys a basic TLS site configuration only when certificate/key files are supplied on the target host. It does not generate or distribute private keys. You must transfer certificate material securely and set restrictive permissions.
