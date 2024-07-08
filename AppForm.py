import tkinter as t
from tkinter import ttk

def enter_data():

    accepted = accept_var.get()

    if accepted== "Accepted":

      firstname = first_name_entry.get()
      lastname = last_name_entry.get()
      title= title_combobox.get()
      age = age_spinbox.get()
      nationallity = nation_combobox.get()
      numcourses = numcourse_spinbox.get()
      registrationstatus= reg_status_var.get()

    print("First Name: ", firstname, "Last_Name : ", lastname)
    print("Title:", title, "age: ", age, "NAtionallity:", nationallity)
    print("#courses: ", numcourses)
    print("Registration Status", registrationstatus)
    print("----------------------------------------------")

window = t.Tk()
window.title("Application Form")

frame = t.Frame(window)
frame.pack()

#save user information

user_info_frame = t.LabelFrame(frame, text= "User Infrormation")
user_info_frame.grid(row=0 , column=0, padx=20, pady=10)


first_name_label = t.Label(user_info_frame, text= "First Name")
first_name_label.grid(row=0 , column=0)
last_name_label = t.Label(user_info_frame, text= "Last Name")
last_name_label.grid(row=0 , column=1)

first_name_entry = t.Entry(user_info_frame)
last_name_entry = t.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_lable = t.Label(user_info_frame, text= "Title")
title_combobox = ttk.Combobox(user_info_frame, values=["","Mr","Ms","Mrs"])
title_lable.grid(row=0, column=2)
title_combobox.grid(row=1, column=3)

age_label = t.Label(user_info_frame, text="Age")
age_spinbox = t.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)


nation_label = t.Label(user_info_frame, text= "Nationality")
nation_combobox= ttk.Combobox(user_info_frame, values=['British', 'Indian', 'America'])
nation_label.grid(row=2, column=1)
nation_combobox.grid(row=3, column=1)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


#save Course Info

course_frame = t.Label(frame)
course_frame.grid(row= 1 , column=0, sticky= 'news' , padx=20, pady=10)

register_label = t.Label(course_frame, text= "Registration status")
reg_status_var = t.StringVar(value= "Not Registered")
register_check = t.Checkbutton(course_frame, text = "Currently Registered", 
                               variable =reg_status_var, onvalue="Registered", offvalue="Not Registered")
register_label.grid(row=0, column= 0)
register_check.grid(row=1, column=0)

numcourse_label = t.Label(course_frame, text = '# Completed courses')


numcourse_spinbox = t.Spinbox(course_frame, from_=0, to='infinity')
numcourse_label.grid(row=0, column=1)
numcourse_spinbox.grid(row=1, column=1)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#accept terms

terms_frame = t.LabelFrame(frame, text = "Terms and condition")
terms_frame.grid(row= 2, column=0, sticky='news', padx=20, pady=10)

accept_var=t.StringVar(value="Not Accepted")


term_check = t.Checkbutton(terms_frame, text= "I accept terms and condition"
                           ,variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")

term_check.grid(row=0, column=0)

button = t.Button(frame, text="Save", command=enter_data)
button.grid(row=3 , column=0, sticky='news', padx=20, pady=20)



window.mainloop()
