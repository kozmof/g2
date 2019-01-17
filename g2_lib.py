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
    parser.add_argument('-sp', '--save-path', help='save a specified path', action='store', metavar=('path'), type=str)
    parser.add_argument('-st', '--save-at-top', help='save a current path at the top', action='store_true')
    parser.add_argument('-spt', '--save-path-at-top', help='save a specified path at the top', action='store', metavar=('path'), type=str)
    parser.add_argument('-d', '--delete', help='delete a specified path', nargs=1, action='store', metavar=('num'), type=int)
    parser.add_argument('-rd', '--range-delete', help='delete nums in a specified range', nargs=2, action='store', metavar=('num', 'num'), type=int)
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

#TODO test
def write_path_with_pos(register_path, file_path):
    if not os.path.isdir(register_path):
        print("{} doesn't exist.".format(register_path))
        return 

    try:
        with open(file_path, 'r') as f:
            paths_list = [line.rstrip() for line in f.readlines()]
    except IOError:
        print("paths.txt doesn't exist.")
        return 

    if register_path not in paths_list:
        with open(file_path, 'a+') as f:
            f.write(register_path + '\n')

#TODO test
def write_path_with_pos_to_top(register_path, file_path):
    if not os.path.isdir(register_path):
        print("{} doesn't exist.".format(register_path))
        return 

    try:
        with open(file_path, 'r') as f:
            paths_list = [line.rstrip() for line in f.readlines()]
    except IOError:
        print("paths.txt doesn't exist.")
        return 

    if register_path not in paths_list:
        with open(file_path, 'w+') as f:
            for path in [register_path] + paths_list:
                f.write(path + '\n')


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
            if os.path.isdir(path):
                sign = "🗸"
            else:
                sign = "💀"

            f.write(path + '\n')
            print(path + " {}".format(sign))
            
#TODO test
def ragne_delete(num1, num2, file_path):
    try:
        with open(file_path, 'r') as f:
            paths_list = [line.rstrip() for line in f.readlines()]
    except IOError:
        print("paths.txt doesn't exist.")
        return 

    if 0 <= num1 <= len(paths_list) and 0 <= num2 <= len(paths_list):
        if num1 < num2:
            for num in range(num1, num2 + 1):
                paths_list.pop(num)
        else:
            for num in range(num2, num1 + 1):
                paths_list.pop(num)
    else:
        print("This number doesn't exist.")

    with open(file_path, 'w') as f:
        for path in paths_list:
            if os.path.isdir(path):
                sign = "🗸"
            else:
                sign = "💀"

            f.write(path + '\n')
            print(path + " {}".format(sign))


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
            if os.path.isdir(path):
                sign = "🗸"
            else:
                sign = "💀"

            f.write(path + '\n')
            print(path + " {}".format(sign))


def reverse(file_path):
    try:
        with open(file_path, 'r') as f:
            paths_list = [line.rstrip() for line in f.readlines()]
    except IOError:
        print("paths.txt doesn't exist.")
        return 

    with open(file_path, 'w') as f:
        for num, path in enumerate(reversed(paths_list)):
            if os.path.isdir(path):
                sign = "🗸"
            else:
                sign = "💀"

            f.write(path + '\n')
            print(num, path + " {}".format(sign))


def jump(num, file_path):
    try:
        with open(file_path, 'r') as f:
            paths_list = [line.rstrip() for line in f.readlines()]
    except IOError:
        print("paths.txt doesn't exist.")
        return 

    try:
        path = paths_list[num]

        if os.path.isdir(path):
            os.chdir(path)
            os.system(environ["SHELL"])
        else:
            print("{} doesn't exists".format(path))
            return 

    except IndexError:
        print("This number doesn't exist.")
        return


def manipulate(args):
    file_path = PROJECT_DIR + '/paths.txt'

    if args.list:
        for path in load_path(file_path):
            if os.path.isdir(path[1]):
                sign = "🗸"
            else:
                sign = "💀"

            print(path[0], path[1] + " {}".format(sign))

    elif args.save:
        write_path(file_path)

    elif args.save_path:
        write_path(args.save_path[0], file_path)

    elif args.save_at_top:
        write_path_to_top(file_path)

    elif args.save_path_at_top:
        write_path(args.save_path_at_top[0], file_path)

    elif args.delete:
        delete_path(args.delete[0], file_path)

    elif args.range_delete:
        range_delete(args.range_delete[0], args.ragne_delete[1], file_path)

    elif args.change:
        swap_order(args.change[0], args.change[1], file_path)

    elif args.list_reversed:
        reverse(file_path)

    else:
        jump(args.num, file_path)

