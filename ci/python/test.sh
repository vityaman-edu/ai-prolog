set -o errexit
cd $(dirname -- "$0")
cd ../..

echo "[ai] Running Python Knowledge base..."
python src/test_parse.py
python src/test_terraria.py
