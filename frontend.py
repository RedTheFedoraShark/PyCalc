import tkinter as tk
import backend
sqrt_symbol = "\u221A"#import symbolu pierwiastka

lastinput=""
result=""

def check_symbol(symbol):
        if symbol in ("+", "-", "*", "/", f"{sqrt_symbol}", "^"):
            return True
        else:
            return False


def show(symbol): #wyswietlanie wprowadzanych danych
    global result
    global lastinput
    if check_symbol(symbol) and check_symbol(lastinput):
        result=result[:-1]
    lastinput=symbol
    result+=str(symbol)
    textfield.delete(1.0,"end")
    textfield.insert(1.0,result)
    
def clear_field(): # czyszczenie okna
    global result
    textfield.delete(1.0,"end")
    result=""
    
def calculate(): # wyswietlanie wyniku
    global result
    result = textfield.get("1.0", "end")
    endresult=backend.magic(result)
    textfield.delete(1.0,"end")
    textfield.insert(1.0,endresult)
    result =endresult


def enter(event): # enter wywoluje funkcje wyzej
    if event.keysym == "Return":
        calculate()


def backspace(event):
    global result
    trimmed = textfield.get(1.0, "end-2c")
    textfield.delete(1.0, "end")
    textfield.insert(1.0, trimmed)
    result = trimmed

window=tk.Tk()                                                  #utworzenie okna
window.geometry("625x410")
window.configure(background='lavenderblush1')
textfield=tk.Text(window,height=2,width=27,font=("Arial",30),bg="lavenderblush1")   #utworzenie pola tekstowego
textfield.grid(columnspan=6)

window.bind("<Return>", enter) # powiązanie entera z wywołaniem funkcji
window.bind("<BackSpace>", backspace)

button_1=tk.Button(window,text="1",command=lambda: show(1),width=5,font=("Arial",30),bg='lavenderblush2')
button_1.grid(row=2,column=1)
button_2=tk.Button(window,text="2",command=lambda: show(2),width=5,font=("Arial",30),bg='lavenderblush2')
button_2.grid(row=2,column=2)
button_3=tk.Button(window,text="3",command=lambda: show(3),width=5,font=("Arial",30),bg='lavenderblush2')
button_3.grid(row=2,column=3)
button_4=tk.Button(window,text="4",command=lambda: show(4),width=5,font=("Arial",30),bg='lavenderblush2')
button_4.grid(row=3,column=1)
button_5=tk.Button(window,text="5",command=lambda: show(5),width=5,font=("Arial",30),bg='lavenderblush2')
button_5.grid(row=3,column=2)
button_6=tk.Button(window,text="6",command=lambda: show(6),width=5,font=("Arial",30),bg='lavenderblush2')
button_6.grid(row=3,column=3)
button_7=tk.Button(window,text="7",command=lambda: show(7),width=5,font=("Arial",30),bg='lavenderblush2')
button_7.grid(row=4,column=1)
button_8=tk.Button(window,text="8",command=lambda: show(8),width=5,font=("Arial",30),bg='lavenderblush2')
button_8.grid(row=4,column=2)
button_9=tk.Button(window,text="9",command=lambda: show(9),width=5,font=("Arial",30),bg='lavenderblush2')
button_9.grid(row=4,column=3)
button_0=tk.Button(window,text="0",command=lambda: show(0),width=5,font=("Arial",30),bg='lavenderblush2')
button_0.grid(row=5,column=2)
button_plus=tk.Button(window,text="+",command=lambda: show("+"),width=5,font=("Arial",30),bg='lavenderblush2')
button_plus.grid(row=2,column=4)
button_minus=tk.Button(window,text="-",command=lambda: show("-"),width=5,font=("Arial",30),bg='lavenderblush2')
button_minus.grid(row=3,column=4)
button_times=tk.Button(window,text="*",command=lambda: show("*"),width=5,font=("Arial",30),bg='lavenderblush2')
button_times.grid(row=4,column=4)
button_div=tk.Button(window,text="/",command=lambda: show("/"),width=5,font=("Arial",30),bg='lavenderblush2')
button_div.grid(row=2,column=5)
button_pow=tk.Button(window,text="^",command=lambda: show("^"),width=5,font=("Arial",30),bg='lavenderblush2')
button_pow.grid(row=3,column=5)
button_sqrt=tk.Button(window,text=f"{sqrt_symbol}",command=lambda: show(f"{sqrt_symbol}"),width=5,font=("Arial",30),bg='lavenderblush2')
button_sqrt.grid(row=4,column=5)
button_eq=tk.Button(window,text="=",command=calculate,width=5,font=("Arial",30),bg='lavenderblush2')
button_eq.grid(row=5,column=5)
button_c=tk.Button(window,text="c",command=clear_field,width=5,font=("Arial",30),bg='lavenderblush2')
button_c.grid(row=5,column=1)
button_bracket_left=tk.Button(window,text="(",command=lambda: show("("),width=5,font=("Arial",30),bg='lavenderblush2')
button_bracket_left.grid(row=5,column=3)
button_bracket_right=tk.Button(window,text=")",command=lambda: show(")"),width=5,font=("Arial",30),bg='lavenderblush2')
button_bracket_right.grid(row=5,column=4)

window.mainloop()
