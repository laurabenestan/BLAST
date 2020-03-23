# BLAST tutorial to define candidate genes 

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

## DarTseq libraries

DartSeq is a genotyping-by-sequencing system that sequence the most informative representations of genomic DNA samples to help marker discovery. 

### 1. Change the ID name in the vcf file

Create a file saving the beginning of the ID number, i.e. remove the "|F|...." from the ID names.
```{r, engine = 'bash', eval = FALSE}
grep -v -E "#" 64057snps_468ind.recode.vcf | cut -f 3 | sed 's/|.*//g' > id_easy_serran.txt
```

Remove the beginning, i.e. "#" of the vcf file
```{r, engine = 'bash', eval = FALSE}
grev -v -E "#" 64057snps_468ind.recode.vcf > test.vcf
```

Copy the ID names saved in the file id_easy_serran.txt in the new vcf file.
```{r, engine = 'bash', eval = FALSE}
awk 'NR==FNR{a[NR]=$0;next} {$3=a[FNR]}1' OFS="\t" id_easy_serran.txt test.vcf > test2.vcf
```

To have a vcf file that works, you can simply copy paste the beginning of your previous vcf file in h terminal by typing
```{r, engine = 'bash', eval = FALSE}
nano test2.vcf
```

### 2. Find the informations containing the sequences and the name of each sequence in the file sent by the DarT company

In the .csv file gave by DarT company, there is a list of sequences (3rd column) and their ID names (2nd column). 
```{r, engine = 'bash', eval = FALSE}
grep -v "*" Report_DSpl19-4025_SNP_2.csv | cut -d "," -f 2,3 | sort | uniq > sequences_palinurus.txt
```

### 3. Extract the outlier SNPs in this file containing sequences

Use the `line_extract.py` python script to extract only the outlier sequences you are interesting in.

