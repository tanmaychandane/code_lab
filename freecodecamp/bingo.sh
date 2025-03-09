#!/bin/bash
#Bingo Number Generator
echo -e "\n"~~ Bingo Number Generator ~~"\n"
NUMBER=$((RANDOM % 75 + 1 ))
echo $NUMBER
TEXT="The next number is, "
if (( NUMBER <= 15 ))
then
echo $TEXT B:$NUMBER
fi
