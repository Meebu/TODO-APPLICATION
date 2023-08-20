import streamlit as st
import functions

todos=functions.get_todos()
def add():
    todo=st.session_state['New Todo']+'\n'
    todos.append(todo)
    functions.write_todos(todos)

st.title("My todo App")
st.subheader("This is my Todo App",)


for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]# delete the item from session state library
        st.experimental_rerun()


st.text_input(label='',placeholder="Type in a Todo",key="New Todo",on_change=add)


