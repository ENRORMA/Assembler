#!/bin/bash
SCRIPT_PATH=$(dirname "$(readlink -f "$0")")
if [ "$1" == "" ]; then
  python "$SCRIPT_PATH/Assemblers/TextAssembler.py"
else
  python "$SCRIPT_PATH/Assemblers/FileAssembler.py" $1
fi
