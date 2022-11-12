import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string
import pymysql
import db_serial


class Gen_Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Database Inserter')
        self.root.resizable(True, True)
        self.root.configure(bg="white")

        # self.window_height = 600
        # self.window_width = 310

        self.radioSelected = tk.IntVar()
        self.radioSelected.set(2)

        self.var_lower = tk.IntVar()
        self.var_upper = tk.IntVar()
        self.var_num = tk.IntVar()
        self.var_symbols = tk.IntVar()
        self.serial_vars = []

        # ==============================================================================================================

        self.labelId = tk.Label(self.root, bg='white', text="id: ")
        self.labelId.place(x=20, y=20)

        self.labelVersion = tk.Label(self.root, bg='white', foreground="red", text="unregistered")
        self.labelVersion.place(x=120, y=20)

        self.labelTitle = tk.Label(self.root, bg='white', font=14, text="Serial Key Generator Into Database")
        self.labelTitle.place(x=20, y=55)

        self.frame_database = tk.LabelFrame(self.root, bg='white', text='Enter Database Info', width=270, height=175)
        self.frame_database.place(x=20, y=90)

        self.label_db_host = tk.Label(self.frame_database, bg='white', text='host: ')
        self.label_db_host.place(x=20, y=20)

        self.entry_db_host = tk.Entry(self.frame_database, highlightcolor="SteelBlue3", highlightthickness=2, width=20)
        self.entry_db_host.place(x=100, y=20)

        self.label_db_user = tk.Label(self.frame_database, bg='white', text='user: ')
        self.label_db_user.place(x=20, y=50)

        self.entry_db_user = tk.Entry(self.frame_database, highlightcolor="SteelBlue3", highlightthickness=2, width=20)
        self.entry_db_user.place(x=100, y=50)

        self.label_db_password = tk.Label(self.frame_database, bg='white', text='password: ')
        self.label_db_password.place(x=20, y=80)

        self.entry_db_password = tk.Entry(self.frame_database, highlightcolor="SteelBlue3", highlightthickness=2,
                                          width=20)
        self.entry_db_password.place(x=100, y=80)

        self.label_db_database = tk.Label(self.frame_database, bg='white', text='database: ')
        self.label_db_database.place(x=20, y=110)

        self.entry_db_database = tk.Entry(self.frame_database, highlightcolor="SteelBlue3", highlightthickness=2,
                                          width=20)
        self.entry_db_database.place(x=100, y=110)

        # ==============================================================================================================

        self.sep1 = ttk.Separator()
        self.sep1.place(x=20, y=280, width=270)

        # ==============================================================================================================

        self.frame_option = tk.LabelFrame(self.root, bg='white', text='Choose', width=270, height=200)
        self.frame_option.place(x=20, y=300)

        self.label_pass_lenght = tk.Label(self.frame_option, bg='white', text='Password Lenght: ')
        self.label_pass_lenght.place(x=20, y=20)

        # ==============================================================================================================

        self.spin_pass_lenght = tk.Spinbox(self.frame_option, highlightcolor="SteelBlue3", highlightthickness=2,
                                           from_=1, to=100,
                                           width=5, increment=1)
        self.spin_pass_lenght.place(x=120, y=20)
        self.spin_pass_lenght.insert(1, '')

        self.label_insert_count = tk.Label(self.frame_option, bg='white', text='Insert count: ')
        self.label_insert_count.place(x=20, y=60)

        self.spin_insert_count = tk.Spinbox(self.frame_option, highlightcolor="SteelBlue3", highlightthickness=2,
                                            from_=1, to=100,
                                            width=5, increment=1)
        self.spin_insert_count.place(x=120, y=60)
        self.spin_insert_count.insert(1, '')

        # ==============================================================================================================

        self.checkbutton_lower = tk.Checkbutton(self.frame_option, bg='white', text='lower', variable=self.var_lower,
                                                onvalue=1,
                                                offvalue=0)
        self.checkbutton_lower.place(x=20, y=100)

        self.checkbutton_upper = tk.Checkbutton(self.frame_option, bg='white', text='upper', variable=self.var_upper,
                                                onvalue=1,
                                                offvalue=0)
        self.checkbutton_upper.place(x=120, y=100)

        self.checkbutton_num = tk.Checkbutton(self.frame_option, bg='white', text='num', variable=self.var_num,
                                              onvalue=1, offvalue=0)
        self.checkbutton_num.place(x=20, y=140)

        self.checkbutton_symbols = tk.Checkbutton(self.frame_option, bg='white', text='symbols',
                                                  variable=self.var_symbols, onvalue=1,
                                                  offvalue=0)
        self.checkbutton_symbols.place(x=120, y=140)

        # ==============================================================================================================

        self.labelInfo = tk.Label(self.root, bg='white', text="")
        self.labelInfo.place(x=110, y=510)

        # ==============================================================================================================

        self.photoPurchase = tk.PhotoImage(file=r"img\pricing.png")
        self.photoPurchaseImage = self.photoPurchase.subsample(4, 4)

        self.purchasebutton = tk.Button(self.root, text='GET', bg='white', image=self.photoPurchaseImage,
                                        compound='left',
                                        command=self.get_data)
        self.purchasebutton.place(x=220, y=15, width=70)

        self.photoGet = tk.PhotoImage(file=r"img\get.png")
        self.photoGetImage = self.photoGet.subsample(3, 3)

        self.fetchbutton = tk.Button(self.root, text='INSERT', image=self.photoGetImage, compound='left',
                                     font=('Times', 12),
                                     fg='white',
                                     padx=1,
                                     pady=3, bg='SteelBlue3',
                                     activebackground='cornflower blue', activeforeground='black',
                                     command=self.generate)
        self.fetchbutton.place(x=40, y=550, width=100)

        self.photoReset = tk.PhotoImage(file=r"img\clear-symbol.png")
        self.photoResetImage = self.photoReset.subsample(3, 3)

        self.resetbutton = tk.Button(self.root, text='RESET', image=self.photoResetImage, compound='left',
                                     font=('Times', 12),
                                     fg='white',
                                     padx=10,
                                     pady=3, bg='SteelBlue3',
                                     activebackground='cornflower blue', activeforeground='black',
                                     command=self.reset_inputs)
        self.resetbutton.place(x=150, y=550, width=100)

        # ==============================================================================================================

        self.set_text(self.entry_db_host, 'localhost')
        self.set_text(self.entry_db_user, 'root')
        self.set_text(self.entry_db_database, 'indicator')

    # ==================================================================================================================

    def set_text(self, component, text):
        component.delete(0, tk.END)
        component.insert(0, text)
        return

    def generate(self):
        length = int(self.spin_pass_lenght.get())
        count = int(self.spin_insert_count.get())
        db_host = self.entry_db_host.get()
        db_user = self.entry_db_user.get()
        db_pass = self.entry_db_password.get()
        db_name = self.entry_db_database.get()

        lower = tk.StringVar()
        upper = tk.StringVar()
        num = tk.StringVar()
        symbols = tk.StringVar()

        if self.var_lower.get() == 1:
            lower = string.ascii_lowercase
        else:
            lower = ""

        if self.var_upper.get() == 1:
            upper = string.ascii_uppercase
        else:
            upper = ""

        if self.var_num.get() == 1:
            num = string.digits
        else:
            num = ""

        if self.var_symbols.get() == 1:
            symbols = string.punctuation
        else:
            symbols = ""

        if db_host != '' or db_user != '' or db_name != '':
            mydb = pymysql.connect(
                host=db_host,
                user=db_user,
                password=db_pass,
                database=db_name
            )

            mycursor = mydb.cursor()

            mycursor.execute(
                "CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY AUTO_INCREMENT, name TEXT, surname TEXT, "
                "serialkey TEXT NOT NULL, client_id INTEGER, client_mac TEXT, client_ip TEXT, is_auth TINYINT(4) NOT "
                "NULL, remain TINYINT(4) NOT NULL)")

            mydb.commit()

            all_in_one = lower + upper + num + symbols
            if all_in_one != '':
                for i in range(0, count):
                    temp = random.choices(all_in_one, k=length)
                    password = "".join(temp)
                    self.serial_vars.append(password)
                    sql = "INSERT INTO clients (serialkey) VALUES (%s)"
                    mycursor.execute(sql, (str(password),))

                mydb.commit()
                mydb.close()
                result = "{} tane eklendi".format(len(self.serial_vars))
                messagebox.showinfo("Result", result)

    def reset_inputs(self):
        self.entry_db_host.delete(0, 'end')
        self.entry_db_host.focus_set()
        self.entry_db_user.delete(0, 'end')
        self.entry_db_password.delete(0, 'end')
        self.entry_db_database.delete(0, 'end')
        self.spin_pass_lenght.delete(0, "end")
        self.spin_pass_lenght.insert(0, "1")
        self.spin_insert_count.delete(0, "end")
        self.spin_insert_count.insert(0, "1")
        self.checkbutton_lower.deselect()
        self.checkbutton_upper.deselect()
        self.checkbutton_num.deselect()
        self.checkbutton_symbols.deselect()
        self.labelInfo.config(text="")

    def center_screen(self, _window_height, _window_width):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (_window_width / 2))
        y_cordinate = int((screen_height / 2) - (_window_height / 2))
        self.root.geometry("{}x{}+{}+{}".format(_window_width, _window_height, x_cordinate, y_cordinate))

    def start(self):
        self.root.mainloop()

    def get_data(self):
        if self.entry_db_host.get() != '' and self.entry_db_user.get() != '' and self.entry_db_database.get() != '':
            secWindow = db_serial.DB_Window(self.entry_db_host.get(), self.entry_db_user.get(),
                                            self.entry_db_password.get(), self.entry_db_database.get())
            secWindow.center_screen(641, 806)
            secWindow.display_record()
            secWindow.start()


# ======================================================================================================================

mainWindow = Gen_Window()
mainWindow.center_screen(600, 310)
mainWindow.start()
