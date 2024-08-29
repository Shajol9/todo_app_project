#from functions import get_todo, functions.write_doto 
import functions
import time

timedate = time.strftime("Time - %H:%M:%S , Date - %D-%M-%Y")
print (timedate)

while True:
    user_action = input ("Type add, show, edit, completed or exit: ")
    user_action = user_action.strip()
    user_action = user_action.lower()

    if user_action.startswith("add"):
        todo_item = user_action[4:] + "\n"
        
        todo_list = functions.get_todo()

        todo_list.append(todo_item.capitalize())

        functions.write_doto(todo_list)

    elif user_action.startswith("show"):
        todo_list = functions.get_todo()

        #new_todo = [item.strip("\n") for item in todo_list]

        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            row = (f"{index+1}.{item}")
            print(row)

    elif user_action.startswith("edit"):
        try:    
            number = int(user_action[5:]) - 1

            todo_list = functions.get_todo()
            
            print (f"Exsisting to do: {todo_list[number]}")

            update = input(f"Update item number {number + 1} to: ") + "\n"
            todo_list [number] = update.capitalize()

            functions.write_doto(todo_list)

        except (ValueError, IndexError) as error:
            if isinstance(error, ValueError):
                print("Your command is not valid, provide a valid number after the typing 'edit'\nSyntax - 'edit index_number'")
                continue
            elif isinstance(error, IndexError):
                print("No todo task available with the provided index number.\nInsert a valide index number")
                continue
            else:
                print("Unexpected error occured, Try again plese!")
                continue

    elif user_action.startswith("completed"):
        try:    
            completed_task_index = int(user_action[10:]) - 1
            
            todo_list = functions.get_todo()

            done_task = todo_list.pop(completed_task_index)
            done_task = done_task.strip('\n')

            functions.write_doto(todo_list)

            print (f"Task number {completed_task_index + 1}: '{done_task}' marked as completed \ntask {completed_task_index + 1} removed form the todo list.")
            #todo_list.remove(todo_list[completed_task_index])
        except (ValueError, IndexError) as e:
            if isinstance(e, ValueError):
                print("The number of the task taht is to be marked as completed needs to be provided.\nPlease use the Syntax: 'completed index_number'")
                continue
            elif isinstance(e, IndexError):
                print("Index number of the task to be completed is not present.\nIndex number should be with in range of todo index")
                continue
            else:
                print("Unexpected error occured, Try again plese!")
                continue

    elif user_action.startswith("exit"):
        print("Exit the loop and the program")
        break

    else:    
        print("Please type a valid option!")

print ("Bye")
