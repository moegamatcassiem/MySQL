from tkinter import *
from tkinter import messagebox

root = Tk()
root.config(bg="black")
root.geometry("500x500")
root.title("Login Page")

class log:
    def __init__(self, master):
        self.pass_lab = Label(master, text="Password:", fg="lime", bg="black", font="bold, 15")
        self.pass_lab.place(x=50, y=100)
        self.pass_ent = Entry(master, fg="black", bg="lime", highlightbackground="lime", border=1, width=22)
        self.pass_ent.place(x=160, y=100)

        self.adminLog_btn = Button(master, text="login", bg="black", highlightbackground="lime", fg="lime", command=self.admin_log)
        self.adminLog_btn.place(x=200, y=150)

    def admin_log(self):
        if self.pass_ent.get() == "8-2fermENt2020":
            messagebox.showinfo("Admin", "Access Granted")
            root.destroy()
            import log
        else:
            messagebox.showinfo("Admin", "Access denied")

admin = log(root)
root.mainloop()