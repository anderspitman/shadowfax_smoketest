#!./pyenv/bin/python3

import shadowfax

stream = shadowfax.PileupStream('HG002_chr22.bam')

for batch in stream:
    print(batch)
