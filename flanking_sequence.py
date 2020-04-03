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
#inputFastaFileGenome="genomes/sar_genome_lgt6000.fasta"
#inputTableFile="diplodus_coding.snps.bed"



## open fasta file
genome = pysam.FastaFile(inputFastaFileGenome)




## colomn are :
## scaffold, coordinates SNP L, coordinates SNP R, scaffold, soft, type, coordinates scaffold L, coordinates scaffold R, match, brand, ., annotations

## read table
with open(inputTableFile) as inputTable:
    csv_reader = csv.reader(inputTable, delimiter='\t')
    for row in csv_reader:
        scaffold=row[0]
        positionSNP=int(row[1])
        scaffoldPosLeft=int(row[6])
        scaffoldPosRight=int(row[7])
        positionLeft=positionSNP-1-NumberOfFlankingBases
        if positionLeft < 1:
            positionLeft=1
        positionRight=positionSNP-1+NumberOfFlankingBases
        flankingSeq = genome.fetch(scaffold, positionLeft,positionRight)
        rawAnnotations=row[-1]
        splitAnnotations=rawAnnotations.split(";")
        GO="NA"
        for i in splitAnnotations:
            if "GO:" in i:
                GO=i.split("=")[1]
                break;
        if GO != "NA":
            print("%s;%s;%s;%s" % (scaffold, positionSNP,GO,flankingSeq))