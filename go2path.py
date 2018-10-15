#! /usr/bin/env python


import argparse
import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def register():
    parser = argparse.ArgumentParser("advanced cd manipulator")
    parser.add_argument("path", nargs='?', default=os.getcwd(), type=str)
    parser.add_argument('-l', '--list', help='list all saved paths', action='store_true')
    parser.add_argument('-j', '--jump', help='jump to a specified path', nargs=1, action='store', metavar=('num'))
    parser.add_argument('-s', '--save', help='save a current path', action='store_true')
    parser.add_argument('-d', '--delete', help='delete a specified path', nargs=1, action='store', metavar=('num'))
    args = parser.parse_args()
    return args


def load_file():
    file_path = PROJECT_DIR + '/paths.txt'
    with open(file_path, 'r+') as f:
        paths = [line.rstrip() for line in f.readlines()]
    return set(paths)


def manipulation(args):
    pass

if __name__ == '__main__':
    args = register()
    manipulation(args)
    file_paths = load_file()
    for path in file_paths:
        print(path)

