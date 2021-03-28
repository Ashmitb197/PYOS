from tkinter import *

tk = Tk()
tk.overrideredirect(True)
tk.geometry("{0}x{1}+0+0".format(tk.winfo_screenwidth(), tk.winfo_screenheight()))
bg_img = PhotoImage(file = "img\\688202.png")
background_label = Label(tk, image=bg_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def exitbt():
    exit()
shutdown_img = PhotoImage(file = "img\\shut.png")
exit_bt = Button(tk,text = "shutdown", image= shutdown_img,bg = "Red", borderwidth=-1, command = exitbt)
exit_bt.place(x = 30 ,y =700)

def cut():
    print("cut")

m = Menu(tk, tearoff = 0)
m.add_command(label ="Cut", command = cut)
m.add_command(label ="Copy")
m.add_command(label ="Paste")
m.add_command(label ="Exit",command = exitbt)
m.add_separator()
m.add_command(label ="Rename")
  
def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()
  
background_label.bind("<Button-3>", do_popup)






tk.mainloop()
