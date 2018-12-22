#!/bin/bash

for i in "$@"
do
case $i in
    -d=*|--day=*)
    DAY="${i#*=}"

    ;;
   --default)
    DEFAULT=YES
    ;;
    *)

    ;;
esac
done

cd "${0%/*}"
echo $PWD

mkdir ../python/day${DAY} && cd ../python/day${DAY} && touch ${DAY}.py && touch input${DAY}.txt && touch testinput${DAY}.txt && chmod +x ${DAY}.py