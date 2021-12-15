# Tag

A command line interface to manage file name tags.

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

