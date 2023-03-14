import tkinter as tk
from tkinter import  *
#import lizard_13 as lz13
import lizard_13_byte as lz13
from tkinter import ttk

my_pc = lz13.lizard_13()
ide_debug_steps = 0

def ide_run():
    #my_pc.output = ""
    output.delete("1.0", END)
    text = t.get("1.0", "end")
    for command in text.split("\n"):
        my_pc.execute_command(command)
    output.insert("1.0", my_pc.output)

def ide_debug():
    global ide_debug_steps
    print(ide_debug_steps)
    ide_debug_steps += 1
    #my_pc.output = ""
    output.delete("1.0", END)
    text = t.get("1.0", "end")
    commands = text.split("\n")
    my_pc.clear_registers()
    for i in range(ide_debug_steps):
        my_pc.execute_command(commands[i])

    output.insert("1.0", my_pc.output)

def ide_save():
    code_file = open('ide_code.txt', 'wb')
    code_text = t.get("1.0", "end")
    code_file.write(code_text.encode())
    code_file.close()
    #pass

def ide_load():
    code_file = open('ide_code.txt', 'rb')
    code_text = code_file.read()
    t.delete("1.0", END)
    t.insert("1.0", code_text.decode())
    code_file.close()
    #pass

window = tk.Tk()
window.title("Text Widget Example")
#window.geometry('800x600')

b1 = tk.Button(window, text="Run", command=ide_run)
b1.grid(column=0, row=15, ipadx=5, ipady=5, padx=5, pady=5, sticky="ew")

b2 = tk.Button(window, text="Debug", command=ide_debug)
b2.grid(column=1, row=15, ipadx=5, ipady=5, padx=5, pady=5, sticky="ew")

b3 = tk.Button(window, text="Save", command=ide_save)
b3.grid(column=2, row=15, ipadx=5, ipady=5, padx=5, pady=5, sticky="ew")

b4 = tk.Button(window, text="Load", command=ide_load)
b4.grid(column=3, row=15, ipadx=5, ipady=5, padx=5, pady=5, sticky="ew")

# Text Widget
t = tk.Text(window, width=50, height=35)
t.grid(column=0, columnspan=4, row=16, ipadx=5, ipady=5, padx=5, pady=5)

output = tk.Text(window, width = 100, height = 35)
output.grid(column=4, row=16, ipadx=5, ipady=5, padx=5, pady=5)

window.mainloop()
