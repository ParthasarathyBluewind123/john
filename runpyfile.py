import tkinter
from tkinter import *
import subprocess
import os
from os import system as cmd

WINDOW_SIZE = "600x400"
top = tkinter.Tk()
top.geometry(WINDOW_SIZE)
top.title("First GUI Application")


class StdoutRedirector(object):

    def __init__(self):
        # clear before get all values
        self.result = ''

    def write(self, text):
        # have to use += because one `print()` executes `sys.stdout` many times
        self.result += text

def add():   
   res = "python add.py " + e1.get() + " "+ e2.get()   
   #output = subprocess.check_output(res, shell=True) 
   try:
       output = subprocess.check_output(res,shell=True,stderr=subprocess.STDOUT)
   except subprocess.CalledProcessError as e:
       raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))   
   # keep original `sys.stdout
   old_stdout = sys.stdout
   # redirect to class which has `self.result`
   sys.stdout = StdoutRedirector()  
   print(sys.stdout.result.strip())
   output = sys.stdout.result.strip()
   # set back original `sys.stdout
   sys.stdout = old_stdout


def subt():   
   res = "python subt.py " + e1.get() + " "+ e2.get()
   #p = subprocess.Popen(res,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
   try:
       output = subprocess.check_output(res,shell=True,stderr=subprocess.STDOUT)
   except subprocess.CalledProcessError as e:
       raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))   
   #output, errors = p.communicate()
   #output = output.strip()
   # keep original `sys.stdout
   old_stdout = sys.stdout
   # redirect to class which has `self.result`
   sys.stdout = StdoutRedirector()   
   output = sys.stdout.result.strip()
   # set back original `sys.stdout
   sys.stdout = old_stdout
   
def mul():   
   res = "python mul.py " + e1.get() + " "+ e2.get()
   #p = subprocess.Popen(res,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
   try:
       output = subprocess.check_output(res,shell=True,stderr=subprocess.STDOUT)
   except subprocess.CalledProcessError as e:
       raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))   
   
   #output, errors = p.communicate()
   #output = output.strip()
   # keep original `sys.stdout
   old_stdout = sys.stdout
   # redirect to class which has `self.result`
   sys.stdout = StdoutRedirector()   
   output =sys.stdout.result.strip()
   # set back original `sys.stdout
   sys.stdout = old_stdout

def div():   
   res = "python div.py " + e1.get() + " "+ e2.get()
   #p = subprocess.Popen(res,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
   try:
       output = subprocess.check_output(res,shell=True,stderr=subprocess.STDOUT)
   except subprocess.CalledProcessError as e:
       raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
   #output, errors = p.communicate()
   #output = output.strip()
   # keep original `sys.stdout
   old_stdout = sys.stdout
   # redirect to class which has `self.result`
   sys.stdout = StdoutRedirector()   
   output = sys.stdout.result.strip()
   # set back original `sys.stdout
   sys.stdout = old_stdout


lbl_first = tkinter.Label(top, text='First Number')
lbl_first.pack()
e1 = tkinter.Entry(top) 
e1.pack()

lbl_sec = tkinter.Label(top, text='Second Number')
lbl_sec.pack()
e2 = tkinter.Entry(top) 
e2.pack()


output = ''

A = tkinter.Button(top, text ="Add", command = add)
A.pack()

S = tkinter.Button(top, text ="Subt", command = subt)
S.pack()

M = tkinter.Button(top, text ="Mul", command = mul)
M.pack()

D = tkinter.Button(top, text ="Div", command = div)
D.pack()


text = Text(top)
text.pack()
text.insert(END, output)


top.mainloop()