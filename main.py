import mysql.connector as mysql

from tkinter import *
# from tkinter import messagebox

root = Tk()
root.config(bg="white")
root.geometry("500x500")
root.title("Login Page")

class authorize:
    def __init__(self, master):
        self.log = mysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                database='lifechoicesOnline', auth_plugin='auth_socket')
        self.mycursor = self.log.cursor()
        self.tab = 'SELECT * from register'
        self.xy = self.mycursor.execute(self.tab)
        for i in self.mycursor:
            print(i)



            self.user_lab = Label(master, text="Name:", bg="white", fg="#800", font="bold, 15")
            self.user_lab.place(x=50, y=50)
            self.pass_lab = Label(master, text="Surname:", bg="white", fg="#800", font="bold, 15")
            self.pass_lab.place(x=50, y=100)
            self.cell_num_lab = Label(master, text="Cell Number:", bg="white", fg="#800", font="bold, 15")
            self.cell_num_lab.place(x=50, y=150)
            self.id_num_lab = Label(master, text="ID Number:", bg="white", fg="#800", font="bold, 15")
            self.id_num_lab.place(x=50, y=200)


            self.user_ent = Entry(master, highlightbackground="#800")
            self.user_ent.place(x=250, y=50)
            self.pass_ent = Entry(master, highlightbackground="#800")
            self.pass_ent.place(x=250, y=100)
            self.cell_num_ent = Entry(master, highlightbackground="#800")
            self.cell_num_ent.place(x=250, y=150)
            self.id_num_ent = Entry(master, highlightbackground="#800")
            self.id_num_ent.place(x=250, y=200)

            self.log_btn = Button(master, text="Login", bg="white", background="#800", highlightbackground="#800", fg="#fff")
            self.log_btn.place(x=50, y=250)

            self.register_btn = Button(master, text="Register new user", bg="white", background="#800", highlightbackground="#800", fg="#fff", command="reg")
            self.register_btn.place(x=200, y=250)

    def reg(self):
        self.x = "INSERT INTO register (Name, Surname, ID_number, Phone_number) VALUES (%s, %s, %s, %s)"
        self.y = (self.user_ent.get(), self.pass_ent.get(), self.cell_num_ent.get(), self.id_num_ent.get())
        self.mycursor.execute(self.x, self.y)

        self.log.commit()




app=authorize(root)
root.mainloop()