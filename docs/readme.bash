#!/usr/bin/env bash

function header {
    echo "$1"
    echo ""
    echo "\`\`\`"
    ./tag.py $2 --help
    echo "\`\`\`"
    echo ""
}

header "# tag-cli"
header "## Add" add
header "## Clear" clear
header "## Find" find
header "## Index" index
header "## List" list
header "## Remove" remove
header "## Rename" rename
header "## Set" set
header "## Sort" sort
