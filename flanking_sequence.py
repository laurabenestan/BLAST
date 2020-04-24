#================================================================================
#AUTHORS
#================================================================================
'''
GUERIN Pierre-Edouard
France, Montpellier
EPHE, CNRS, CEFE
01/2020
'''
#================================================================================
#NOTICE
#================================================================================

'''
Extract SNPs flanking sequences based on coordinates
'''

#================================================================================
#MODULES
#================================================================================

import re
import sys
import subprocess
import argparse
import os.path
import random
import pysam
import csv

#================================================================================
#CLASS
#================================================================================


#================================================================================
#FUNCTIONS
#================================================================================


#================================================================================
#ARGUMENTS
#================================================================================

parser = argparse.ArgumentParser(description='flanking seq')
parser.add_argument("-o","--output", type=str)
parser.add_argument("-g","--inGenomeFasta",type=str)
parser.add_argument("-t","--inTableFile",type=str)
parser.add_argument("-f","--NumberOfFlankingBases",type=int)

#================================================================================
#MAIN
#================================================================================
args = parser.parse_args()
resultsPath = args.output
inputFastaFileGenome = args.inGenomeFasta
inputTableFile=args.inTableFile
NumberOfFlankingBases=args.NumberOfFlankingBases


#NumberOfFlankingBases=42
#inputFastaFileGenome="/media/superdisk/reservebenefit/donnees/genomes/sar_genome_lgt6000.fasta"
#inputTableFile="processing/diplodus_coding.snps.bed"

inputGff3="/media/superdisk/reservebenefit/working/annotation/DSARv1_annotation.gff3"


## read gff3 and get GO and parents ID as dictionary
goDic = {}
gff_reader = csv.reader(open(inputGff3), delimiter='\t')
for row in gff_reader:
    annot=row[-1]
    if "Ontology_term" in annot:
        for an in annot.split(";"):
            if "Parent" in an:
                parent=an.split('=')[1]
            elif "Ontology" in an:
                go=an.split('=')[1]
                if ',' in go:
                    go=go.split(',')[0]
            else:
                pass
            #print("%s;%s" % (parent, go))
            goDic[parent]=go



## open fasta file
genome = pysam.FastaFile(inputFastaFileGenome)



## colomn are :
## scaffold, coordinates SNP L, coordinates SNP R, scaffold, soft, type, coordinates scaffold L, coordinates scaffold R, match, brand, ., annotations

## read table
csv_reader = csv.reader(open(inputTableFile), delimiter='\t')
for row in csv_reader:
    parent=row[-1].split(';')[1]
    if "Parent" in parent:
        parentId = parent.split('=')[1]
        go = goDic.get(parentId,"NA")
    else:
        go = "NA"
    scaffold=row[0]
    positionSNP=int(row[1])
    scaffoldPosLeft=int(row[6])
    scaffoldPosRight=int(row[7])
    typeSeq = row[5]  
    sequences = genome.fetch(scaffold, scaffoldPosLeft,scaffoldPosRight)
    print("%s;%s;%s;%s;%s" % (scaffold, positionSNP, typeSeq, sequences,go))