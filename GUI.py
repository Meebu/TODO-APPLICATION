import PySimpleGUI as pg
import functions
import time
import os

if not os.path.exists("todos.txt"):# if file not present in directory it will create in the directory
    with open('todos.txt','w') as file:
        pass

pg.theme("DarkPurple4")
label = pg.Text("Type in a TO-DO")
input_box = pg.InputText(tooltip="Enter TODO", key='Todo')
clock=pg.Text('',key='clock')
"""key is a dictionary key : whose value is 
when we add button by input some text , it will be the value of todo Key
"""
button = pg.Button("Add" ,size=10)

list_box=pg.Listbox(values=functions.get_todos(),size=[40,10],enable_events=True,key='Todos')#Todos has already a list
edit_button=pg.Button("Edit",size=10)
complete_button=pg.Button("Complete",size=10)
exit_button=pg.Button("Exit",size=10)
window = pg.Window("My To Do App",
                   layout=[[label],[clock], [input_box, button],[list_box,complete_button],[edit_button,exit_button]],
                   font=('Helvetica',20))
while True:

    event, values= window.read(timeout=200)# this is used to display the time live, refresh the screenafter 200ms
    window['clock'].update(value=time.strftime("%b %d ,%Y %H:%M:%S"))
    print(event)
    print(values)
    """td represents the dictionary and event represents the button that is pressed"""
    match event:
        case 'Add':
            val = values['Todo'] + "\n"
            todos = functions.get_todos()
            todos.append(val)
            functions.write_todos(todos)
            window["Todos"].update(values=todos)
        case 'Edit':
            try:

                todo_to_edit=values['Todos'][0]
                """Value[Todos] is a list having multiple error in """
                print("Name of edit ",todo_to_edit)
                """
                As todos is the list and [0] is that on clicking that , it will be in Todos list to get that """
                new_todo=values['Todo']+'\n'
                todos=functions.get_todos()
                index=todos.index(todo_to_edit)
                todos[index]=new_todo
                functions.write_todos(todos)
                window['Todos'].update(values=todos)# this value is the list of todos in the case
            except IndexError:
                pg.popup("Please Select Item first",font=("Helvitca",20))
        case 'Todos':
            window['Todo'].update(value=values['Todos'][0])

        case pg.WIN_CLOSED:  # when press Cross button it will automatically cancelled
            break

        case 'Complete':
            todo_to_complete=values['Todo']
            print(todo_to_complete)
            todos=functions.get_todos()
            index=todos.index(todo_to_complete)
            print(index)
            todos.pop(index)
            functions.write_todos(todos)
            window['Todos'].update(values=todos)

        case 'Exit':
            window.close()
window.close()
