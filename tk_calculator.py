import parser
import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Calculator")
topbar=Menu(root)
root.config(menu=topbar)

class Message:
    def new(self,text):
        if text=='new':
            messagebox.showinfo('msg',"This is for new page")
        elif text=='history':
            messagebox.showwarning('msg',"No History available")
    def save(self):
        messagebox.askokcancel('msg',"Do you want to save")
obj=Message()

def display_clear():
    display.delete(0,END)
def display_undo():
    text = display.get()
    if len(text):
        display.delete((len(text) - 1), END)

menu1=Menu(topbar)
topbar.add_cascade(label="File",menu=menu1)
menu1.add_command(label="New",command=lambda :obj.new('new'))
menu1.add_command(label="Save",command=obj.save)
menu1.add_separator()
menu1.add_command(label="History",command=lambda :obj.new('history'))
menu1.add_command(label="Exit",command=exit)

menu2=Menu(topbar)
topbar.add_cascade(label="Edit",menu=menu2)
menu2.add_command(label="Cut")
menu2.add_command(label="Copy")
menu2.add_command(label="Paste")
menu2.add_separator()
menu2.add_command(label="Undo",command=display_undo)
menu2.add_command(label="Clear",command=display_clear)

i=0
def get_input(num):
    global i
    display.insert(i, num)
    i += 1
def get_operators(op):
    global i
    display_text = display.get()
    if len(display_text):
        len_opp = len(op)
        # print(display_text[-len_opp])
        ak = [i for i in range(0, 10) if str(i) == display_text[-1]]
        print("XXXXXXX", ak)
        print("XXX op XXXX", op)
        if ak:
            if str(display_text[-len_opp:]) != str(op):
                display.insert(i, op)
                i += len_opp
        else:
            if not op in ['(',')']:
                display.delete((len(display_text) - len_opp), END)
            display.insert(i, op)
            i += len_opp

def calculate():
    display_text = display.get()
    try:
        if '%' in display_text:
            display_text = display_text.replace('%', '/100')
        compile_text = parser.expr(display_text).compile()
        result = eval(compile_text)
        display_clear()
        display.insert(0, result)
    except Exception as e:
        print("Error------", e)


frame=Frame(root,background="pink")
display=Entry(frame,width=13)
display.config(font=("Arial", 20))
display.grid(row=0,columnspan=10, padx=10, pady=10)
Button(frame,text="%",command=lambda:get_operators('%'),width=5).grid(row=1,column=0,padx=5,pady=5)
Button(frame,text="AC",command=lambda:display_clear(),width=5).grid(row=1,column=1,padx=5,pady=5)
Button(frame,text="exp",command=lambda:get_operators('**'),width=5).grid(row=1,column=2,padx=5,pady=5)
Button(frame,text="<-",command=lambda :display_undo(),width=5).grid(row=1,column=3,padx=5,pady=5)
Button(frame,text="^2",command=lambda:get_operators('**2'),width=5).grid(row=2,column=0,padx=5,pady=5)
Button(frame,text="(",command=lambda:get_operators('('),width=5).grid(row=2,column=1,padx=5,pady=5)
Button(frame,text=")",command=lambda:get_operators(')'),width=5).grid(row=2,column=2,padx=5,pady=5)
Button(frame,text="/",command=lambda:get_operators('/'),width=5).grid(row=2,column=3,padx=5,pady=5)
Button(frame,text="7",command=lambda:get_input(7),width=5).grid(row=3,column=0,padx=5,pady=5)
Button(frame,text="8",command=lambda:get_input(8),width=5).grid(row=3,column=1,padx=5,pady=5)
Button(frame,text="9",command=lambda:get_input(9),width=5).grid(row=3,column=2)
Button(frame,text="*",command=lambda:get_operators('*'),width=5).grid(row=3,column=3,padx=5,pady=5)
Button(frame,text="4",command=lambda:get_input(4),width=5).grid(row=4,column=0,padx=5,pady=5)
Button(frame,text="5",command=lambda:get_input(5),width=5).grid(row=4,column=1,padx=5,pady=5)
Button(frame,text="6",command=lambda:get_input(6),width=5).grid(row=4,column=2,padx=5,pady=5)
Button(frame,text="-",command=lambda:get_operators('-'),width=5).grid(row=4,column=3,padx=5,pady=5)
Button(frame,text="1",command=lambda:get_input(1),width=5).grid(row=5,column=0,padx=5,pady=5)
Button(frame,text="2",command=lambda:get_input(2),width=5).grid(row=5,column=1,padx=5,pady=5)
Button(frame,text="3",command=lambda:get_input(3),width=5).grid(row=5,column=2,padx=5,pady=5)
Button(frame,text="+",command=lambda:get_operators('+'),width=5).grid(row=5,column=3,padx=5,pady=5)
Button(frame,text="!X",width=5).grid(row=6,column=0,padx=5,pady=5)
Button(frame,text=".",command=lambda:get_input("."),width=5).grid(row=6,column=1,padx=10,pady=5)
Button(frame,text="0",command=lambda:get_input(0),width=5).grid(row=6,column=2,padx=5,pady=5)
Button(frame,text="=",command=lambda:calculate(),width=5).grid(row=6,column=3,padx=5,pady=5)

frame.grid()
root.mainloop()
