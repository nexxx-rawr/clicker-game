import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("1000x760")
points = tk.IntVar(value=0)
multiplier = 1
points_requirment = 50
clicks = tk.IntVar(value=0)
multiplier = tk.IntVar(value=0)

def click():
    clicks.set(clicks.get() + 1)

def show_multiplier():
 mul = tk.Label(Home, text=multiplier, font=("",35,""))
 return mul




def increase():
 global points
 points.set(points.get() + multiplier)
 coins_text.set(f"Coins: {points.get()}")

def create_text(ltext, lfont, lsize, ltext_state,lx,ly,ltab):
 global label
 if isinstance(ltext, tk.Variable):
  label = tk.Label(ltab, textvariable=ltext, font=(lfont, lsize, ltext_state))
 else:
  label = tk.Label(ltab, text=ltext, font=(lfont, lsize, ltext_state))
 label.place(x=lx,y=ly)
 return label

def create_button(btext,bfont,bsize,btext_state,bx,by,btab,command_1):
 global button 
 button = tk.Button(btab, text=btext, font=(bfont,bsize,btext_state), command=command_1, )
 button.place(x=bx,y=by)

def buy_create(text1,text2,font1,font2,size1,size2,text_s1,text_s2,x1,y1,x2,y2,command_2):
 buy_label = tk.Label(Shop, text=text1, font=(font1,size1,text_s1))
 buy_label.place(x=x1,y=y1)
 buy_button = tk.Button(Shop, text=text2, font=(font2,size2,text_s2,), command=lambda: (command_2(), click()))
 buy_button.place(x=x2,y=y2)

coins_text = tk.StringVar(value="Coins: 0")

def buy_01():
 global multiplier
 global points_requirment
 if points.get() >= points_requirment:
  points.set(points.get() - points_requirment)
  multiplier *= 2
  points_requirment *= 2
  coins_text.set(f"Coins: {points.get()}")
  show_multiplier()
 else:
  print("Insufficient Funds!")


notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill="both")

def create_tab(name):
 tab = ttk.Frame(notebook)
 notebook.add(tab, text=name)
 return tab

Home = create_tab("Home")
Shop = create_tab("Shop")
create_text("Clicker GAME", "Onyx", 100, "bold",250, 0, Home)
create_button("Press Me", "Arial", 20, "", 425, 350, Home, lambda: (increase(), click()))
buy_create("MULTIPLIER","BUY ME","Arial","Impact",18,18,"bold","",0,100,170,90,buy_01)
create_text(coins_text, "Arial", 20, "bold", 425, 280, Home)
create_text("SHOP","Onyx",75,"bold",450,0,Shop)
show_multiplier()



tk.mainloop()

