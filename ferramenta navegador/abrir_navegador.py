import webbrowser
import tkinter as tk

obj_tk = tk.Tk( )

obj_tk.title("Abrir o navegador")
obj_tk.geometry("300x200")

def browser():
    webbrowser.open("www.google.com.br")

btn = tk.Button(obj_tk,text="Abrir o Edge",command=browser).pack(pady=20)
obj_tk.mainloop()