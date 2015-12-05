filename = 'datafile.txt' #production

import os

# filename = 'test.txt' #for test

def clear():
    os.system('clear') # on linux / os x
    # os.system('cls')  # on windows

def add_todo(new_task = ''):
    if new_task == '':
        new_task = input('UUPPS! No input! Please, write your task, and press enter:\n')
        return add_todo(new_task)
    todo_items = open_file().split('\n')
    todo_items.append(new_task)
    write_file(todo_items)
    print('Your new task successfully added')

def list_todo(): # only unchecked
    input_list = list_helper()
    clear()
    print('\n')
    print('***************************************************')
    if len(input_list) == 0:
        print(' WOOOW, Congratulate, You haven\'t incompleted task')
        print('***************************************************')

    else:
        output = []
        print('Your incompleted tasks:')
        print('***************************************************')
        for i in range(len(input_list)):
            if input_list[i][-1] != 'X':
                output.append(input_list[i])
        for i in range(len(output)):
            print(i+1, '. ',output[i], sep='')

def list_todo_only_ch(): # only checked, need for uncompleted method
    input_list = list_helper()
    output = []
    print('Completed tasks:')
    for i in range(len(input_list)):
        if input_list[i][-1] == 'X':
            output.append(input_list[i])
    for i in range(len(output)):
        print(i+1, '. ',output[i][0:-1], sep='')

def list_todo_ch(): # checked and unchecked
    output = list_helper()
    print('Your current tasks:')
    for i in range(len(output)):
        if output[i][-1] == 'X':
            print(i+1, '. [X] ',output[i][0:-1], sep='')
        else:
            print(i+1, '. [ ] ',output[i], sep='')

def list_todo_all(): # checked, unchecked, and removed
    output = remove_helper()
    print('All tasks in system:')
    for i in range(len(output)):
        if output[i] != '' and output[i][-1] == 'X':
            print(i+1, '. [X] ',output[i][0:-1], sep='')
        elif output[i] != '' and output[i][-1] == '*':
            if output[i][-2] == 'X':
                print(i+1, '. [-] ',output[i][0:-2], sep='')
            elif output[i][-1] == '*':
                print(i+1, '. [*] ',output[i][0:-1], sep='')
        elif output[i ]!= '':
            print(i+1, '. [ ] ',output[i], sep='')

def list_helper():
    todo_items = open_file().split('\n')
    output = []
    for item in todo_items:
        if item != '' and item[-1] != '*':
            output.append(item)
    return output

def remove_helper():
    todo_items = open_file().split('\n')
    output = []
    for item in todo_items:
        if item != '':
            output.append(item)
    return output

def remove_todo(task_id=''):
    if task_id == '':
        list_todo_all()
        task_id = input('Chose a number: ')
        return remove_todo(task_id)
    items = remove_helper()
    output = []
    task_id = int(task_id)
    for i in range(len(items)):
        if i != (task_id - 1):
            output.append(items[i])
        else:
            output.append(items[i] + '*')
    write_file(output)

def remove_todo_ultimate(task_id=''):
    if task_id == '':
        list_todo_all()
        task_id = input('Chose a number: ')
        return remove_todo_ultimate(task_id)
    items = remove_helper()
    output = []
    task_id = int(task_id)
    for i in range(len(items)):
        if i != (task_id - 1):
            output.append(items[i])
    write_file(output)

def list_removed_todo():
    todo_items = open_file().split('\n')
    output = []
    print('Removed elements:')
    for item in todo_items:
        if item != '' and item[-1] == '*':
            if item != '' and item[-2] == 'X':
                output.append(item[:-2])
            else:
                output.append(item[:-1])
    for i in range(len(output)):
        print(output[i][0:-1])

def completed_todo(task_id = ''):
    items = list_helper()
    output = []
    if task_id == '':
        list_todo()
        task_id = input('Choose a number: ')
        return completed_todo(task_id)

    task_id = int(task_id)
    for i in range(len(items)):
        if task_id != i+1:
            output.append(items[i])
        else:
            output.append(items[i] + 'X')
    write_file(output)

def uncompleted_todo(task_id = ''):
    items = list_helper()
    output = []
    if task_id == '':
        list_todo_only_ch()
        task_id = input('Choose a number: ')
        return uncompleted_todo(task_id)

    task_id = int(task_id)
    for i in range(len(items)):
        if task_id != i+1:
            output.append(items[i])
        else:
            output.append(items[i][0:-1])
    write_file(output)

def write_file(todo_items):
    output_file = open(filename, 'w')
    output_file.write('\n'.join(todo_items))
    output_file.close()

def open_file():
    input_file = open(filename)
    input_text = input_file.read()
    input_file.close()
    return input_text

def delete_database():
    realy = input('Are you reealy want to delete the database?(y/n)')
    if realy == 'y':
        open_file = open(filename, 'w')
        open_file.write('')
        open_file.close()

def search_todo():
    items = remove_helper()
    search_word = input('What are you looking for?: ')
    a=0
    for i in range(len(items)):
        if search_word==items[i]:
            print(str(items[i])+" is the " + str(i+1)+ ". on your list")
            break
        elif search_word==items[i][:-1] and items[i][-1]=='*':
            print(str(items[i][:-1])+ ' is already removed')
            break
        elif search_word==items[i][:-1] and items[i][-1]=='X':
            print(str(items[i][:-1])+ ' is already done')
            break
        elif search_word==items[i][:-2] and items[i][-1]=='*' and items[i][-2]=='X':
            print(str(items[i][:-2])+ ' is already done and removed')
            break
        else:
            a+=1
    if a==len(items):
        print("It is not on your todo list")
