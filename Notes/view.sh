#!/bin/bash
counter=0
for file in ~/CS-UY1114/Notes/*.txt; do
	days[$counter]=$file
	let counter=$counter+1
#	cat $file
done
counter=0
while [ $counter -lt ${#days[@]} ]; do
	echo $counter
	let counter=$counter+1
done
