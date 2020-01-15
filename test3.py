import tkinter
 
root = tkinter.Tk()
 
def color_label(any_label, user_input):
    any_label.configure(text=user_input, bg="green", fg="white")
 
frame1 = tkinter.Frame(root, relief='ridge')
frame3 = tkinter.Frame(root, relief='ridge')
frame2 = tkinter.Frame(root, relief='ridge')
frame4 = tkinter.Frame(root, relief='ridge')
frame5 = tkinter.Frame(root, borderwidth=2, relief='ridge')
frame6 = tkinter.Frame(root, borderwidth=2, relief='ridge')
frame7 = tkinter.Frame(root, borderwidth=2, relief='ridge')
frame8 = tkinter.Frame(root, borderwidth=2, relief='ridge')
frame9 = tkinter.Frame(root, borderwidth=2, relief='ridge')
frame10 = tkinter.Frame(root, borderwidth=2, relief='ridge')
 
frame1.grid(row=0, column=0, sticky="nsew")
frame3.grid(row=0, column=1, sticky="nsew", columnspan=4)
frame2.grid(row=1, column=0, sticky="nsew")
frame4.grid(row=1, column=1, sticky="nsew", columnspan=4)
frame5.grid(row=2, column=0, sticky="nsew")
frame6.grid(row=2, column=1, sticky="nsew")
frame7.grid(row=2, column=2, sticky="nsew")
frame8.grid(row=2, column=3, sticky="nsew")
frame9.grid(row=2, column=4, sticky="nsew")
frame10.grid(row=3, column=0, sticky="nsew", columnspan=5)
 
label1 = tkinter.Label(frame1, text="Host Name")
text1 = tkinter.Entry(frame3)

#button1 = tkinter.Button(frame3, text="Configure button 1", command=lambda: color_label(label1, entry.get()))

label2 = tkinter.Label(frame2, text="Test 1")
text2 = tkinter.Entry(frame4)

#button2 = tkinter.Button(frame4, text="Configure button 2", command=lambda: color_label(label2, entry.get()))

labelframe = tkinter.LabelFrame(frame10,height=10, text="Output")
labelframe.pack(fill='x', 
             padx=5, 
             pady=5)
 
result = tkinter.Label(labelframe,text="test output\n")
result.pack(fill='x')

button = tkinter.Button(frame5, text="Ping", command=lambda: color_label(result, text1.get()))
button1 = tkinter.Button(frame6, text="Start", command=root.destroy)
button2 = tkinter.Button(frame7, text="Shut Down", command=root.destroy)
button3 = tkinter.Button(frame8, text="Restart", command=root.destroy)
button4 = tkinter.Button(frame9, text="Quit", command=root.destroy)
 
#entry = tkinter.Entry(frame6) 
label1.pack(anchor='w', fill='x', expand=tkinter.YES)
label2.pack(anchor='w', fill='x', expand=tkinter.YES)
text1.pack(anchor='w', fill='x', expand=tkinter.YES)
text2.pack(anchor='w', fill='x', expand=tkinter.YES)
# button1.pack(fill='x')
# button2.pack(fill='x')
button.pack(anchor='w', fill='x', expand=tkinter.YES, padx=2, pady=2)
button1.pack(anchor='w', fill='x', expand=tkinter.YES, padx=2, pady=2)
button2.pack(anchor='w', fill='x', expand=tkinter.YES, padx=2, pady=2)
button3.pack(anchor='w', fill='x', expand=tkinter.YES, padx=2, pady=2)
button4.pack(anchor='w', fill='x', expand=tkinter.YES, padx=2, pady=2)
#entry.pack(fill='x')
 
root.mainloop()