import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n' #grabs todo entered into text box and puts into session state type (looks like dict)
    todos.append(todo)
    functions.write_todos(todos)


st.title("My todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo", label_visibility="collapsed",  placeholder='Add a todo...',
              on_change=add_todo, key='new_todo')
