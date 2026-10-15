# 03 — Private CA, CSR, signing and validation

## Concepts
- **Private key:** secret material; never share or commit it.
- **CSR:** Certificate Signing Request. It contains a public key and requested identity fields, and is signed by the requester.
- **CA:** Certificate Authority that validates and signs requests.
- **SAN:** Subject Alternative Name; modern clients use it to verify DNS/IP identities.
- **Chain validation:** verifies that the server certificate was signed by a trusted CA and is valid for the requested identity.

## Create a lab CA (on a dedicated CA VM or isolated admin machine)
Keep the CA private key offline if possible. This simplified lab command is for learning only:
```bash
mkdir -p pki/private pki/certs
chmod 700 pki/private
openssl genrsa -out pki/private/lab-ca.key 4096
chmod 600 pki/private/lab-ca.key
openssl req -x509 -new -key pki/private/lab-ca.key \
  -sha256 -days 365 -out pki/certs/lab-ca.crt \
  -subj "/O=Sysadmin Lab/CN=Sysadmin Lab Root CA"
```
For a production CA, use an audited CA solution, protected/offline root keys, a documented issuance policy, and proper revocation handling.

## Create server key and CSR
Run on the server or the server's secure build workstation:
```bash
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -out web.lab.test.key
chmod 600 web.lab.test.key
openssl req -new -key web.lab.test.key \
  -out web.lab.test.csr \
  -subj "/O=Sysadmin Lab/CN=web.lab.test" \
  -config pki/server-csr.cnf
```
The CSR config adds SAN `DNS:web.lab.test`. Review the CSR before signing:
```bash
openssl req -in web.lab.test.csr -noout -text
```

## Sign the CSR in the lab
Copy the CSR to the CA using a controlled channel; do not copy the server private key.
```bash
openssl x509 -req -in web.lab.test.csr \
  -CA pki/certs/lab-ca.crt -CAkey pki/private/lab-ca.key \
  -CAcreateserial -out web.lab.test.crt -days 90 -sha256 \
  -extfile pki/server-csr.cnf -extensions v3_server
```
In real environments, follow an approved identity verification and issuance process. Never sign arbitrary CSRs without checking ownership of the requested hostname.

## Validate certificate and identity
```bash
openssl verify -CAfile pki/certs/lab-ca.crt web.lab.test.crt
openssl x509 -in web.lab.test.crt -noout -subject -issuer -dates -ext subjectAltName
openssl req -in web.lab.test.csr -noout -verify
```
For a local HTTPS test, map `web.lab.test` to the lab server IP in the test machine's hosts file and trust the lab CA only on that test machine. Remove that trust after the exercise.

## Renewal and revocation exercise
Write down:
- Who owns the hostname?
- Who approves the CSR?
- What is the certificate expiration date?
- How is renewal requested before expiry?
- How would a compromised server key be handled?
- How would clients learn that a certificate is revoked?

This project intentionally does not claim to implement a complete production CRL/OCSP service.
