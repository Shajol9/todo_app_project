import streamlit as st
import functions


todo_list = functions.get_todo()

def add_todo():
    newtodo = st.session_state["new_todo"] + "\n"
    todo_list.append(newtodo)
    functions.write_todo(todo_list)

st.title("My TO-DO App")
st.subheader("This is my first webapp")

for todo in todo_list:
    st.checkbox(todo)


st.text_input(label ="Add new todo:", 
              placeholder="Type here to add nwe todo...",
              on_change=add_todo, key="new_todo")