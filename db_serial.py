import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import pymysql


class DB_Window:
    def __init__(self, host, user, password, db):
        self.root = tk.Tk()
        self.root.title('Database Inserter')
        self.root.resizable(True, True)
        self.root.configure(bg="white")

        global _host, _user, _pass, _db
        _host = host
        _user = user
        _pass = password
        _db = db

        # ==============================================================================================================

        self.window_height = 641  # 631
        self.window_width = 806

        # ==============================================================================================================

        # Hepsini kapsayan frame
        self.MainFrame = tk.Frame(self.root, bd=10, width=770, height=700, relief=tk.RIDGE, bg="dodger blue")
        self.MainFrame.grid()

        # Sadece başlığın olduğu frame
        self.TitleFrame = tk.Frame(self.MainFrame, bd=7, width=770, height=100, relief=tk.RIDGE, bg="cornflowerblue")
        self.TitleFrame.grid(row=0, column=0)

        # Başlık haricindekiler kapsayan frame
        self.TopFrame3 = tk.Frame(self.MainFrame, bd=5, width=770, height=500, relief=tk.RIDGE, bg="dodger blue")
        self.TopFrame3.grid(row=1, column=0)

        # Entry'lerin ve listenin olduğu yer
        self.LeftFrame = tk.Frame(self.TopFrame3, bd=5, width=770, height=400, padx=2, relief=tk.RIDGE,
                                  bg="dodger blue")
        self.LeftFrame.pack(side=tk.LEFT)
        # Entry'lerin olduğu yer
        self.LeftFrame1 = tk.Frame(self.LeftFrame, bd=5, width=600, height=180, padx=12, pady=9, relief=tk.RIDGE,
                                   bg="cornflowerblue")
        self.LeftFrame1.pack(side=tk.TOP)

        # Butonları kapsayan dış frame
        self.RightFrame1 = tk.Frame(self.TopFrame3, bd=5, width=100, height=400, padx=2, relief=tk.RIDGE,
                                    bg="dodger blue")
        self.RightFrame1.pack(side=tk.RIGHT)
        # Butonları kapsayan iç frame
        self.RightFrame1a = tk.Frame(self.RightFrame1, bd=5, width=90, height=300, padx=2, pady=2, relief=tk.RIDGE,
                                     bg="cornflowerblue")
        self.RightFrame1a.pack(side=tk.TOP)

        # ==============================================================================================================

        self.label_title = tk.Label(self.TitleFrame, font=('arial', 40, 'bold'), text='MYSQL Connection', bd=7,
                                    bg="cornflowerblue")
        self.label_title.grid(row=0, column=0, padx=132)

        self.label_id = tk.Label(self.LeftFrame1, font=('arial', 12, 'bold'), text='ID', bd=7, bg="cornflowerblue")
        self.label_id.grid(row=1, column=0, sticky=tk.W, padx=5)
        self.entry_id = tk.Entry(self.LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=15, justify=tk.LEFT,
                                 state='disabled')
        self.entry_id.grid(row=1, column=1, sticky=tk.W, padx=5)

        self.label_remain = tk.Label(self.LeftFrame1, font=('arial', 12, 'bold'), text='Remain', bd=7,
                                     bg="cornflowerblue")
        self.label_remain.grid(row=1, column=2, sticky=tk.W, padx=5)
        self.entry_remain = tk.Entry(self.LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=15, justify=tk.LEFT)
        self.entry_remain.grid(row=1, column=3, sticky=tk.W, padx=5)

        self.label_name = tk.Label(self.LeftFrame1, font=('arial', 12, 'bold'), text='Name', bd=7, bg="cornflowerblue")
        self.label_name.grid(row=2, column=0, sticky=tk.W, padx=5)
        self.entry_name = tk.Entry(self.LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=15, justify=tk.LEFT)
        self.entry_name.grid(row=2, column=1, sticky=tk.W, padx=5)

        self.label_surname = tk.Label(self.LeftFrame1, font=('arial', 12, 'bold'), text='Surname', bd=7,
                                      bg="cornflowerblue")
        self.label_surname.grid(row=2, column=2, sticky=tk.W, padx=5)
        self.entry_surname = tk.Entry(self.LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=15, justify=tk.LEFT)
        self.entry_surname.grid(row=2, column=3, sticky=tk.W, padx=5)

        self.label_serial_key = tk.Label(self.LeftFrame1, font=('arial', 12, 'bold'), text='Serial key', bd=7,
                                         bg="cornflowerblue")
        self.label_serial_key.grid(row=4, column=0, sticky=tk.W, padx=5)
        self.entry_serial_key = tk.Entry(self.LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify=tk.LEFT)
        self.entry_serial_key.grid(row=4, column=1, sticky=tk.W, padx=5, columnspan=3)

        self.label_client_id = tk.Label(self.LeftFrame1, font=('arial', 12, 'bold'), text='Client ID', bd=7,
                                        bg="cornflowerblue")
        self.label_client_id.grid(row=5, column=0, sticky=tk.W, padx=5)
        self.entry_client_id = tk.Entry(self.LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=15, justify=tk.LEFT)
        self.entry_client_id.grid(row=5, column=1, sticky=tk.W, padx=5)

        self.entry_client_mac = tk.Label(self.LeftFrame1, font=('arial', 12, 'bold'), text='Client MAC', bd=7,
                                         bg="cornflowerblue")
        self.entry_client_mac.grid(row=5, column=2, sticky=tk.W, padx=5)
        self.entry_client_mac = tk.Entry(self.LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=15, justify=tk.LEFT)
        self.entry_client_mac.grid(row=5, column=3, sticky=tk.W, padx=5)

        self.entry_client_ip = tk.Label(self.LeftFrame1, font=('arial', 12, 'bold'), text='Client IP', bd=7,
                                        bg="cornflowerblue")
        self.entry_client_ip.grid(row=7, column=0, sticky=tk.W, padx=5)
        self.entry_client_ip = tk.Entry(self.LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify=tk.LEFT)
        self.entry_client_ip.grid(row=7, column=1, sticky=tk.W, padx=5, columnspan=3)

        # ==============================================================================================================

        self.scroll_y = tk.Scrollbar(self.LeftFrame, orient=tk.VERTICAL)
        self.client_records = ttk.Treeview(self.LeftFrame, height=14, columns=(
            'id', 'name', 'surname', 'serialkey', 'client_id', 'client_mac', 'client_ip', 'is_auth', 'remain'),
                                           xscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.client_records.heading('id', text='id')
        self.client_records.heading('name', text='name')
        self.client_records.heading('surname', text='surname')
        self.client_records.heading('serialkey', text='serialkey')
        self.client_records.heading('client_id', text='client_id')
        self.client_records.heading('client_mac', text='client_mac')
        self.client_records.heading('client_ip', text='client_ip')
        self.client_records.heading('is_auth', text='is_auth')
        self.client_records.heading('remain', text='remain')

        self.client_records['show'] = 'headings'

        self.client_records.column('id', width=20)
        self.client_records.column('name', width=70)
        self.client_records.column('surname', width=70)
        self.client_records.column('serialkey', width=70)
        self.client_records.column('client_id', width=70)
        self.client_records.column('client_mac', width=70)
        self.client_records.column('client_ip', width=70)
        self.client_records.column('is_auth', width=10)
        self.client_records.column('remain', width=10)

        self.client_records.pack(fill=tk.BOTH, expand=1)
        self.client_records.bind("<<TreeviewSelect>>", self.get_item_vals)

        # ==============================================================================================================

        self.button_add = tk.Button(self.RightFrame1a, font=('arial', 16, 'bold'), text='Add New', bd=4, pady=1,
                                    padx=24, width=8,
                                    height=2, command=self.add_record)
        self.button_add.grid(row=0, column=0, padx=1)

        self.button_display = tk.Button(self.RightFrame1a, font=('arial', 16, 'bold'), text='Refresh', bd=4, pady=1,
                                        padx=24,
                                        width=8,
                                        height=2, command=self.display_record)
        self.button_display.grid(row=1, column=0, padx=1)

        self.button_update = tk.Button(self.RightFrame1a, font=('arial', 16, 'bold'), text='Update', bd=4, pady=1,
                                       padx=24,
                                       width=8,
                                       height=2, command=self.update_record)
        self.button_update.grid(row=2, column=0, padx=1)

        self.button_delete = tk.Button(self.RightFrame1a, font=('arial', 16, 'bold'), text='Delete', bd=4, pady=1,
                                       padx=24,
                                       width=8,
                                       height=2, command=self.delete_record)
        self.button_delete.grid(row=3, column=0, padx=1)

        self.button_search = tk.Button(self.RightFrame1a, font=('arial', 16, 'bold'), text='Search', bd=4, pady=1,
                                       padx=24,
                                       width=8,
                                       height=2, command=self.search_record)
        self.button_search.grid(row=4, column=0, padx=1)

        self.button_reset = tk.Button(self.RightFrame1a, font=('arial', 16, 'bold'), text='Reset', bd=4, pady=1,
                                      padx=24, width=8,
                                      height=2, command=self.reset_inputs)
        self.button_reset.grid(row=5, column=0, padx=1)

        self.button_exit = tk.Button(self.RightFrame1a, font=('arial', 16, 'bold'), text='Exit', bd=4, pady=1, padx=24,
                                     width=8,
                                     height=2, command=self.exit_app)
        self.button_exit.grid(row=6, column=0, padx=1)

    # ==================================================================================================================

    def exit_app(self):
        exit_result = tkinter.messagebox.askyesno("Exit", "Confirm if you want to exit")
        if exit_result > 0:
            self.root.destroy()
            return

    def reset_inputs(self):
        self.entry_id.config(state='normal')
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_surname.delete(0, tk.END)
        self.entry_serial_key.delete(0, tk.END)
        self.entry_client_id.delete(0, tk.END)
        self.entry_client_mac.delete(0, tk.END)
        self.entry_client_ip.delete(0, tk.END)
        self.entry_remain.delete(0, tk.END)

    def is_entry_empty(self):
        if self.entry_serial_key.get() == '':
            return True

    def add_record(self):
        if self.is_entry_empty():
            tkinter.messagebox.showerror('Add New', 'Enter Correct Detail')
        else:
            mydb = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                database='indicator'
            )
            mycursor = mydb.cursor()
            sql = "INSERT INTO clients (serialkey, remain) VALUES (%s, %s)"
            mycursor.execute(sql, (self.entry_serial_key.get(), self.entry_remain.get()))
            mydb.commit()
            mydb.close()
            tkinter.messagebox.showinfo('Add New', 'Record entered successfully')
            self.display_record()

    def display_record(self):
        self.entry_id.config(state='disabled')
        mydb = pymysql.connect(
            host=_host,
            user=_user,
            password=_pass,
            database=_db
        )
        mycursor = mydb.cursor()
        sql = "SELECT * FROM clients"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        if len(result) != 0:
            self.client_records.delete(*self.client_records.get_children())
            for row in result:
                self.client_records.insert('', tk.END, values=row)
            mydb.commit()
        mydb.close()

    def update_record(self):
        if self.is_entry_empty():
            tkinter.messagebox.showerror('Update', 'Update')
        else:
            mydb = pymysql.connect(
                host=_host,
                user=_user,
                password=_pass,
                database=_db
            )
            mycursor = mydb.cursor()
            sql = "UPDATE clients SET name=%s, surname=%s, serialkey=%s, client_id=%s, client_mac=%s, client_ip=%s, remain=%s WHERE id=%s"
            val = (
                self.entry_name.get(), self.entry_surname.get(), self.entry_serial_key.get(),
                self.entry_client_id.get(),
                self.entry_client_mac.get(),
                self.entry_client_ip.get(),
                self.entry_remain.get(), self.entry_id.get())
            mycursor.execute(sql, val)
            mydb.commit()
            mydb.close()
            tkinter.messagebox.showinfo('Update', 'Record updated successfully')
            self.display_record()

    def delete_record(self):
        detele_record = tkinter.messagebox.askyesno("Delete", "Confirm if you want to delete record")
        if detele_record > 0:
            mydb = pymysql.connect(
                host=_host,
                user=_user,
                password=_pass,
                database=_db
            )
            mycursor = mydb.cursor()
            sql = "DELETE FROM clients WHERE id=%s"
            val = (self.entry_id.get())
            mycursor.execute(sql, val)
            mydb.commit()
            mydb.close()
            tkinter.messagebox.showinfo('Delete', 'Record deleted successfully')
            self.display_record()

    def search_record(self):
        tkinter.messagebox.showinfo("Search",
                                    "It still under development. If it will be much more record, i will consider again")

    def get_item_vals(self, event):
        self.reset_inputs()

        # selected_item = self.client_records.focus()
        # item = self.client_records.item(selected_item)
        # row = item['values']

        global row
        for selected_item in self.client_records.selection():
            item = self.client_records.item(selected_item)
            row = item['values']

        self.set_text(self.entry_id, row[0])
        self.set_text(self.entry_name, row[1])
        self.set_text(self.entry_surname, row[2])
        self.set_text(self.entry_serial_key, row[3])
        self.set_text(self.entry_client_id, row[4])
        self.set_text(self.entry_client_mac, row[5])
        self.set_text(self.entry_client_ip, row[6])
        # self.set_text(self.is_auth, row[7])
        self.set_text(self.entry_remain, row[8])

        self.entry_id.config(state='disabled')

    def set_text(self, component, text):
        component.delete(0, tk.END)
        component.insert(0, text)
        return

    def center_screen(self, _window_height, _window_width):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (_window_width / 2))
        y_cordinate = int((screen_height / 2) - (_window_height / 2))
        self.root.geometry("{}x{}+{}+{}".format(_window_width, _window_height, x_cordinate, y_cordinate))

    def start(self):
        self.root.mainloop()

# ==================================================================================================================

# self.center_screen(self.root, 641, 806)
# self.display_record()

# mainWindow = DB_Window()
# mainWindow.center_screen(641, 806)
# mainWindow.display_record()
# mainWindow.start()
