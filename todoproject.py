from functions import get_todos, write_todos
# import functions: this can also be used , in it you have to state file in front of funtion in file
# ie function.get_todos() : this is module
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print(now)

while True:
    user_action = input("type add, show, exit, complete, edit :")
    user_action = user_action.strip()

# python console will treat "add"  and "add " differently
# that lead to difference in command
# to counter  this we use strip() case

    if user_action.startswith('add'):

        todo = user_action[4:]                           # this is call slicing

        todos = get_todos('new.txt')                 # reading lines in text files

        todos.append(todo + '\n')                               # appending the todo in list

        write_todos(todos)                 # writing lines in text files

    elif user_action.startswith('show'):

        todos = get_todos()

        # new_todos=[item.strip('\n') for item in todos]    (for removing un wanted gap lines)

        for index, item in enumerate(todos):                   # if we want to show the items in todos list
                                                               # witheout bracket , commas ,
            item = item.strip('\n')                            # (for removing un wanted gap lines)
            row = f"{index+1}.{item}"   # f string                 the FOR LOOP come into play.
            print(row)                                         # it will print the item separately in the list

    elif user_action.startswith('exit'):
        break                                                  # break statement will take compiler out of the loop

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])                          # get integer input for the no. of todo to edit
            number = number - 1                                      # set the assigned no. as 1st is 0 as default

            todos = get_todos()
            todo_to_edited = todos[number].strip()

            new_todo = input("enter the new todo:")                      # get new todo input
            todos[number] = new_todo + "\n"                # replace

            print("new todo list is ", todos)

            write_todos(todos,'new.txt')

        except ValueError:
            print("entered command is not valid, edit 'number of todo' ")
            continue # take compiler to the starting of the loop

    elif user_action.startswith('complete'):   # when a todo is complete
        try:
            number = int(user_action[9:])
            number = number - 1

            todos = get_todos()

            todos.pop(number)                                         # pop method used to remove an item from the list

            write_todos(todos,'new.txt')

        except IndexError:
            print("enter correct command, complete 'number of todo in list' ")
            continue

    else:                                                # to state the command entered is unknown
        print("hey , you entered an unknown command")              # that is not defined above


print("bye!")
