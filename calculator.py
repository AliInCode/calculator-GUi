from tkinter import *
import tkinter.messagebox


#=============================== Setting =======================================
root = Tk()
root.geometry('400x200')
root.title('Calculator')
root.resizable(width=False, height = False)
color = 'gray'
root.configure(bg=color)
#=============================== varibles =======================================
number_First = StringVar()
number_Second = StringVar()
result_value = StringVar()
#=============================== Frames =======================================
top_first = Frame(root, width =400, height = 60,bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width =400, height = 60,bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width =400, height = 60,bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width =400, height = 60,bg=color)
top_forth.pack(side=TOP)
#=============================== Functions =======================================
def errorMsg(ms):
    if ms=='error':
        tkinter.messagebox.showerror('Error','somthing wnet wrong')
    elif ms == "divisons zero error":
        tkinter.messagebox.showerror('Divisions Error', 'Can Not Divide By 0')

def plus():
    try:
        value = float(number_First.get()) + float(number_Second.get())
        result_value.set(value)
    except:
        errorMsg('error')
def minus():
    try:
        value = float(number_First.get()) - float(number_Second.get())
        result_value.set(value)
    except:
        errorMsg('error')
def mul():
    try:
        value = float(number_First.get()) * float(number_Second.get())
        result_value.set(value)
    except:
        errorMsg('error')
def div():
    if number_Second.get()== '0':
        errorMsg('divisons zero error')
    elif number_Second.get() != "0":
        try:
            value = float(number_First.get()) / float(number_Second.get())
            result_value.set(value)
        except:
            errorMsg('error')
        

#=============================== Buttons =======================================

btn_plus = Button(top_third, text ="+", width=10,
                  highlightbackground=color , command= lambda: plus())
btn_plus.pack(side=LEFT, padx=10,pady=10)

btn_minus = Button(top_third, text ="-", width=10,
                   highlightbackground=color,command= lambda: minus())
btn_minus.pack(side=LEFT, padx=10,pady=10)

btn_mul = Button(top_third, text ="*", width=10,
                 highlightbackground=color,command= lambda: mul())
btn_mul.pack(side=LEFT, padx=10,pady=10)

btn_div = Button(top_third, text ="/", width=10,
                 highlightbackground=color,command= lambda: div() )
btn_div.pack(side=LEFT, padx=10,pady=10)

#=============================== Entries and Labels =======================================
labal_first = Label(top_first, text ="Input Number 1: ", bg=color)
labal_first.pack(side=LEFT, pady=10,padx=10)


first_number = Entry(top_first,highlightbackground=color, textvariable= number_First)
first_number.pack(side=LEFT)

labal_second = Label(top_second, text ="Input Number 2: ", bg=color)
labal_second.pack(side=LEFT, pady=10,padx=10)


second_number = Entry(top_second, highlightbackground=color,textvariable= number_Second )
second_number.pack(side=LEFT)

result = Label(top_forth, text ="Reault: ", bg=color)
result.pack(side=LEFT, pady=10,padx=10)


result_Number = Entry(top_forth, highlightbackground=color,textvariable= result_value)
result_Number.pack(side=LEFT)

 


root.mainloop()