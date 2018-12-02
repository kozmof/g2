import argparse
import os
from os import environ

#Orders of saved paths are consistent with paths.txt.

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


def register():
    parser = argparse.ArgumentParser("advanced cd manipulator")
    parser.add_argument("num", nargs='?', default=0, type=int)
    parser.add_argument('-l', '--list', help='list all saved paths', action='store_true')
    parser.add_argument('-lr', '--list-reversed', help='reverse a list then shows them', action='store_true')
    parser.add_argument('-s', '--save', help='save a current path', action='store_true')
    parser.add_argument('-st', '--save-at-top', help='save a current path at the top', action='store_true')
    parser.add_argument('-d', '--delete', help='delete a specified path', nargs=1, action='store', metavar=('num'), type=int)
    parser.add_argument('-c', '--change', help='change path order', nargs=2, action='store', metavar=('num', 'num'), type=int)
    args = parser.parse_args()
    return args


def load_path(file_path):
    try:
        with open(file_path, 'r') as f:
            paths_list = [(num, line.rstrip()) for num, line in enumerate(f.readlines())]
            return paths_list
    except IOError:
        print("paths.txt doesn't exist.")
        return 


def write_path(file_path):
    try:
        with open(file_path, 'r') as f:
            paths_list = [line.rstrip() for line in f.readlines()]
    except IOError:
        print("paths.txt doesn't exist.")
        return 

    if os.getcwd() not in paths_list:
        with open(file_path, 'a+') as f:
            f.write(os.getcwd() + '\n')


def write_path_to_top(file_path):
    try:
        with open(file_path, 'r') as f:
            paths_list = [line.rstrip() for line in f.readlines()]
    except IOError:
        print("paths.txt doesn't exist.")
        return 

    if os.getcwd() not in paths_list:
        with open(file_path, 'w+') as f:
            for path in [os.getcwd()] + paths_list:
                f.write(path + '\n')


def delete_path(num, file_path):
    try:
        with open(file_path, 'r') as f:
            paths_list = [line.rstrip() for line in f.readlines()]
    except IOError:
        print("paths.txt doesn't exist.")
        return 

    try:
        paths_list.pop(num)

    except IndexError:
        print("This number doesn't exist.")
        return 

    with open(file_path, 'w') as f:
        for path in paths_list:
            f.write(path + '\n')
            print(path)


def swap_order(num1, num2, file_path):
    try:
        with open(file_path, 'r') as f:
            paths_list = [line.rstrip() for line in f.readlines()]
    except IOError:
        print("paths.txt doesn't exist.")
        return 

    try:
        paths_list[num1], paths_list[num2] = paths_list[num2], paths_list[num1] 
    except IndexError:
        print("A first or second number doesn't exist.")
        return 

    with open(file_path, 'w') as f:
        for path in paths_list:
            f.write(path + '\n')


def reverse(file_path):
    try:
        with open(file_path, 'r') as f:
            paths_list = [line.rstrip() for line in f.readlines()]
    except IOError:
        print("paths.txt doesn't exist.")
        return 

    with open(file_path, 'w') as f:
        for num, path in enumerate(reversed(paths_list)):
            f.write(path + '\n')
            print((num, path))


def jump(num, file_path):
    try:
        with open(file_path, 'r') as f:
            paths_list = [line.rstrip() for line in f.readlines()]
    except IOError:
        print("paths.txt doesn't exist.")
        return 

    try:
        path = paths_list[num]
        os.chdir(path)
        os.system(environ["SHELL"])
    except IndexError:
        print("This number doesn't exist.")
        return


def manipulate(args):
    file_path = PROJECT_DIR + '/paths.txt'

    if args.list:
        for path in load_path(file_path):
            print(path[0], path[1])

    elif args.save:
        write_path(file_path)

    elif args.save_at_top:
        write_path_to_top(file_path)

    elif args.delete:
        delete_path(args.delete[0], file_path)

    elif args.change:
        swap_order(args.change[0], args.change[1], file_path)

    elif args.list_reversed:
        reverse(file_path)

    else:
        jump(args.num, file_path)

