#!/bin/bash

usage="$(basename "$0") [-h|--help] [-d|--day=n] [-y|--year=n]
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
    -y=*|--year=*)
    YEAR="${i#*=}"

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

mkdir -p ../${YEAR}/python/day${DAY} && 
    cd ../${YEAR}/python/day${DAY} && 
    touch d${DAY}.py && 
    touch input${DAY}.txt && 
    touch testinput${DAY}.txt && 
    chmod +x d${DAY}.py