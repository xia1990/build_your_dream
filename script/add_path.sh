#!/bin/bash

XML="test.xml"

readarray -t xml_array < $XML
for line in "${xml_array[@]}"
do
	echo $line | grep -aoe "project"
	if [ "$?" == 0 ];then
		if [ "$?" == 0 ];then
			name_line=$(echo $line | grep -aoe "name=[a-zA-Z0-9\"\"\._]*" | awk -F'"|"' '{print $2}')
			echo $line | grep -v "path" | sed -n "s/name=[a-zA-Z0-9\"\"\._]*/& path=\"$name_line\"/g"p | tee -a local.xml
		fi
	else
		echo $line | tee -a local.xml
	fi
done	
