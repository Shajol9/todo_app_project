import functions
import FreeSimpleGUI as fsg

lable = fsg.Text("Type your To-Do")
input_box = fsg.InputText(tooltip="Enter todo here")
button = fsg.Button("ADD")

window = fsg.Window('To-Do App', layout=[[lable],[input_box, button]])
window.read()
window.close()