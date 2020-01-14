import tkinter as tk

# -----

import subprocess


def callback1(a, b):

    import test

    # keep original `sys.stdout
    old_stdout = sys.stdout

    # redirect to class which has `self.result`
    sys.stdout = StdoutRedirector()

    # it will execute only `function2`
    test.function1(a, b)

    # assign result to label (after removing ending "\n")
    lbl['text'] = sys.stdout.result.strip()

    # set back original `sys.stdout
    sys.stdout = old_stdout
# -----

class StdoutRedirector(object):

    def __init__(self):
        # clear before get all values
        self.result = ''

    def write(self, text):
        # have to use += because one `print()` executes `sys.stdout` many times
        self.result += text

def callback2(a, b):

    import test

    # keep original `sys.stdout
    old_stdout = sys.stdout

    # redirect to class which has `self.result`
    sys.stdout = StdoutRedirector()

    # it will execute only `function2`
    test.function2(a, b)

    # assign result to label (after removing ending "\n")
    lbl['text'] = sys.stdout.result.strip()

    # set back original `sys.stdout
    sys.stdout = old_stdout

# -----

def callback4(a, b):

    import test

    # keep original `sys.stdout
    old_stdout = sys.stdout

    # redirect to class which has `self.result`
    sys.stdout = StdoutRedirector()

    # it will execute only `function2`
    test.function4(a, b)

    # assign result to label (after removing ending "\n")
    lbl['text'] = sys.stdout.result.strip()

    # set back original `sys.stdout
    sys.stdout = old_stdout

# -----

import sys

class StdoutRedirectorLabel(object):

    def __init__(self, widget):
        self.widget = widget
        # clear at start because it will use +=
        self.widget['text'] = ''

    def write(self, text):
        # have to use += because one `print()` executes `sys.stdout` many times
        self.widget['text'] += text

def callback3(a, b):

    import test

    # keep original `sys.stdout
    old_stdout = sys.stdout

    # redirect to class which will add text to `lbl`
    sys.stdout = StdoutRedirectorLabel(lbl)

    # it will execute only `function3` and assign result to Label (with ending "\n")
    test.function3(a, b)

    # set back original `sys.stdout
    sys.stdout = old_stdout

# --- main ---

master = tk.Tk()
master.geometry('600x400')
master.title("First GUI Application")

lbl_f = tk.Label(master, text='First Number')
lbl_s = tk.Label(master, text='Second Number')
e1 = tk.Entry(master) 
e2 = tk.Entry(master) 

btn1 = tk.Button(master, text="add", command=callback1(e1.get(),e2.get()))
btn1.pack()

btn2 = tk.Button(master, text="subt", command=callback2(e1.get(),e2.get()))
btn2.pack()

btn3 = tk.Button(master, text="mul", command=callback3(e1.get(),e2.get()))
btn3.pack()

btn4 = tk.Button(master, text="div", command=callback4(e1.get(),e2.get()))
btn4.pack()

lbl = tk.Label(master, text='')
#lbl = tk.Text(master, text='')
lbl.pack()


master.mainloop()