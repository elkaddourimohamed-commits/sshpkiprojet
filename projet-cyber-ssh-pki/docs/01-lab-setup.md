# 01 — Lab setup

## Objectives
Create a repeatable, isolated environment for SSH administration and certificate exercises.

## Network
Use a hypervisor host-only network or an isolated cloud lab network. Record:
- Administrator VM hostname/IP:
- Server VM hostname/IP:
- DNS name used in the lab (example: `web.lab.test`):
- OS and version:
- Snapshot name before changes:

Use `192.0.2.0/24` only as documentation; it is reserved for examples and will not route on the public internet.

## Server prerequisites (Debian/Ubuntu)
On the disposable server VM:
```bash
sudo apt update
sudo apt install -y openssh-server openssl nginx python3
sudo systemctl enable --now ssh
sudo systemctl enable --now nginx
```

Check:
```bash
systemctl status ssh --no-pager
ss -lnt
ip -brief address
```

## Firewall
Allow SSH only from the administrator VM's lab IP where possible. Do not expose port 22 or the lab CA to the internet. If working in a cloud account, use the provider security group/network firewall to limit source addresses.

## Evidence to collect
- `ip -brief address`
- `ss -lnt`
- `systemctl is-active ssh nginx`
- screenshot or terminal output showing the VM network is isolated
