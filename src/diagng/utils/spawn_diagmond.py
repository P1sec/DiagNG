#!/usr/bin/env python3
from os.path import dirname, realpath, join
from os import execlp, chdir

UTILS_DIR = dirname(realpath(__file__))
MODULE_DIR = dirname(realpath(UTILS_DIR))
SRC_DIR = dirname(realpath(MODULE_DIR))
ROOT_DIR = dirname(realpath(SRC_DIR))
DIAGMOND_DIR = realpath(join(ROOT_DIR, 'diagmond'))


def main():
    chdir(DIAGMOND_DIR)

    execlp('cargo', 'cargo', 'run', '--release')


if __name__ == '__main__':
    main()
