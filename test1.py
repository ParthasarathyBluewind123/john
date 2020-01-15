import tkinter as tk
import subprocess 
import os

fields = ('Host Name','Test1','Test2','Test3','Test4')

import subprocess

def Ping(entries):
    cmd = ["ping", entries['Host Name'].get()]
    output = subprocess.check_output(cmd)    
    print('>', output)    
    result['text'] = output.decode('utf-8')

def makeform(root, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
        ent = tk.Entry(row)        
        row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, 
                 expand=tk.YES, 
                 fill=tk.X)
        entries[field] = ent
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Test")
    root.geometry("1000x500")  
    
    ents = makeform(root, fields)    
    
    b1 = tk.Button(root, height=2, width=12, text='Ping', command=(lambda e=ents: Ping(e)))
    b1.pack(side=tk.LEFT,                   
                 padx=2, 
                 pady=2)
    
    b2 = tk.Button(root, height=2, width=12, text='Start', command=(lambda e=ents: Ping(e)))
    b2.pack(side=tk.LEFT, 
                 padx=2, 
                 pady=2)
    
    b3 = tk.Button(root, height=2, width=12, text='Shut Down', command=(lambda e=ents: Ping(e)))
    b3.pack(side=tk.LEFT, 
                 padx=2, 
                 pady=2)
    
    b4 = tk.Button(root, height=2, width=12, text='Restart', command=(lambda e=ents: Ping(e)))
    b4.pack(side=tk.LEFT, 
                 padx=2, 
                 pady=2)
    
    b5 = tk.Button(root, height=2, width=12, text='Health', command=(lambda e=ents: Ping(e)))
    b5.pack(side=tk.LEFT, 
                 padx=2, 
                 pady=2)
    
    b = tk.Button(root, height=2, width=12, text='Quit', command=root.quit)
    b.pack(side=tk.LEFT,
                 padx=2, 
                 pady=2)    
    
    # frame = tk.Frame(root)

    # label = tk.Label(frame, text="test")
    # label.pack(side=tk.LEFT)

    # entry = tk.Entry(frame)
    # entry.pack(side=tk.LEFT)

    # frame.pack()
    
    labelframe = tk.LabelFrame(root, text="Output")
    labelframe.pack(side=tk.BOTTOM, 
                 fill=tk.BOTH, 
                 padx=5, 
                 pady=5)
     
    result = tk.Label(labelframe)
    result.pack(fill=tk.X)
    
    root.mainloop()