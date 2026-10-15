#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 2 ]]; then
  echo "Usage: $0 CA_CERT SERVER_CERT" >&2
  exit 2
fi
ca="$1"
cert="$2"
openssl verify -CAfile "$ca" "$cert"
openssl x509 -in "$cert" -noout -subject -issuer -dates -ext subjectAltName
