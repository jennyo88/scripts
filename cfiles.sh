#!/bin/bash
# -----------------------------------------------------------------
# File name:            Convert Files
# Program description:  Prompt user for directory list
#                       with the long listing option.
# Author:               Jennifer Romero
# Usage:                cfiles
# -----------------------------------------------------------------
#
# -----check whether user had supplied -h or --help. If yes display usage
if [[ ( $@ == "--help") || $@ == "-h" ]]
then
  echo "Usage: $(basename $0) [arguments]"
  exit 0
fi

## Prompted commands

echo ' --------------------------------------------------- '
echo " -------------- Converting Files Script ------------ "
echo ' --------------------------------------------------- '
echo ' '
echo ' '
echo ' '

printf "Original file extension? "
read srcExt

printf "New file extension? "
read destExt

printf "Original file directory? "
read srcDir

printf "New file directory? "
read destDir

### Script

for filename in "$srcDir"/*.$srcExt;
do

	basePath=${filename%.*}
	baseName=${basePath##*/}

	ffmpeg -i $filename -c:v libx265 -c:a copy -threads 3 $opts "$destDir"/"$baseName"."$destExt"

done

echo "Conversion from ${srcExt} to ${destExt} complete!"
