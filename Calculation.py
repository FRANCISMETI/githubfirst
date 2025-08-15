import tkinter as tk

def add_calculation(symbol):
    pass

#adding window console
root= tk.Tk()
root.title('Calculation')
root.geometry('310x280')

calculation = ''

#buttons functions reusable code
def add_calculation(symbol):
    global calculation #variable assigned before function
    calculation += str(symbol)                         # store the assigned button in text
    text_result.delete(1.0, 'end')      # delete the index in specified list
    text_result.insert(1.0, calculation)        #insert the index in specified list

def eval_calculation():
    global calculation
    try:                                                       #code that might raise an exception
        result = str(eval(calculation))
        calculation = ''
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, result)
    except:                                                 #code to handle specific
        clear()
        text_result.insert(1.0, 'Error')

def clear():
    global calculation
    calculation = ''
    text_result.delete(1.0, 'end')

text_result = tk.Text(root, width=40, height=2, font='arial 16 bold')
text_result.grid(columnspan=6)

btn1 = tk.Button(root, text='1', command=lambda: add_calculation('1'),width=5, font='arial 14')
btn1.grid(row=3, column=0)

btn2 = tk.Button(root, text='2', command=lambda: add_calculation('2'),width=5, font='arial 14')
btn2.grid(row=3, column=1)

btn3 = tk.Button(root, text='3', command=lambda: add_calculation('3'),width=5, font='arial 14')
btn3.grid(row=3, column=2)

btn4 = tk.Button(root, text='4', command=lambda: add_calculation('4'),width=5, font='arial 14')
btn4.grid(row=4, column=0)

btn5 = tk.Button(root, text='5', command=lambda: add_calculation('5'),width=5, font='arial 14')
btn5.grid(row=4, column=1)

btn6 = tk.Button(root, text='6', command=lambda: add_calculation('6'),width=5, font='arial 14')
btn6.grid(row=4, column=2)

btn7 = tk.Button(root, text='7', command=lambda: add_calculation('7'),width=5, font='arial 14')
btn7.grid(row=5, column=0)

btn8 = tk.Button(root, text='8', command=lambda: add_calculation('8'),width=5, font='arial 14')
btn8.grid(row=5, column=1)

btn9 = tk.Button(root, text='9', command=lambda: add_calculation('9'),width=5, font='arial 14')
btn9.grid(row=5, column=2)

btn0 = tk.Button(root, text='0', command=lambda: add_calculation('0'),width=5, font='arial 14')
btn0.grid(row=6, column=1)

btnplus = tk.Button(root, text='+', command=lambda: add_calculation('+'),width=5, font='arial 14')
btnplus.grid(row=3, column=3)

btnminus = tk.Button(root, text='-', command=lambda: add_calculation('-'),width=5, font='arial 14')
btnminus.grid(row=4, column=3)

btnmult = tk.Button(root, text='*', command=lambda: add_calculation('*'),width=5, font='arial 14')
btnmult.grid(row=5, column=3)

btndiv = tk.Button(root, text='/', command=lambda: add_calculation('/'),width=5, font='arial 14')
btndiv.grid(row=6, column=3)

btnequal = tk.Button(root, text='=', command=eval_calculation,width=5, font='arial 14')
btnequal.grid(row=6, column=2)

btnclear = tk.Button(root, text='C', command=clear,width=5, font='arial 14')
btnclear.grid(row=6, column=0)

root.mainloop()

