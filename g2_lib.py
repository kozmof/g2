import os
import argparse
from os import environ
from pathlib import Path

# Orders of saved paths are consistent with paths.txt.

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


def register():
    parser = argparse.ArgumentParser("advanced cd manipulator")
    parser.add_argument('num', nargs='?', default=0, type=int)
    parser.add_argument('-m', '--match', nargs=1, action='store', default="", type=str)
    parser.add_argument('-ma', '--match-all', nargs=1, action='store', default="", type=str)
    parser.add_argument('-l', '--list', help='list all saved paths', action='store_true')
    parser.add_argument('-lr', '--list-reversed', help='reverse a list then shows them', action='store_true')
    parser.add_argument('-s', '--save', help='save a current path', action='store_true')
    parser.add_argument('-sp', '--save-path', help='save a specified path', action='store', metavar=('path'), type=str)
    parser.add_argument('-st', '--save-at-top', help='save a current path at the top', action='store_true')
    parser.add_argument('-spt', '--save-path-at-top', help='save a specified path at the top', action='store', metavar=('path'), type=str)
    parser.add_argument('-d', '--delete', help='delete a specified path', nargs=1, action='store', metavar=('num'), type=int)
    parser.add_argument('-dr', '--delete-range', help='delete nums in a specified range', nargs=2, action='store', metavar=('num', 'num'), type=int)
    parser.add_argument('-c', '--change', help='change path order', nargs=2, action='store', metavar=('num', 'num'), type=int)
    args = parser.parse_args()
    return args


def load_path(file_path, with_num=False):
    try:
        with open(file_path, 'r') as f:
            if with_num:
                paths_list = [(num, line.rstrip()) for num, line in enumerate(f.readlines())]
            else:
                paths_list = [line.rstrip() for line in f.readlines()]

            return paths_list

    except IOError:
        print("paths.txt doesn't exist.")
        return 


def make_sign(path):
    if os.path.isdir(path):
        sign = "✔️"
    else:
        sign = "💀"

    return sign


def save(file_path, paths_list, reverse=False):
    with open(file_path, 'w') as f:
        if not reverse:
            enum = enumerate(paths_list)
        else:
            enum = enumerate(reversed(paths_list))

        for num, path in enum:
            sign = make_sign(path)
            f.write(path + '\n')
            print(num, path + " {}".format(sign))


def write_path(file_path):
    paths_list = load_path(file_path)

    if os.getcwd() not in paths_list:
        with open(file_path, 'a+') as f:
            f.write(os.getcwd() + '\n')


def write_path_with_pos(register_path, file_path):
    register_path = os.path.realpath(str(Path(register_path).expanduser()))
    if not os.path.isdir(register_path):
        print("{} doesn't exist.".format(register_path))
        return 

    paths_list = load_path(file_path)

    if register_path not in paths_list:
        with open(file_path, 'a+') as f:
            f.write(register_path + '\n')


def write_path_to_top(file_path):
    paths_list = load_path(file_path)

    if os.getcwd() not in paths_list:
        with open(file_path, 'w+') as f:
            for path in [os.getcwd()] + paths_list:
                f.write(path + '\n')


def write_path_with_pos_to_top(register_path, file_path):
    register_path = os.path.realpath(str(Path(register_path).expanduser()))
    if not os.path.isdir(register_path):
        print("{} doesn't exist.".format(register_path))
        return 

    paths_list = load_path(file_path)

    if register_path not in paths_list:
        with open(file_path, 'w+') as f:
            for path in [register_path] + paths_list:
                f.write(path + '\n')


def delete_path(num, file_path):
    paths_list = load_path(file_path)

    try:
        paths_list.pop(num)

    except IndexError:
        print("This number doesn't exist.")
        return 

    save(file_path, paths_list)
            

def range_delete(num1, num2, file_path):
    paths_list = load_path(file_path)

    if 0 <= num1 <= len(paths_list) and 0 <= num2 <= len(paths_list):
        if num1 < num2:
            for _ in range(num1, num2 + 1):
                paths_list.pop(num1)
        else:
            for _ in range(num2, num1 + 1):
                paths_list.pop(num2)
    else:
        print("This number doesn't exist.")

    save(file_path, paths_list)


def swap_order(num1, num2, file_path):
    paths_list = load_path(file_path)

    try:
        paths_list[num1], paths_list[num2] = paths_list[num2], paths_list[num1] 
    except IndexError:
        print("A first or second number doesn't exist.")
        return 

    save(file_path, paths_list)


def reverse(file_path):
    paths_list = load_path(file_path)
    save(file_path, paths_list, reverse=True)


def jump(num, file_path):
    paths_list = load_path(file_path)

    try:
        path = paths_list[num]

        if os.path.isdir(path):
            os.chdir(path)
            os.system(environ["SHELL"])
        else:
            print("{} doesn't exist".format(path))
            return 

    except IndexError:
        print("This number doesn't exist.")
        return


def match(name, file_path, full_path=False):
    paths_list = load_path(file_path)
    flag = False

    try:
        for path in paths_list:
            if path[-1] == "/":
                path = path[:-1]

            split_list = path.split("/")

            if full_path:
                for directory in split_list:
                    if name in directory:
                        flag = True
                        break
            else:
                if split_list and name in split_list[-1]:
                    flag = True

            if flag:
                if os.path.isdir(path):
                    os.chdir(path)
                    os.system(environ["SHELL"])
                    return 
                else:
                    print("{} doesn't exist".format(path))
                    return 

    except IndexError:
        print("This number doesn't exist.")
        return


def manipulate(args):
    file_path = PROJECT_DIR + '/paths.txt'

    if args.list:
        for num, path in load_path(file_path, with_num=True):
            sign = make_sign(path)
            print(num, path + " {}".format(sign))

    elif args.save:
        write_path(file_path)

    elif args.save_path:
        write_path_with_pos(args.save_path, file_path)

    elif args.save_at_top:
        write_path_to_top(file_path)

    elif args.save_path_at_top:
        write_path_with_pos_to_top(args.save_path_at_top, file_path)

    elif args.delete:
        delete_path(args.delete[0], file_path)

    elif args.delete_range:
        range_delete(args.delete_range[0], args.delete_range[1], file_path)

    elif args.change:
        swap_order(args.change[0], args.change[1], file_path)

    elif args.list_reversed:
        reverse(file_path)

    elif args.match:
        match(args.match[0], file_path)

    elif args.match_all:
        match(args.match_all[0], file_path, full_path=True)

    else:
        jump(args.num, file_path)

