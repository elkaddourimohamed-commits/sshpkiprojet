from scripts.audit_ssh_config import read_config

def test_reads_explicit_settings(tmp_path):
    conf = tmp_path / "sshd_config"
    conf.write_text("PermitRootLogin no\nPasswordAuthentication yes\n# X11Forwarding yes\n")
    result = read_config(conf)
    assert result["permitrootlogin"] == "no"
    assert result["passwordauthentication"] == "yes"
    assert "x11forwarding" not in result
