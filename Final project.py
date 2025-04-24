import tkinter as tk
from tkinter import messagebox

tasks = []  # In-memory task list for now

# --- Callback functions ---
def open_add_task():
    add_window = tk.Toplevel(root)
    add_window.title("Add Task")
    add_window.geometry("300x250")

    tk.Label(add_window, text="Task Name").pack(pady=5)
    task_name = tk.Entry(add_window)
    task_name.pack()

    tk.Label(add_window, text="Due Date (MM/DD)").pack(pady=5)
    due_date = tk.Entry(add_window)
    due_date.pack()

    def save_task():
        name = task_name.get().strip()
        date = due_date.get().strip()
        if not name:
            messagebox.showerror("Input Error", "Task name cannot be empty.")
            return
        tasks.append(f"{name} - Due: {date}")
        messagebox.showinfo("Success", "Task added!")
        add_window.destroy()

    tk.Button(add_window, text="Save Task", command=save_task).pack(pady=10)


def open_view_tasks():
    view_window = tk.Toplevel(root)
    view_window.title("View Tasks")
    view_window.geometry("300x300")

    tk.Label(view_window, text="Your Tasks:").pack(pady=5)

    listbox = tk.Listbox(view_window, width=40)
    listbox.pack(pady=5)
    for task in tasks:
        listbox.insert(tk.END, task)

    def delete_task():
        selected = listbox.curselection()
        if selected:
            tasks.pop(selected[0])
            listbox.delete(selected)
        else:
            messagebox.showwarning("Selection Error", "No task selected.")

    tk.Button(view_window, text="Delete Selected Task", command=delete_task).pack(pady=10)


def exit_app():
    if messagebox.askokcancel("Quit", "Do you want to quit StudyMate?"):
        root.destroy()

# --- Main Window ---
root = tk.Tk()
root.title("StudyMate – Student Study Planner")
root.geometry("400x300")

# Labels
tk.Label(root, text="Welcome to StudyMate!", font=("Helvetica", 16)).pack(pady=10)
tk.Label(root, text="Plan your study time efficiently.").pack()
tk.Label(root, text="Choose an action below:").pack(pady=5)

# Buttons
tk.Button(root, text="Add Task", command=open_add_task).pack(pady=5)
tk.Button(root, text="View Tasks", command=open_view_tasks).pack(pady=5)
tk.Button(root, text="Exit", command=exit_app).pack(pady=5)

root.mainloop()
