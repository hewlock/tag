import os
import re

TAG_RE = re.compile(r'\{[a-zA-Z0-9-]+\}')

def get_raw_tags(filename):
    return TAG_RE.findall(filename)

def get_tag(raw_tag):
    return raw_tag[1:-1]

class File:
    def __init__(self, filepath):
        self._original = filepath
        self._dir, self._filename = os.path.split(self._original)
        self._base, self._ext = os.path.splitext(self._filename)
        raw_tags = get_raw_tags(self._base)
        self._tags = set()

        for raw_tag in raw_tags:
            self._base = self._base.replace(raw_tag, '')
            self._tags.add(get_tag(raw_tag))

    def __repr__(self):
        return f"File('{self._original}')"

    @property
    def tags(self):
        return self._tags

    @property
    def filename(self):
        tags = sorted(self._tags)
        tag_text = '{' + '}{'.join(tags) + '}' if len(tags) > 0 else ''
        return f"{self._base}{tag_text}{self._ext}"

    @property
    def relative_path(self):
        return os.path.join(self._dir, self.filename)

    @property
    def absolute_path(self):
        return os.path.abspath(self.relative_path)
