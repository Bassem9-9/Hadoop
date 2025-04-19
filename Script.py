import tkinter as tk
from tkinter import scrolledtext
import subprocess

# Function to execute SSH command
def run_ssh():
    ip = ip_entry.get()
    user = user_entry.get()
    cmd = cmd_entry.get()

    ssh_command = f"ssh {user}@{ip} '{cmd}'"

    try:
        output = subprocess.check_output(ssh_command, shell=True, stderr=subprocess.STDOUT)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, output.decode())
    except subprocess.CalledProcessError as e:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, e.output.decode())

# Function to set and run predefined commands
def set_command(cmd):
    cmd_entry.delete(0, tk.END)
    cmd_entry.insert(0, cmd)
    run_ssh()

# GUI setup
root = tk.Tk()
root.title("SSH GUI BY BASSEM")
root.geometry("800x600")
root.configure(bg="#2d2d30")

label_style = {'bg': '#2d2d30', 'fg': 'white', 'font': ('Segoe UI', 11)}
entry_style = {'bg': '#f0f0f0', 'font': ('Segoe UI', 10)}

# Input Frame
input_frame = tk.Frame(root, bg="#2d2d30")
input_frame.grid(row=0, column=0, padx=20, pady=10, sticky='w')

tk.Label(input_frame, text="IP Address:", **label_style).grid(row=0, column=0, sticky='e', padx=5, pady=5)
ip_entry = tk.Entry(input_frame, width=30, **entry_style)
ip_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Username:", **label_style).grid(row=1, column=0, sticky='e', padx=5, pady=5)
user_entry = tk.Entry(input_frame, width=30, **entry_style)
user_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Command:", **label_style).grid(row=2, column=0, sticky='e', padx=5, pady=5)
cmd_entry = tk.Entry(input_frame, width=50, **entry_style)
cmd_entry.grid(row=2, column=1, padx=5, pady=5)

# Run Button
tk.Button(input_frame, text="Run Command", bg="#007acc", fg="white", font=('Segoe UI', 10, 'bold'),
          activebackground="#005f99", activeforeground="white", command=run_ssh)\
    .grid(row=3, column=1, pady=10, sticky='w')

# Quick Commands Frame
quick_frame = tk.Frame(root, bg="#2d2d30")
quick_frame.grid(row=1, column=0, padx=20, pady=5, sticky='w')

tk.Label(quick_frame, text="Quick Commands:", **label_style).grid(row=0, column=0, padx=5, pady=5, sticky='w')

quick_cmds = [
    ("List Files", "ls -l"),
    ("Show Path", "pwd"),
    ("HDFS Root", "hdfs dfs -ls /"),
    ("Check Hadoop", "hadoop version"),
    ("Start HDFS/YARN", "start-all.sh")
]

for i, (label, cmd) in enumerate(quick_cmds):
    tk.Button(quick_frame, text=label, width=20, bg="#444", fg="white",
              command=lambda c=cmd: set_command(c))\
        .grid(row=1, column=i, padx=5, pady=5)

# Output Box
result_text = scrolledtext.ScrolledText(root, width=95, height=22, bg="#1e1e1e", fg="#d4d4d4",
                                        insertbackground='white', font=('Consolas', 10))
result_text.grid(row=2, column=0, padx=20, pady=10)

root.mainloop()
