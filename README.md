# Tag

A command line interface to manage file name tags.

## Installation

### Install from PyPI

```
pip install hew-tag
tag --version
```

### Install from source

```
git clone https://github.com/hewlock/tag.git
cd tag
make init
pip install -e .
tag --version
```

### Run from source

```
git clone https://github.com/hewlock/tag.git
cd tag
make init
python -m tag --version
```

## Description

There is nothing special about file tags. They are just text inside the
filename. You can add or remove them any way you would normally rename a
file. This tool just makes it a little easier to do things in bulk.

I have arbitrarily chosen to start tags with an open curly `{` and
close tags with a close curly `}`. I thought this was easier to read than some
other options (including the popular web "hash tag" format).

The main feature of `tag` is to index files by tag. For example, if you keep
all files for the same year in the same folder, it can be a little challenging
to find related files (taxes, car maintenance, etc.). `tag index` creates a
directory tree of tags with smylinks to all the tagged documents. This makes it
easy to find all files tagged with `taxes-2020` when tax time comes around.

For example:

```
~/Documents/
├── 2020/
│   ├── 2020-09-01 Car Service {toyota-yaris}.pdf
│   ├── 2020-10-01 Charitable Receipt {taxes-2020}.pdf
│   └── ...
└── 2021/
    ├── 2021-01-15 Work W-2 {taxes-2020}.pdf
    ├── 2021-03-01 Car Service {toyota-yaris}.pdf
    └── ...
```

Running:
`tag index ~/Documents ~/Tags`

Will produce symlinks like:

```
~/Tags/
├── taxes-2020/
│   ├── 2020-10-01 Charitable Receipt {taxes-2020}.pdf -> ~/Documents/2020/2020-10-01 Charitable Receipt {taxes-2020}.pdf
│   └── 2021-01-15 Work W-2 {taxes-2020}.pdf -> ~/Documents/2021/2021-01-15 Work W-2 {taxes-2020}.pdf
└── toyota-yaris/
    ├── 2020-09-01 Car Service {toyota-yaris}.pdf -> ~Documents/2020/2020-09-01 Car Service {toyota-yaris}.pdf
    └── 2021-03-01 Car Service {toyota-yaris}.pdf -> ~Documents/2021/2021-09-01 Car Service {toyota-yaris}.pdf
```

## Cookbook

### Rename all tags in a directory recursively

Suppose I name my Toyota Yaris "Harold" and want to rename all my tags. I can
use `tag find` to list all uses of the `toyota-yaris` tag and then use
`tag rename` with `xargs` to rename the tag to `harold`. Using the `-0` arg for
both `tag find` and `xargs` assures any whitespace in file names won't affect the command.

```
tag find -r0 toyota-yaris ~/Documents | xargs -0 tag rename toyota-yaris harold
```

## Usage

### Synopsis

```
Usage: tag [OPTIONS] COMMAND [ARGS]...

  tag - manage file name tags

  File tags:
    - are in the file name matching: {[a-zA-Z0-9-]+}
    - start with '{' and end with '}'
    - consist of letters, numbers and the '-' character

  Examples:
    - myfile{my-tag-1}{my-tag-2}.txt
    - My Title Case File {My-Tag-1}{My-Tag-2}.txt

Options:
  --version  Show version information.
  --help     Show this message and exit.

Commands:
  add      Add tags to files.
  clear    Clear tags from files.
  find     Find files by tag.
  index    Index tagged files.
  list     List tags on files.
  remove   Remove tags from files.
  rename   Rename a tag on files.
  set      Set tags on files.
  sort     Sort tags on files.
  version  Show version information.
```

### Add

```
Usage: tag add [OPTIONS] TAGS [FILES]...

  Add tags to files.

  TAGS  comma seperated list of tags
  FILES list of files

  Examples:
    - tag add my-tag myfile.txt
    - tag add my-tag-1,my-tag-2 *.txt

Options:
  -v, --verbose  Show additional output.
  -d, --debug    Make no changes to the file system.
  --help         Show this message and exit.
```

### Clear

```
Usage: tag clear [OPTIONS] [FILES]...

  Clear tags from files.

  FILES list of files

  Examples:
    - tag clear myfile{my-tag}.txt
    - tag clear *.txt

Options:
  -v, --verbose  Show additional output.
  -d, --debug    Make no changes to the file system.
  --help         Show this message and exit.
```

### Find

```
Usage: tag find [OPTIONS] TAG [PATH]

  Find files by tag.

  TAG  tag to find
  PATH path to search (default .)

  Examples:
    - tag find -r my-tag path/to/files/
    - tag find my-tag

Options:
  -a, --all        Include hidden files.
  -0, --null       End output lines with NULL (\0) instead of newline.
  -r, --recursive  Include subdirectories recursively.
  -t, --tree       Show output as tree.
  --help           Show this message and exit.
```

### Index

```
Usage: tag index [OPTIONS] PATH OUTPUT

  Index tagged files.

  PATH   path to search
  OUTPUT path to new index

  Examples:
    - tag index my-files my-index
    - tag index -r my-files my-index

Options:
  -a, --all        Include hidden files.
  -d, --debug      Make no changes to the file system.
  -r, --recursive  Include subdirectories recursively.
  -t, --tree       Create index with nested tag tree.
  -v, --verbose    Show additional output.
  --help           Show this message and exit.
```

### List

```
Usage: tag list [OPTIONS] [PATH]

  List tags on files.

  PATH path to search (default .)

  Examples:
    - tag list -r path/to/files/
    - tag list

Options:
  -a, --all        Include hidden files.
  -c, --count      Show count of matches.
  -0, --null       End output lines with NULL (\0) instead of newline.
  -r, --recursive  Include subdirectories recursively.
  --help           Show this message and exit.
```

### Remove

```
Usage: tag remove [OPTIONS] TAGS [FILES]...

  Remove tags from files.

  TAGS  comma seperated list of tags
  FILES list of files

  Examples:
    - tag remove my-tag myfile{my-tag}.txt
    - tag remove my-tag-1,my-tag-2 *.txt

Options:
  -v, --verbose  Show additional output.
  -d, --debug    Make no changes to the file system.
  --help         Show this message and exit.
```

### Rename

```
Usage: tag rename [OPTIONS] OLD_TAG NEW_TAG [FILES]...

  Rename a tag on files.

  OLD_TAG current tag name
  NEW_TAG new tag name
  FILES list of files

  Examples:
    - tag rename my-tag my-new-tag myfile{my-tag}.txt
    - tag rename my-tag my-new-tag *.txt

Options:
  -v, --verbose  Show additional output.
  -d, --debug    Make no changes to the file system.
  --help         Show this message and exit.
```

### Set

```
Usage: tag set [OPTIONS] TAGS [FILES]...

  Set tags on files.

  Add and remove tags to ensure each file has the supplied tags and only the
  supplied tags.

  TAGS  comma seperated list of tags
  FILES list of files

  Examples:
    - tag set my-tag myfile{my-tag}.txt
    - tag set my-tag-1,my-tag-2 *.txt

Options:
  -v, --verbose  Show additional output.
  -d, --debug    Make no changes to the file system.
  --help         Show this message and exit.
```

### Sort

```
Usage: tag sort [OPTIONS] [FILES]...

  Sort tags on files.

  FILES list of files

  Examples:
    - tag sort myfile{my-tag-2}{my-tag-1}.txt
    - tag sort *.txt

Options:
  -v, --verbose  Show additional output.
  -d, --debug    Make no changes to the file system.
  --help         Show this message and exit.
```

### Version

```
Usage: tag version [OPTIONS]

  Show version information.

  Examples:
    - tag version

Options:
  --help  Show this message and exit.
```

