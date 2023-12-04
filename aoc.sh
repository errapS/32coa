#!/bin/bash

for i in {2..24}; do
	if [ $i -lt 10 ]; then
		folder_name="0$i"
	else	
		folder_name="$i"
	fi
	file_name="aoc_$folder_name.py"
	mkdir "$folder_name"
	touch "$folder_name/$file_name"
done
