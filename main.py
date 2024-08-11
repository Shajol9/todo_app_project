import os

script_dir = os.path.dirname(os.path.abspath(__file__))
todo_file_path = os.path.join(script_dir,'todo.txt')


def get_todo(filepath = todo_file_path):    # use of default parameter in a function defination
    with open(filepath, 'r') as local_file:
        todos = local_file.readlines()
    return todos


def write_doto(filepath, todo_list,):
    with open(filepath, 'w') as local_file:
        local_file.writelines(todo_list)


while True:
    user_action = input ("Type add, show, edit, completed or exit: ")
    user_action = user_action.strip()
    user_action = user_action.lower()

    if user_action.startswith("add"):
        todo_item = user_action[4:] + "\n"
        
        todo_list = get_todo()

        todo_list.append(todo_item.capitalize())

        write_doto(todo_file_path, todo_list)

    elif user_action.startswith("show"):
        todo_list = get_todo()

        #new_todo = [item.strip("\n") for item in todo_list]

        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            row = (f"{index+1}.{item}")
            print(row)

    elif user_action.startswith("edit"):
        try:    
            number = int(user_action[5:]) - 1

            todo_list = get_todo()
            
            print (f"Exsisting to do: {todo_list[number]}")

            update = input(f"Update item number {number + 1} to: ") + "\n"
            todo_list [number] = update.capitalize()

            write_doto(todo_file_path, todo_list)

        except ValueError or IndexError:
            print("Your command is not valid, provide a valid number after the typing 'edit'")
            continue

    elif user_action.startswith("completed"):
        try:    
            completed_task_index = int(user_action[10:]) - 1
            
            todo_list = get_todo()

            done_task = todo_list.pop(completed_task_index)
            done_task = done_task.strip('\n')

            write_doto(todo_file_path, todo_list)

            print (f"Task number {completed_task_index + 1}: '{done_task}' marked as completed \ntask {completed_task_index + 1} removed form the todo list.")
            #todo_list.remove(todo_list[completed_task_index])
        except IndexError:
            print("The item number is not present.\nProvide a valid item number!")
            continue

    elif user_action.startswith("exit"):
        print("Exit the loop and the program")
        break

    else:    
        print("Please type a valid option!")

print ("Bye")
