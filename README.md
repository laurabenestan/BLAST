# BLAST tutorial on RAD-seq datasets

Performing an efficient BLAST on RAD-sequencing and DarTseq datasets may sometimes be tricky, i.e. knowning which file contauins the sequence and ID information for RAD-seq and Dartseq librairies.

## Installing BLAST search tool on your computer

To easily install NCBI BLAST tool, you can follow the nice tutorial done by (Eric Normendeau)[https://github.com/enormandeau/ncbi_blast_tutorial]

## RAD-sequencing libraries

### 1. Finding where is the information of the sequences

When you finish to run STACKs, you will end up having a file named populations.loci.fa by specifying the `--fasta_loci option`. 
This file contains the per-locus consensus FASTA output that you can easily use to perform BLAST alignment in NCBI. 

