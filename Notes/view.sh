#!/bin/bash
counter=0
for file in ~/CS-UY1114/Notes/*.txt; do
#	days[$counter]=$file
#	let counter=$counter+1
	cat $file
done
#for i in ${#days[@]}; do
#	echo ${days[i]}
#done
