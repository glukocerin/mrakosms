from sys import *
import os
import todo

def help():
    #os.system('clear') # on linux / os x
    os.system('cls')  # on windows
    open_file = open('help.txt')
    open_text = open_file.read()
    open_file.close()
    print(open_text)

if len(argv) != 1 and len(argv) < 4:
    if (argv[1] == 'add'):
        if len(argv) == 3:
            todo.add_todo(argv[2])
        else:
            todo.add_todo()
    elif argv[1] == 'st':
            todo.list_todo_all()
    elif (argv[1] == 'ls'):
        if len(argv) == 3 and argv[2] == '-l':
            todo.list_todo_ch()
        elif len(argv) == 3 and argv[2] == '-la':
            todo.list_todo_all()
        elif len(argv) == 3 and argv[2] == '-ch':
            todo.list_todo_only_ch()
        else:
            todo.list_todo()
    elif (argv[1] == 'rm'):
        if len(argv) == 3 and argv[2] == '-r':
            todo.remove_todo()
        elif len(argv) == 3 and argv[2] == '-rf':
            todo.remove_todo_ultimate()
        else:
            todo.remove_todo()
    elif (argv[1] == 'ch'):
        todo.completed_todo()
    elif (argv[1] == 'uch'):
        todo.uncompleted_todo()
    elif (argv[1] == '--help'):
        help()
    elif (argv[1]) == '--version':
        print('TODO for Developers version 0.1')
    elif (argv[1] == 'del'):
        todo.delete_database()
    elif (argv[1] == 'src'):
        todo.search_todo()
    elif (argv[1] == '--menu'):
        todo.clear()
        #os.system('clear') # on linux / os x
        os.system('cls')  # on windows
        menu.menu_input(True)
    else:
        print('Invalid syntax')
else:
    help()
