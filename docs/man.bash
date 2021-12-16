function command {
    echo "=head2 $1"
    echo ""
    ./tag.py $2 --help
    echo ""
}

function version {
    ./tag.py version | sed -n "$1p"
}

echo "=encoding utf8"
echo ""
echo "=head1 NAME"
echo ""
echo "tag - manage file name tags"
echo ""
echo "=head1 SYNOPSIS"
echo ""
echo "tag [I<OPTION>]..."
echo "tag COMMAND [I<OPTION>]... [I<ARG>]..."
echo ""
echo "=head1 DESCRIPTION"
echo ""
./tag.py --help
echo ""
echo "=head1 COMMANDS"
echo ""

command ADD add
command CLEAR clear
command FIND find
command INDEX index
command LIST list
command REMOVE remove
command RENAME rename
command SET set
command SORT sort
command VERSION version

echo "=head1 EXAMPLE"
echo ""
echo "Rename all tags in a directory recursively"
echo ""
echo "  tag find -r0 my-old-tag ~/Documents | xargs -0 tag rename my-old-tag my-new-tag"
echo ""
echo "=head1 AUTHOR"
echo ""
version 6
echo ""
echo "=head1 LICENSE"
echo ""
version 2
echo ""
echo "=head1 LINKS"
echo ""
echo "=over"
echo ""
echo "=item Project: L<https://github.com/hewlock/tag>"
echo ""
echo "=back"
