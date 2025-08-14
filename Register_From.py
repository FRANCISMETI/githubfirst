import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Registration Form')
root.geometry('500x370')
root.resizable(False,False)

def enter_data():
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    title = title_combo.get()
    age = age_spin.get()
    nationality = nationality_combo.get()
    register = regi_var.get()
    numcourse = numcourse_spin.get()
    numsem = numsem_spin.get()
    accept = accept_var.get()

    print (firstname, lastname, title, age, nationality, register, numcourse, numsem, accept)

    with open(firstname+'.text', 'w')as f:
        f.write('Firstname: '+firstname+'\n')
        f.write('Lastname: ' + lastname +'\n')
        f.write('Title: ' + title+ '\n')
        f.write('Age: ' + age+'\n')
        f.write('Nationality: ' + nationality+'\n')
        f.write('Register: ' + register+'\n')
        f.write('Number of Coursers: ' + numcourse+ '\n')
        f.write('Number of Semesters: ' + numsem+ '\n')
        f.write('Accept Terms & Conditions: ' + accept+ '\n')



frame = tk.Frame(root)
frame.pack()


#user info
user_info = tk.LabelFrame(frame, text='user info')
user_info.grid(row=0, column=0)

firstname = tk.Label(user_info, text='First Name')
firstname.grid(row=0, column=0)
firstname_entry = tk.Entry(user_info, bd=2)
firstname_entry.grid(row=1, column=0)


lastname = tk.Label(user_info, text='Last Name')
lastname.grid(row=0, column=1)
lastname_entry = tk.Entry(user_info, bd=2)
lastname_entry.grid(row=1, column=1)

title = tk.Label(user_info, text='title')
title.grid(row=0, column=2)
title_combo = ttk.Combobox(user_info, values=['Mr.', 'Ms.', 'Dr.'])
title_combo.grid(row=1, column=2)

age = tk.Label(user_info, text='Age')
age.grid(row=2, column=0)
age_spin = tk.Spinbox(user_info, from_=18, to=60, bd=2)
age_spin.grid(row=3, column=0)

nationality = tk.Label(user_info, text='Nationality')
nationality.grid(row=2, column=1)
nationality_combo = ttk.Combobox(user_info, values=['India', 'US', 'UAE', 'UK', 'China', 'Russia'])
nationality_combo.grid(row=3, column=1)

for widget in user_info.winfo_children():
    widget.grid(padx=10, pady=5)

#register info
Register = tk.LabelFrame(frame, text='Register')
Register.grid(row=1, column=0, sticky='news')

register_label = tk.Label(Register, text='Registration')
register_label.grid(row=0, column=0)
regi_var = tk.StringVar(value='not Registered')
register_check = tk.Checkbutton(Register, text='Click For Register', variable=regi_var, onvalue='Registered',
                                offvalue='not Registered')
register_check.grid(row=1, column=0)

numcourse = tk.Label(Register, text='Number of Courses Completed')
numcourse.grid(row=0, column=1)
numcourse_spin = tk.Spinbox(Register, from_=0, to=10)
numcourse_spin.grid(row=1, column=1)

numsem = tk.Label(Register, text='Number Of Semesters')
numsem.grid(row=0, column=2)
numsem_spin = tk.Spinbox(Register, from_=0, to=10)
numsem_spin.grid(row=1, column=2)

for widget in Register.winfo_children():
    widget.grid(padx=10, pady=5)

#accept terms & conditions
accept = tk.LabelFrame(frame, text='Terms & Conditions')
accept.grid(row=2, column=0, sticky='news', padx=20, pady=20)

accept_var = tk.StringVar(value='not accepted')
accept_check = tk.Checkbutton(accept, text='Accept Terms & Condition', variable=accept_var, onvalue='Accepted',
                              offvalue='not accepted')
accept_check.grid(row=0, column=0)

button = tk.Button(frame, text='Enter Data', command=enter_data)
button.grid(row=3, column=0, sticky='news', padx=20, pady=20)

root.mainloop()

