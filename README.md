# tag-cli

CLI to manage file tags. Tags start with `{`; have one or more letters, numbers or `-`; then end with `}`.

Regex: `\{[a-zA-Z0-9-]\}`

Example: `my-file{my-tag-1}{my-tag-2}.txt`

## Usage

```
Usage: tag [OPTIONS] COMMAND [ARGS]...

  tag-cli: filename tags v0.1

Options:
  --verbose / --quiet
  --help               Show this message and exit.

Commands:
  add  Add tags to files.
```

### Add

```
Usage: tag add [OPTIONS] TAGS [FILES]...

  Add tags to files.

  TAGS  comma seperated list of tags
  FILES list of files

  Examples:
    tag add mytag myfile.txt
    tag add mytag1,mytag2 *.txt

Options:
  --help  Show this message and exit.
```
