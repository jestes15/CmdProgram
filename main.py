from implementation import *
import sys


def execute(argv):
    str_split = string_split(argv)
    user_choice(str_split)


def execute_prog():
    start_msg = 'Welcome to my command line tool'
    print(f'{start_msg}')
    bool_val = True
    while bool_val:
        cmd_prompt = 'msr> '
        user_input = str(input(f'{cmd_prompt}'))
        str_split = string_split(user_input)

        if 'exit' in str_split[0]:
            bool_val = False
        else:
            user_choice(str_split)


class UndefinedArgument:
    def __init__(self):
        print("An argument was passed that is not recognized")


if __name__ == '__main__':
    if len(sys.argv) > 2:
        arg1 = sys.argv[1]
        if arg1 == "-c":
            arg2 = sys.argv[2]
            execute(arg2)
        elif arg1 == "-t":
            execute_prog()
    else:
        execute_prog()
