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
OUTLIERS="data/367outliers_pcadapt_mullus.tsv"
SPECIES="diplodus"
GFF3="/media/superdisk/reservebenefit/working/annotation/DSARv1_annotation.gff3"
### mullus
GENOME_FASTA="/media/superdisk/reservebenefit/donnees/genomes/mullus_genome_lgt6000.fasta"
OUTLIERS="data/476outliers_pcadapt_diplodus.tsv"
SPECIES="mullus"
GFF3="/media/superdisk/reservebenefit/working/annotation/MSURv1_annotation.gff3"
### serran
GENOME_FASTA="/media/superdisk/reservebenefit/donnees/genomes/serran_genome_lgt3000.fasta"
OUTLIERS="data/641outliers_pcadapt_serranus.tsv"
SPECIES="serran"
GFF3="/media/superdisk/reservebenefit/working/annotation/SCABv1_annotation.gff3"


## convert into bed
awk '{ print $1"\t"$2"\t"$2+1 }' $OUTLIERS > processing/selected_loci_"$SPECIES".bed
