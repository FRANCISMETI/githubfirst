import tkinter as tk

root = tk.Tk()
root.title('Calculation')
root.geometry('300x400')

calculation = ''

def add_calculation(symbol):
    global  calculation
    calculation += str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)

def eval_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ''
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0,'Error')

def clear_field():
    global calculation
    calculation = ''
    text_result.delete(1.0, 'end')

def backspace():
   global calculation
   calculation = calculation[:-1]
   text_result.delete(1.0, 'end')
   text_result.insert(1.0, calculation)

def percentage():
    global calculation
    calculation = int(text_result.get(1.0, 'end'))
    calculation /= 100
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)

text_result = tk.Text(root, width=35, height=3, font='arial 14 bold')
text_result.pack(padx=10, pady=60)

btnclear = tk.Button(root, text='C', command = lambda : add_calculation('C'),
                     width=5, font='arial 14')
btnclear.place(x=10, y=120)

btnbackspace = tk.Button(root, text='Back', command =backspace,
                     width=5, font='arial 14')
btnbackspace.place(x=80, y=120)

btnpercent = tk.Button(root, text='%', command = percentage,
                     width=5, font='arial 14')
btnpercent.place(x=150, y=120)

btndiv = tk.Button(root, text='/', command =lambda :add_calculation('/'),
                     width=5, font='arial 14')
btndiv.place(x=220, y=120)

btn7 = tk.Button(root, text='7', command =lambda :add_calculation('7'),
                     width=5, font='arial 14')
btn7.place(x=10, y=170)

btn8 = tk.Button(root, text='8', command =lambda :add_calculation('8'),
                     width=5, font='arial 14')
btn8.place(x=80, y=170)

btn9 = tk.Button(root, text='9', command =lambda :add_calculation('9'),
                     width=5, font='arial 14')
btn9.place(x=150, y=170)

btnmulti = tk.Button(root, text='x', command =lambda :add_calculation('*'),
                     width=5, font='arial 14')
btnmulti.place(x=220, y=170)

btn4 = tk.Button(root, text='4', command =lambda :add_calculation('4'),
                     width=5, font='arial 14')
btn4.place(x=10, y=220)

btn5 = tk.Button(root, text='5', command =lambda :add_calculation('5'),
                     width=5, font='arial 14')
btn5.place(x=80, y=220)

btn6 = tk.Button(root, text='6', command =lambda :add_calculation('6'),
                     width=5, font='arial 14')
btn6.place(x=150, y=220)

btnminus = tk.Button(root, text='-', command =lambda :add_calculation('-'),
                     width=5, font='arial 14')
btnminus.place(x=220, y=220)

btn1 = tk.Button(root, text='1', command =lambda :add_calculation('1'),
                     width=5, font='arial 14')
btn1.place(x=10, y=270)

btn2 = tk.Button(root, text='2', command =lambda :add_calculation('2'),
                     width=5, font='arial 14')
btn2.place(x=80, y=270)

btn3 = tk.Button(root, text='3', command =lambda :add_calculation('3'),
                     width=5, font='arial 14')
btn3.place(x=150, y=270)

btnplus = tk.Button(root, text='+', command =lambda :add_calculation('+'),
                     width=5, font='arial 14')
btnplus.place(x=220, y=270)

btnopen = tk.Button(root, text='(', command =lambda :add_calculation('('),
                     width=2, font='arial 14')
btnopen.place(x=10, y=320)

btnclose = tk.Button(root, text=')', command =lambda :add_calculation(')'),
                     width=2, font='arial 14')
btnclose.place(x=45, y=320)


btn0 = tk.Button(root, text='0', command =lambda :add_calculation('0'),
                     width=5, font='arial 14')
btn0.place(x=80, y=320)

btndot = tk.Button(root, text='.', command =lambda :add_calculation('.'),
                     width=5, font='arial 14')
btndot.place(x=150, y=320)

btnequal = tk.Button(root, text='=', command =eval_calculation,
                     width=5, font='arial 14')
btnequal.place(x=220, y=320)






root.mainloop()