import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def mark_completed():
    try:
        selected_index = listbox_tasks.curselection()[0]
        task_text = listbox_tasks.get(selected_index)
        if task_text.startswith("[ ] "):
            task_text = task_text.replace("[ ] ", "[x] ")
        listbox_tasks.delete(selected_index)
        listbox_tasks.insert(selected_index, task_text)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

def save_tasks():
    with open("tasks.txt", "w") as f:
        tasks = listbox_tasks.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                listbox_tasks.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x300")

entry_task = tk.Entry(root, width=30)
entry_task.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack()

btn_add = tk.Button(frame_buttons, text="Add Task", command=add_task)
btn_add.pack(side=tk.LEFT)

btn_delete = tk.Button(frame_buttons, text="Delete Task", command=delete_task)
btn_delete.pack(side=tk.LEFT)

btn_completed = tk.Button(frame_buttons, text="Mark as Completed", command=mark_completed)
btn_completed.pack(side=tk.LEFT)

listbox_tasks = tk.Listbox(root, width=40, height=10)
listbox_tasks.pack(pady=20)

scrollbar_tasks = tk.Scrollbar(root)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

btn_save = tk.Button(root, text="Save Tasks", command=save_tasks, width=15)
btn_save.pack(pady=10)

btn_load = tk.Button(root, text="Load Tasks", command=load_tasks, width=15)
btn_load.pack()

root.mainloop()
