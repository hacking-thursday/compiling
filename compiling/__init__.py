import re

from compiling import console
__version__ = '0.0.1'

SUFFIX_TRANSLATE = {
    'c': 'o',
    'cpp': 'o',
    'cc': 'o',
    'cxx': 'o',
    'java': 'class',
    'py': 'pyc',
    'go': 'o',
    'y': 'c',
}


def compiled(path):
    def lookup(match):
        return '.' + SUFFIX_TRANSLATE[
            match.string[match.start() + 1: match.end()]
        ]

    def build_suffix(pattern):
        return re.escape('.' + pattern) + '$'
    regex = re.compile('(%s)' % '|'.join(
        map(build_suffix, SUFFIX_TRANSLATE.keys())
    ))
    return regex.sub(lookup, path)
