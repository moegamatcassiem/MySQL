import mysql.connector
from tkinter import *

root = Tk()
root.config(bg="#fff")
root.geometry("500x500")
root.title("login")

log = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='lifechoicesOnline', auth_plugin='mysql_native_password')
mycursor = log.cursor()
xy = mycursor.execute('SELECT * from ')

user_lab = Label(root, text="Enter usernames", bg="#fff", fg="#800", font="arial 15 bold")
user_lab.place(x=10, y=10)

pass_lab = Label(root, text="Enter password", bg="#fff", fg="#800",  font="arial 15 bold")
pass_lab.place(x=10, y=50)

id_num_lab = Label(root, text="Enter ID number", bg="#fff", fg="#800",  font="arial 15 bold")
id_num_lab.place(x=10, y=90)

cell_num_lab = Label(root, text="Enter ID number", bg="#fff", fg="#800",  font="arial 15 bold")
cell_num_lab.place(x=10, y=130)

user_ent = Entry(root, bg="#800", fg="white")
user_ent.place(x=200, y=10)

pass_ent = Entry(root, bg="#800", fg="white")
pass_ent.place(x=200, y=50)

id_num_ent = Entry(root, bg="#800", fg="white")
id_num_ent.place(x=200, y=90)

cell_num_ent = Entry(root, bg="#800", fg="white")
cell_num_ent.place(x=200, y=130)



login_btn = Button(root, text="Login", bg="#fff", fg="#800", highlightbackground="#800")
login_btn.place(x=50, y=200)





root.mainloop()