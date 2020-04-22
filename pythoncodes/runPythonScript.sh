echo "inside pscript"

#!/bin/bash

echo $1
inputFileName="$1"

date=`date +%m-%d-%Y`
outputFileName="${date}_Dataset.csv"

echo "input file name $inputFileName"
echo "output file name $outputFileName"

python3.6 pipelineProgramme.py $outputFileName $inputFileName
