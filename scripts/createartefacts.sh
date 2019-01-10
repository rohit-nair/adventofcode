#!/bin/bash

usage="$(basename "$0") [-h|--help] [-d|--day=n]
Creates a day script file and a testinput and input file for the day argument passed.

where:
    -h|--help   Shows this help text
    -d|--day    Set the day value."

for i in "$@"
do
case $i in
    -d=*|--day=*)
    DAY="${i#*=}"

    ;;
    -h | --help)
    echo "$usage"
    exit

    ;;
   --default)
    DEFAULT=YES
    ;;
    *)

    ;;
esac
done

cd "${0%/*}"
echo "Path="$PWD "Day="$DAY

mkdir ../2018/python/day${DAY} && 
    cd ../2018/python/day${DAY} && 
    touch d${DAY}.py && 
    touch input${DAY}.txt && 
    touch testinput${DAY}.txt && 
    chmod +x d${DAY}.py