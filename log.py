import mysql.connector
from tkinter import *

root = Tk()
root.config(bg="black")
root.geometry("500x500")
root.title("Login Page")

class data:
    def __init__(self,master):
        self.log = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='lifechoicesOnline'
                               , auth_plugin='mysql_native_password')

        self.reg_table_btn = Button(master, text="Display Register", command=self.reg_table, bg="black",
                                    highlightbackground="lime", fg="lime")
        self.reg_table_btn.place(x=250, y=250)

    def reg_table(self):
        self.info = self.log.cursor()
        self.info.execute("SELECT * FROM register limit 0,10")
        i = 0
        for self.student in self.info:
            for j in range(len(self.student)):
                self.e = Entry(root, width=10, fg="lime", bg="black", highlightbackground="lime", border=1)
                self.e.grid(row=i, column=j)
                self.e.insert(END, self.student[j])
            i = i+1


app = data(root)
root.mainloop()