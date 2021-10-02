# tag-files

Script to search for files with tags and create tag folders sym-linked to the tagged files

Tags start with `#` and have one or more letters, numbers or `-`. Regex: `#[a-zA-Z0-9-]`

## Usage

`./tag-files.sh SRC DEST`

## Example

Create a Tags folder with symlinks to all tagged Documents.

`bash ./tag-files.sh ~/Documents ~/Tags`
