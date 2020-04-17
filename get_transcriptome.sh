## download Muscle of Spiny lobster transcriptome
## https://www.ncbi.nlm.nih.gov/sra/SRX6760688[accn]

wget -O transcriptomes/muscle_lobster.sra  https://sra-download.ncbi.nlm.nih.gov/traces/sra9/SRR/009788/SRR10023610

## load an environment with sra toolkit
SINIMG="singularity exec --bind /media/superdisk:/media/superdisk snpsdata_analysis.simg"

nohup $SINIMG fastq-dump -I --split-files transcriptomes/muscle_lobster.sra &