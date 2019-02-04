#!/bin/bash

OUTPUT=$(grep -R -i -n --include=\*.py "pdb.set_trace()" .)
if [ ! -z "$OUTPUT" ]; then
    echo $OUTPUT
    exit 1
fi

