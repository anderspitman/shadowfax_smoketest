curl -LOR https://github.com/anderspitman/shadowfax_smoketest/releases/latest/download/HG002_chr22.bam
curl -LOR https://github.com/anderspitman/shadowfax_smoketest/releases/latest/download/HG002_chr22.bam.bai

python3 -m venv pyenv
source pyenv/bin/activate
pip install shadowfax
