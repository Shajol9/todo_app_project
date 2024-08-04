import os

script_dir = os.path.dirname(os.path.abspath(__file__))
todo_file_path = os.path.join(script_dir,'todo.txt')


while True:
    user_action = input ("Type add, show, edit, completed or exit: ")
    user_action = user_action.strip()
    user_action = user_action.lower()

    if user_action.startswith("add"):
        todo_item = user_action[4:] + "\n"
        
        file = open(todo_file_path, 'r')
        todo_list=file.readlines()
        file.close()

        todo_list.append(todo_item.capitalize())

        file = open(todo_file_path, 'w')
        file.writelines(todo_list)
        file.close()

    elif user_action.startswith("show"):
        with open(todo_file_path, 'r') as file:
            todo_list = file.readlines()

        #new_todo = [item.strip("\n") for item in todo_list]

        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            row=(f"{index+1}.{item}")
            print(row)

    elif user_action.startswith("edit"):
        try:    
            number = int(user_action[5:]) - 1
            # print (f"Exsisting to do: {todo_list[number]}")
            # todo_list [number] = input (f"Updae your todo item to: {number}: ")
            # print (f"Updated todo item {number} is: {todo_list[number]}")

            with open(todo_file_path, 'r') as file:
                todo_list = file.readlines()
                print (f"Exsisting to do: {todo_list[number]}")

            update = input(f"Update item number {number + 1} to: ") + "\n"
            todo_list [number] = update.capitalize()

            with open(todo_file_path, 'w') as file:
                file.writelines(todo_list)
        except ValueError or IndexError:
            print("Your command is not valid, provide a valid number after the typing 'edit'")
            continue

    elif user_action.startswith("completed"):
        try:    
            completed_task_index = int(user_action[10:]) - 1
            
            with open(todo_file_path, 'r') as file:
                todo_list = file.readlines()

            done_task = todo_list.pop(completed_task_index)
            done_task = done_task.strip('\n')

            with open(todo_file_path, 'w') as file:
                file.writelines(todo_list)

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
