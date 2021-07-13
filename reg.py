import mysql.connector as mysql
from tkinter import *
from tkinter import messagebox

root = Tk()
root.config(bg="white")
root.geometry("500x500")
root.title("Login Page")

class register:
    def __init__(self, master):

        self.regis = mysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                database='lifechoicesOnline', auth_plugin='mysql_native_password')
        self.mycursor = self.regis.cursor()
        self.tab = 'SELECT * from register'
        self.xy = self.mycursor.execute(self.tab)
        for i in self.mycursor:
            print(i)

        # register
        self.reg_title = Label(master, text="Register", bg="white", fg="#800", font="bold, 20")
        self.reg_title.place(x=200, y=190)
        self.user_lab = Label(master, text="Name:", bg="white", fg="#800", font="bold, 15")
        self.user_lab.place(x=50, y=230)
        self.pass_lab = Label(master, text="Surname:", bg="white", fg="#800", font="bold, 15")
        self.pass_lab.place(x=50, y=270)
        self.cell_num_lab = Label(master, text="Cell Number:", bg="white", fg="#800", font="bold, 15")
        self.cell_num_lab.place(x=50, y=310)
        self.id_num_lab = Label(master, text="ID Number:", bg="white", fg="#800", font="bold, 15")
        self.id_num_lab.place(x=50, y=350)


        self.user_ent = Entry(master, highlightbackground="#800")
        self.user_ent.place(x=250, y=230)
        self.pass_ent = Entry(master, highlightbackground="#800")
        self.pass_ent.place(x=250, y=270)
        self.cell_num_ent = Entry(master, highlightbackground="#800")
        self.cell_num_ent.place(x=250, y=310)
        self.id_num_ent = Entry(master, highlightbackground="#800")
        self.id_num_ent.place(x=250, y=350)

        self.reg_btn = Button(master, text="Register as new user", bg="white", background="#800", highlightbackground="#800", fg="#fff", command=self.reg)
        self.reg_btn.place(x=170, y=390)

        # login
        self.log_title = Label(master, text="Login", bg="white", fg="#800", font="bold, 20")
        self.log_title.place(x=200, y=10)
        self.name_lab = Label(master, text="Name:", bg="white", fg="#800", font="bold, 15")
        self.name_lab.place(x=50, y=50)
        self.surname_lab = Label(master, text="Surname:", bg="white", fg="#800", font="bold, 15")
        self.surname_lab.place(x=50, y=90)

        self.name_ent = Entry(master, fg="#800", highlightbackground="#800")
        self.name_ent.place(x=250, y=50)
        self.surname_ent = Entry(master, fg="#800", highlightbackground="#800")
        self.surname_ent.place(x=250, y=90)

        self.log_btn = Button(master, text="Login", bg="#800", highlightbackground="#800", fg="white", command=self.log)
        self.log_btn.place(x=220, y=130)

        # admin
        self.admin_btn = Button(master, text="Admin login", bg="#800", highlightbackground="#800", fg="white", command=self.admin)
        self.admin_btn.place(x=200, y=450)

        # functions
    def log(self):
            self.ab = self.mycursor.execute('SELECT * from register')
            self.a = "INSERT INTO login (name, surname) VALUES (%s, %s)"
            self.b = (self.user_ent.get(), self.surname_ent.get())
            self.mycursor.execute(self.a, self.b)

    def reg(self):
        self.x = "INSERT INTO register (name, surname, ID_number, cell_number) VALUES (%s, %s, %s, %s)"
        self.y = (self.user_ent.get(), self.pass_ent.get(), self.cell_num_ent.get(), self.id_num_ent.get())
        self.mycursor.execute(self.x, self.y)
        self.regis.commit()


    def admin(self):
        root.destroy()
        import admin_log

app=register(root)
root.mainloop()