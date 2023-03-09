#!/bin/bash
if [[ "$1" == "" ]] ; then
python Assemblers/TextAssembler.py
else
python Assemblers/FileAssembler.py $1
fi