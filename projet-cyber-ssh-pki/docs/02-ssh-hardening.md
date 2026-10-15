# 02 — SSH key-based administration and hardening

## Create a dedicated key on the administrator workstation
Use a passphrase. Do not send or commit the private key.
```bash
ssh-keygen -t ed25519 -a 64 -f ~/.ssh/lab_admin_ed25519
```

Install the public key:
```bash
ssh-copy-id -i ~/.ssh/lab_admin_ed25519.pub labadmin@SERVER_IP
```
If `ssh-copy-id` is unavailable, append the *public* `.pub` key to `~/.ssh/authorized_keys` on the server, ensuring correct ownership and permissions.

Test in a second terminal before changing server settings:
```bash
ssh -i ~/.ssh/lab_admin_ed25519 labadmin@SERVER_IP
```

## Review settings
Inspect `templates/sshd_config.lab.conf`. It is a reference, not a drop-in file. Before applying any SSH change:
1. Keep the current session open.
2. Validate configuration with `sudo sshd -t`.
3. Confirm console access or VM snapshot rollback.
4. Apply one change at a time.
5. Test a new SSH connection before closing the original session.

Never disable password authentication until public-key login has been proven. Keep a documented recovery path.

## Host key verification
On first connection, verify the host key fingerprint through a trusted channel. Do not blindly accept changed host keys. A changed key may be legitimate after a rebuild, but it must be investigated.

## Audit
Run:
```bash
python3 scripts/audit_ssh_config.py --config /etc/ssh/sshd_config
```
The script reports effective-looking values from explicit lines only; it does not evaluate all OpenSSH `Include`, `Match`, or default behavior. Use `sudo sshd -T` for effective configuration review.
