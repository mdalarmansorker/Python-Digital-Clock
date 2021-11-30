import tkinter  as tk 
from tkinter import ttk
my_w = tk.Tk()
my_w.geometry("405x300")  
from time import strftime
def my_time():
    time_string = strftime('%H:%M:%S %p \n %A \n %d %B , %Y') # time format 
    l1.config(text="Software Development Project I\nMD AL ARMAN SORKER\nBAUST - CSE - 10th Batch\nID - 200101059\n"+time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
	
my_font=('times',20,'bold') # display size and style

l1=tk.Label(my_w,font=my_font,bg='White')
l1.grid(row=1,column=1,padx=5,pady=25)

my_time()
my_w.mainloop()