import functions
import FreeSimpleGUI as fsg

lable = fsg.Text("Type your To-Do")
input_box = fsg.InputText(tooltip="Enter todo here", key="todo")
add_button = fsg.Button("Add")
list_box_display = fsg.Listbox(values=functions.get_todo(), key='todos',
                               enable_events=True, size = [40,8] )
edit_button = fsg.Button("Edit")

window = fsg.Window('To-Do App', 
                    layout=[[lable],[input_box, add_button], [list_box_display, edit_button]],
                    font=('Helvetica', 18))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todo_list = functions.get_todo()
            new_todo = values['todo'] + '\n'
            todo_list.append(new_todo)
            functions.write_todo(todo_list)
            window['todos'].update(values=todo_list)
        case "Edit":
            todo_to_edit = values['todos'][0]
            todo_list = functions.get_todo()
            todo_edit_index = todo_list.index(todo_to_edit)
            new_todo = values['todo'] + '\n'
            todo_list[todo_edit_index] = new_todo
            functions.write_todo(todo_list)
            window['todos'].update(values=todo_list)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case fsg.WIN_CLOSED:
            break

window.close()