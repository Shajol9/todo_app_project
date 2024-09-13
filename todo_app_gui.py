import functions
import FreeSimpleGUI as fsg
import time
import os

if not os.path.exists('todo.txt'):
    with open('todo.txt', 'w') as file:
        pass

fsg.theme("DarkGreen4")
# Defining wedgets 
clock_lable = fsg.Text("", key="clock")
lable = fsg.Text("Type your To-Do")
input_box = fsg.InputText(tooltip="Enter todo here", key="todo")
add_button = fsg.Button("Add")

list_box_display = fsg.Listbox(values=functions.get_todo(), key='todos',
                               enable_events=True, size = [50,8] )
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete")

exit_button = fsg.Button("Exit")

# Window instanciation and layout
window = fsg.Window('To-Do App', 
                    layout=[[clock_lable],
                            [lable],
                            [input_box, add_button],
                            [list_box_display, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 18))

#Run the windows continously to monitor and react to activities
while True:
    event, values = window.read(timeout=500)
    print(event)
    print(values)
    match event:
        case "Add":
            todo_list = functions.get_todo()
            new_todo = values['todo'] + '\n'
            todo_list.append(new_todo)
            functions.write_todo(todo_list)
            window['todos'].update(values=todo_list)
            window["todo"].update(value="")
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"
                todo_list = functions.get_todo()
                todo_edit_index = todo_list.index(todo_to_edit)
                todo_list[todo_edit_index] = new_todo
                functions.write_todo(todo_list)
                window['todos'].update(values=todo_list)
                window['todo'].update(value="")
            except IndexError:
                fsg.popup("Please selcet the todo to edit first, then press edit.", font=('Helvetica', 18))
        case "todos":
            try: 
                window['todo'].update(value=values['todos'][0].strip("\n"))
            except IndexError:
                continue
        case "Complete":
            try:
                todo_completed = values['todos'][0]
                todo_list = functions.get_todo()
                todo_completed_index = todo_list.index(todo_completed)
                completed = todo_list.pop(todo_completed_index)
                functions.write_todo(todo_list)
                window['todos'].update(values=todo_list)
                window['todo'].update(value="")
            except:
                fsg.popup("Please selcet the todo to be marked as completed, then press complete.", font=('Helvetica', 18))
        case "Exit":
            break    
        case fsg.WIN_CLOSED:
            break
    window["clock"].update(value=time.strftime("Date: %b %d, %Y. Time: %H:%M:%S"))

window.close()