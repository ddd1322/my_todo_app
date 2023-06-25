import os

if not os.path.exists('new.txt'):
    with open('new.txt', 'w') as file:
        pass


def get_todos(textfile='new.txt'):  # custom function
    with open(textfile, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, textfile='new.txt'):
    with open('new.txt', 'w') as file_local:
        file_local.writelines(todos_arg)


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0245
    return meters
