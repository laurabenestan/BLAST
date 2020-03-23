# BLAST tutorial on RAD-seq datasets

Performing an efficient BLAST on RAD-sequencing and DarTseq datasets may sometimes be tricky, i.e. knowning which file contains the sequence and ID information for RAD-seq and Dartseq librairies.

## Installing BLAST search tool on your computer

To easily install NCBI BLAST tool, you can follow the nice tutorial done by (Eric Normendeau)[https://github.com/enormandeau/ncbi_blast_tutorial]

## RAD-sequencing libraries

### 1. Finding the files indicating the raw sequences (fasta) and the ID (name of the loci)

When you finish to run STACKs, you will end up having a file named **populations.loci.fa** by specifying the `--fasta_loci option`. 
This file contains the per-locus consensus FASTA output that you can easily use to perform BLAST alignment in NCBI. 

### 2. Extracting the ID that you found were outliers

You probably used one population-differntiated (PD) or Genotype-Environmental-association analysis (GEA) and you detected a list of putative outlier SNPs.
First you want to extract the  outlier SNPs sequences from the file **populations.loci.fa**.

To do so you can transform the fasta file in a text file format to then use a script `line.extract.py` that you can find in (Eric Normandeau github page)[https://github.com/enormandeau/Scripts].

When you have finished to extract the outlier sequences from the text file, you can then perform a BLAST on this subset of sequences.

### 3. Download sequences database

Forst you can download the NCBI database, which contains all the sequences avaimable worldwide, to do so run:
```{r, engine = 'bash', eval = FALSE}
update_blastdb.pl --decompress nr [*]
```

After downloading this database, you need to convert it in the right format by using the ``makeblastdb`` tool.
```{r, engine = 'bash', eval = FALSE}
makeblastdb -in reference.fasta -title reference -dbtype nucl -out databases/reference
```

You can do the same with the [SWISSPROT database](https://www.uniprot.org/uniprot/?query=reviewed:yes). The SWISSPROT database contains only the collection of functional information on proteins, with accurate, consistent and rich annotation. 

### 4. BLAST search on outlier sequences

You can now run the blast command using your dataset containing outlier SNPs sequences (sequences.fasta) on the NCBI database.
```{r, engine = 'bash', eval = FALSE}
blastn -db databases/reference -query sequences.fasta -evalue 1e-3 -word_size 11 -outfmt 0 > sequences.reference
```




