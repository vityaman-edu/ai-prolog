set -o errexit
cd $(dirname -- "$0")
cd ../..

echo "[ai] Running SWI-Prolog..."
swipl -f res/main.pl
