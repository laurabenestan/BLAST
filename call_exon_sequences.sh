###############################################################################
## from a list of genome location
## it return a list of sequences 


###############################################################################
###############################################################################
## load an environment with bedtools vcftools available
SINGULARITY_SIMG="/media/superdisk/utils/conteneurs/snpsdata_analysis.simg"
singularity shell --bind /media/superdisk:/media/superdisk $SINGULARITY_SIMG


###############################################################################
## global variables
### diplodus
GENOME_FASTA="/media/superdisk/reservebenefit/donnees/genomes/sar_genome_lgt6000.fasta"
#OUTLIERS="476outliers_pcadapt_diplodus.tsv"
#OUTLIERS="193rdaoutliers_diplodus.tsv"
OUTLIERS="47588allsnps_diplodus.tsv"
SPECIES="diplodus"
GFF3="/media/superdisk/reservebenefit/working/annotation/DSARv1_annotation.gff3"
### mullus
GENOME_FASTA="/media/superdisk/reservebenefit/donnees/genomes/mullus_genome_lgt6000.fasta"
OUTLIERS="367outliers_pcadapt_mullus.tsv"
OUTLIERS="199rdaoutliers_mullus.tsv"
OUTLIERS="36613allsnps_mullus.tsv"
SPECIES="mullus"
GFF3="/media/superdisk/reservebenefit/working/annotation/MSURv1_annotation.gff3"
### serran
GENOME_FASTA="/media/superdisk/reservebenefit/donnees/genomes/serran_genome_lgt3000.fasta"
OUTLIERS="641outliers_pcadapt_serranus.tsv"
OUTLIERS="311rdaoutliers_serranus.tsv"
OUTLIERS="64057allsnps_serranus.tsv"
SPECIES="serran"
GFF3="/media/superdisk/reservebenefit/working/annotation/SCABv1_annotation.gff3"


## select exon only
EXOME="exome/"$SPECIES"_exon.gff3"
awk '{ if($3 =="exon") { print $0 } }' $GFF3 > $EXOME
## convert into bed
OUTBED=processing/"${OUTLIERS/.tsv/_selected_loci.bed}"
awk '{ print $1"\t"$2"\t"$2+1 }' data/$OUTLIERS > $OUTBED
## get coding region for SNPs
CODINGBED=processing/"${OUTLIERS/.tsv/_coding.snps.bed}"
bedtools intersect -wb -a $OUTBED -b $EXOME > $CODINGBED
## format annotation table (get genome sequences with 99*2 flanking region)
SNPSCSV=sequences/"${OUTLIERS/.tsv/.snps.csv}"
python3 flanking_sequence.py -g $GENOME_FASTA -t $CODINGBED -f 99 > $SNPSCSV