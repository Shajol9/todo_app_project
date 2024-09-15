import streamlit as st
import functions


todo_list = functions.get_todo()

def add_todo():
    newtodo = st.session_state["new_todo"] + "\n"
    todo_list.append(newtodo)
    functions.write_todo(todo_list)

st.title("My TO-DO App")
st.subheader("This is my first webapp")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        completed_item =  todo_list.pop(index)
        functions.write_todo(todo_list)
        del st.session_state[todo]
        st.rerun()

st.text_input(label ="Add new todo:", 
              placeholder="Type here to add nwe todo...",
              on_change=add_todo, key="new_todo")