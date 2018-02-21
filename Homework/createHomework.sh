#!/bin/bash
hnum=$1
qnum=$2
counter=1
mkdir "hw"$hnum
cd "hw"$hnum
while [ $counter -le $qnum ]; do
	touch "bl2448_hw"$hnum"_q"$counter".py"
	sudo chmod 755 "bl2448_hw"$hnum"_q"$counter".py"
	let counter=$counter+1
done
