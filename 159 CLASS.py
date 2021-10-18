from tkinter import*

root = Tk()
root.geometry = ("600x400")

list_name = ["Mickey mouse", "Elsa", "Anna", "Donald Duck"]
dict_student = {"name: Swasti",
                "age:12"  }
try:
    
    print(list_name[5])
    print(dict_student["mom"])
    
except IndexError :
       messagebox.showinfo("Error","Fool go and check your code") 
except KeyError :
       messagebox.showinfo("Error","Fool go and check your code")    
       
       root.mainloop()

"""
Created on Mon Oct 18 14:17:19 2021

@author: Admin

"""