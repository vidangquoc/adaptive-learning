#!/usr/bin/env bash
set -euo pipefail

URL='https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-phrase-list/Oxford%20Phrase%20List.pdf'
OUT_DIR="$(cd "$(dirname "$0")" && pwd)/raw"
OUT_FILE="$OUT_DIR/Oxford-Phrase-List.pdf"
MANIFEST="$OUT_DIR/MANIFEST.txt"

mkdir -p "$OUT_DIR"

curl -L --fail --retry 3 "$URL" -o "$OUT_FILE"

SHA256="$(sha256sum "$OUT_FILE" | awk '{print $1}')"
SIZE="$(wc -c < "$OUT_FILE" | tr -d ' ')"
DATE="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

cat > "$MANIFEST" <<EOF
source=Oxford Phrase List
url=$URL
retrieved_at=$DATE
sha256=$SHA256
bytes=$SIZE
EOF

echo "Saved: $OUT_FILE"
echo "SHA256: $SHA256"
