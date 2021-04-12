import tkinter
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root = tkinter.Tk()
root.geometry("500x400")
root.resizable(0,0)
root.title("Library Management System")

topframe = Frame(root,width=500, height=300)  
topframe.pack(side=TOP)
main_logo = ImageTk.PhotoImage(Image.open("front.png").resize((500,200))) 
main_logo__lbl = Label(topframe,image=main_logo)
main_logo__lbl.pack()

bottomframe = Frame(root,width=500, height=50,bg='#104cad')  
bottomframe.pack(side=TOP,expand = True, fill = "both")

def new_game():
    #gv.setrun()
    #root.destroy()
    root.withdraw()
    import pingpong as pp  

def main_menu():
    root.deiconify()
    
play_img = ImageTk.PhotoImage(Image.open("play.png").resize((146,147))) 
play_but = Button(bottomframe,image=play_img,relief=tk.FLAT,bg='#104cad',command=lambda:new_game())
play_but.pack(side=LEFT,padx=(20,0))

score_img = ImageTk.PhotoImage(Image.open("score.png").resize((146,147))) 
score_but = Button(bottomframe,image=score_img,relief=tk.FLAT,bg='#104cad')
score_but.pack(side=LEFT)

ctrl_img = ImageTk.PhotoImage(Image.open("controls.png").resize((146,147))) 
ctrl_but = Button(bottomframe,image=ctrl_img,relief=tk.FLAT,bg='#104cad')
ctrl_but.pack(side=LEFT)

root.mainloop()