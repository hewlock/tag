# tag-cli

```
Usage: tag [OPTIONS] COMMAND [ARGS]...

  tag-cli: file name tag manager

  File tags:
    - are in the file name directly before the extension
    - start with '{' and end with '}'
    - consist of letters, numbers and the '-' character

  Examples:
    - myfile{my-tag-1}{my-tag-2}.txt
    - My Title Case File {My-Tag-1}{My-Tag-2}.txt

Options:
  --version  Print version.
  --help     Show this message and exit.

Commands:
  add     Add tags to files.
  clear   Clear tags from files.
  remove  Remove tags from files.
  set     Set tags on files.
  sort    Sort file tags.
```

## Add

```
Usage: tag add [OPTIONS] TAGS [FILES]...

  Add tags to files.

  TAGS  comma seperated list of tags
  FILES list of files

  Examples:
    - tag add my-tag myfile.txt
    - tag add my-tag-1,my-tag-2 *.txt

Options:
  -v, --verbose  Print additional output.
  -d, --debug    Make no changes to the file system.
  --help         Show this message and exit.
```

## Clear

```
Usage: tag clear [OPTIONS] [FILES]...

  Clear tags from files.

  FILES list of files

  Examples:
    - tag clear myfile{my-tag}.txt
    - tag clear *.txt

Options:
  -v, --verbose  Print additional output.
  -d, --debug    Make no changes to the file system.
  --help         Show this message and exit.
```

## Remove

```
Usage: tag remove [OPTIONS] TAGS [FILES]...

  Remove tags from files.

  TAGS  comma seperated list of tags
  FILES list of files

  Examples:
    - tag remove my-tag myfile{my-tag}.txt
    - tag remove my-tag-1,my-tag-2 *.txt

Options:
  -v, --verbose  Print additional output.
  -d, --debug    Make no changes to the file system.
  --help         Show this message and exit.
```

## Set

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
  -v, --verbose  Print additional output.
  -d, --debug    Make no changes to the file system.
  --help         Show this message and exit.
```

## Sort

```
Usage: tag sort [OPTIONS] [FILES]...

  Sort file tags.

  FILES list of files

  Examples:
    - tag sort myfile{my-tag-2}{my-tag-1}.txt
    - tag sort *.txt

Options:
  -v, --verbose  Print additional output.
  -d, --debug    Make no changes to the file system.
  --help         Show this message and exit.
```
