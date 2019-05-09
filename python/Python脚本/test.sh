#!/bin/bash
repo list -p >path.txt
branch=$1
count=0
for path in `cat path.txt`
do
	count=$((count + 1))
	{
	pushd $path > /dev/null
		git branch -D $branch > /dev/null
		
	popd > /dev/null 
	}&
	echo $count
	if [ $count == 10 ]
	then
		count=0
		echo "$count start wait"
		wait
	fi
done
wait