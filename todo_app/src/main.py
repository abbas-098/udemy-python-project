import streamlit as st
from db import add_task, init_db, get_all_tasks, update_task, remove_task
import pandas as pd

# Always initialize the db first
init_db()
DB_PATH = "todo.db"


st.title("My Todo App")

task = st.text_input("Add a new task:")

add_task_button = st.button("Add Task", type="primary")


edit_ask_id = st.text_input("Enter the ID to edit the task:", key="Edit")
edit_task_button = st.button("Edit Task", type="secondary")
if edit_ask_id:
    edit_task_description = st.text_input("Enter the new description:")


remove_task_id = st.text_input("Enter the ID to remove the task:", key="Remove")
remove_task_button = st.button("Remove Task", type="secondary")

if add_task_button:
    if task:
        add_task(DB_PATH, task)
        st.success("Successfully added the task", icon="✅")
    else:
        st.error("Error adding the task", icon="🚨")

st.write("To do List")

to_do = get_all_tasks(DB_PATH)

if to_do:
    df = pd.DataFrame(to_do, columns=["ID", "Description", "Status", "Time Created"])
    st.table(data=df, border=True)


# Editing a task
if edit_task_button:
    if edit_ask_id:
        update_task(DB_PATH, edit_ask_id, edit_task_description)
        st.success(
            f"Successfully edit the task id {edit_ask_id}. Pleas refresh page",
            icon="✅",
        )
    else:
        st.error("Error editing the task", icon="🚨")


# Remove a task
if remove_task_button:
    if remove_task_id:
        remove_task(DB_PATH, remove_task_id)
        st.success(
            f"Successfully removed the task id {edit_ask_id}. Pleas refresh page",
            icon="✅",
        )
    else:
        st.error("Error removing the task", icon="🚨")
