#!/usr/bin/env bash

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
help Remove remove
help Set set
help Sort sort
