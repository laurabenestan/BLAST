## In the .csv file gave by DarT company, there is a list of sequences (3rd column) and their ID names (2nd column).
## create a fasta file with ID names as ID
DART_RAW="/media/superdisk/reservebenefit/donnees/dart/palinurus/infos/Report_DSpl19-4025_SNP_2.csv"
grep -v "*" $DART_RAW  | cut -d "," -f 2,3 | sort | uniq | awk '{ printf ">%s\n%s\n",$1,$2 }' | tr ',' '\n' | sed '/^$/d' > data/palinurus_variants_dart.fasta

