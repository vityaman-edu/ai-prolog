set -o errexit
cd $(dirname -- "$0")
cd ../..

echo "[ai] Running Python Knowledge base..."
python src/main.py res # echo < res/input.txt
