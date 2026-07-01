#!./pyenv/bin/python3

import shadowfax

PILEUP_GBS = 1

stream = shadowfax.PileupStream('HG002_chr22.bam', output_batch_size=PILEUP_GBS*1024*1024*1024)

for batch in stream:
    print(batch)
