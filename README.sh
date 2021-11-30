#!/usr/bin/env bash

# ./README.sh > README.md

function help {
    echo ""
    echo "## $1"
    echo ""
    echo "\`\`\`"
    ./tag $2 --help
    echo "\`\`\`"
}

echo "# tag-cli"
echo ""
echo "\`\`\`"
./tag --help
echo "\`\`\`"

help Add add
help Clear clear
help Find find
help Index index
help List list
help Remove remove
help Rename rename
help Set set
help Sort sort
