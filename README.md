# tag

Scripts to manage file tags. File tags start with `#` and have one or more letters, numbers or `-`.
Regex: `#[a-zA-Z0-9-]`.
Example tagged files:

```
My File #tag1 #tag2.md
super-cool-file#tag1#tag2.md
```

## Usage

### Synopsis

```
tag-index.sh SRC DEST
```
    
### Index

Find tagged files in `SRC` and index them in `DST`. `DST` will have one folder per tag with each tagged file symlinked inside.

```
bash ./tag-files.sh ~/Documents ~/Tags
```
