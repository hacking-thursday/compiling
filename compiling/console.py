#!/usr/bin/env python
import argparse
import time

import six
from compiling import config
from compiling._utils import source_generator


def main():
    generator = source_generator('c')
    while True:
        print(next(generator))
        time.sleep(1)

if __name__ == '__main__':
    main()
