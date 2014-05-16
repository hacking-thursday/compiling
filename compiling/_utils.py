import os
import random
import yaml
import six

USERDIR = os.path.join(os.path.expanduser('~'), '.compiling')
SYSDIR = os.path.abspath(os.path.dirname(__file__))

DATADIR = 'data'

_data = {}


def join_sys(*path):
    '''build a path under the system's directory'''
    return os.path.join(SYSDIR, *path)


def join_user(*path):
    '''build a path under the user's directory'''
    return os.path.join(USERDIR, *path)


def _load_data():
    dataroot = join_sys(DATADIR)
    for filename in os.listdir(dataroot):
        if not filename.endswith('.yml'):
            continue
        src = filename[:-4]

        with open(join_sys(DATADIR, filename)) as f:
            _data[src] = list(yaml.safe_load_all(f))


def source_generator(src):
    if src not in _data:
        raise NotImplementedError(
            'source_generator does not support src = %s' % src
        )

    random.seed()

    while True:
        yield _data[src][random.randint(0, len(_data[src]) - 1)]

_load_data()
if not os.path.exists(USERDIR):
    if os.path.lexists(USERDIR):
        os.unlink(USERDIR)
    os.mkdir(USERDIR)
