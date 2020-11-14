#!/bin/bash

echo -n "colHeads,"
count=0
while [ $count -lt 592 ]; do
	echo -n "tumor,"
	count=$(($count + 1))
done
echo "tumor"
