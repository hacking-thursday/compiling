import os
import random

import yaml

_data = {}

def _load_data():
    dataroot = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))
    for filename in os.listdir(dataroot):
        if not filename.endswith('.yml'):
            continue
        src = filename[:-4]

        with open(os.path.join(dataroot, filename)) as f:
            _data[src] = list(yaml.safe_load_all(f))

def source_generator(src):
    if src not in _data:
        raise NotImplementedError('source_generator does not support src = {}'.format(src))

    random.seed()

    while True:
        yield _data[src][random.randint(0, len(_data[src])-1)]

_load_data()
