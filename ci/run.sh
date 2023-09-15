set -o errexit
cd $(dirname -- "$0")
cd ..

echo "[ai] Running SWI-Prolog..."
swipl -f src/main.pl <&1 EOF
