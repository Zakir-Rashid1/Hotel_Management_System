import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox


class Customer_wind:  
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Details")
        self.root.geometry("1240x610+230+270")

        ############ Variables ###############
        self.var_ref = tk.StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_custname = tk.StringVar()
        self.var_mother = tk.StringVar()
        self.var_gender = tk.StringVar()
        self.var_post = tk.StringVar()
        self.var_mobile = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_nationality = tk.StringVar()
        self.var_idproof = tk.StringVar()
        self.var_idnumber = tk.StringVar()
        self.var_address = tk.StringVar()


        ################ Title ###########################
        lbl_title = tk.Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black",fg="gold")
        lbl_title.place(x=0, y=0, width=1240, height=50) 


        ################ Logo ###########################
        img2 = Image.open("./images/logohotel.png")
        img2 = img2.resize((100, 40))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbling = tk.Label(self.root, image=self.photoimg2, bd=0, relief="ridge")
        lbling.place(x=5, y=2, width=100, height=40)

        ################ Label Frame ####################
        labelframeleft = tk.LabelFrame(self.root, bd=2, relief="ridge", text="Customer Details", padx=2, pady=10, font=("times new roman", 14, "bold"))
        labelframeleft.place(x=5, y=55, width=425, height=490)

        # Cust Ref
        cusref = tk.Label(labelframeleft, text="Customer Ref", font=("arial", 12, "bold"), padx=2, pady=6)
        cusref.grid(row=0, column=0, sticky="w")
        txtcusref = ttk.Entry(labelframeleft, textvariable=self.var_ref, width=29, font=("arial", 13, "bold"), state="readonly")
        txtcusref.grid(row=0, column=1)

        # Cust Name
        cname = tk.Label(labelframeleft, text="Customer Name", font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky="w")
        textcname = ttk.Entry(labelframeleft, textvariable=self.var_custname, width=29, font=("arial", 13, "bold"))
        textcname.grid(row=1, column=1)

        # Mother Name
        lblmname = tk.Label(labelframeleft, text="Mother Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky="w")
        textmname = ttk.Entry(labelframeleft, textvariable=self.var_mother, width=29, font=("arial", 13, "bold"))
        textmname.grid(row=2, column=1)

        # Gender Combobox
        label_gender = tk.Label(labelframeleft, text="Gender", font=("arial", 12, "bold"), padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky="w")
        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_gender, font=("arial", 13, "bold"), width=27, state="readonly")
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # Postal Code
        lblpostcode = tk.Label(labelframeleft,text="Postal Code", font=("arial", 12, "bold"), padx=2, pady=6)
        lblpostcode.grid(row=4, column=0, sticky="w")
        txtpostcode = ttk.Entry(labelframeleft,textvariable=self.var_post, width=29, font=("arial", 13, "bold"))
        txtpostcode.grid(row=4, column=1)

        # Mobile Number
        lblmobile = tk.Label(labelframeleft,text="Mobile Number", font=("arial", 12, "bold"), padx=2, pady=6)
        lblmobile.grid(row=5, column=0, sticky="w")
        txtmobile = ttk.Entry(labelframeleft,textvariable=self.var_mobile, width=29, font=("arial", 13, "bold"))
        txtmobile.grid(row=5, column=1)

        # Email ID
        lblemail = tk.Label(labelframeleft, text="Email ID", font=("arial", 12, "bold"), padx=2, pady=6)
        lblemail.grid(row=6, column=0, sticky="w")
        txtemail = ttk.Entry(labelframeleft,textvariable=self.var_email, width=29, font=("arial", 13, "bold"))
        txtemail.grid(row=6, column=1)

        # Nationality
        lblnationality = tk.Label(labelframeleft, text="Nationality", font=("arial", 12, "bold"), padx=2, pady=6)
        lblnationality.grid(row=7, column=0, sticky="w")
        combo_nationality = ttk.Combobox(labelframeleft,textvariable=self.var_nationality, font=("arial", 13, "bold"), width=27, state="readonly")
        combo_nationality['values'] = ("Kashmiri", "Afgani", "Palesteni")
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)


        # ID Type Combo Box
        lblidproof = tk.Label(labelframeleft, text="Id Proof Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lblidproof.grid(row=8, column=0, sticky="w")
        combo_id = ttk.Combobox(labelframeleft,textvariable=self.var_idproof, font=("arial", 13, "bold"), width=27, state="readonly")
        combo_id['values'] = ("Aadhar Card", "Driving Licence", "Passport")
        combo_id.current(0)
        combo_id.grid(row=8, column=1)


        # ID Number
        lblidnumber = tk.Label(labelframeleft, text="Id Number", font=("arial", 12, "bold"), padx=2, pady=6)
        lblidnumber.grid(row=9, column=0, sticky="w")
        txtidnumber = ttk.Entry(labelframeleft,textvariable=self.var_idnumber, width=29, font=("arial", 13, "bold"))
        txtidnumber.grid(row=9, column=1)


        # Address
        lbladdress = tk.Label(labelframeleft, text="Address", font=("arial", 12, "bold"), padx=2, pady=6)
        lbladdress.grid(row=10, column=0, sticky="w")
        txtaddress = ttk.Entry(labelframeleft, textvariable=self.var_address, width=29, font=("arial", 13, "bold"))
        txtaddress.grid(row=10, column=1)

        ################ Btns ##########################
        btn_frame = tk.Frame(labelframeleft, bd=2, relief="ridge", bg="black")
        btn_frame.place(x=0, y=350, width=418, height=40)

        btnadd = tk.Button(btn_frame, command=self.add_data, font=("arial", 11, "bold"), text="Add", fg="black", width=9, height=2)
        btnadd.grid(row=0, column=0, padx=2)

        btnupdate = tk.Button(btn_frame, command=self.update, font=("arial", 11, "bold"), text="Update", fg="black", width=9, height=2)
        btnupdate.grid(row=0, column=1, padx=2)

        btndelete = tk.Button(btn_frame, command=self.delete, font=("arial", 11, "bold"), text="Delete", fg="black", width=9, height=2)
        btndelete.grid(row=0, column=2, padx=2)

        btnreset = tk.Button(btn_frame, command=self.reset, font=("arial", 11, "bold"), text="Reset", fg="black", width=9, height=2)
        btnreset.grid(row=0, column=3, padx=2)


        ################# Table Frame ################################
        table_frame = tk.LabelFrame(self.root, bd=2, relief="ridge", text="View Details And Search System", padx=2, pady=10, font=("times new roman", 14, "bold"))
        table_frame.place(x=435, y=55, width=803, height=490)

        lblsearchby = tk.Label(table_frame, text="Search By: ", font=("arial", 13, "bold"), bg="red", fg="black")
        lblsearchby.grid(row=0, column=0, sticky="w", padx=3)

        self.search_var = tk.StringVar()
        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, values=["mobile", "ref"], font=("arial", 13, "bold"), width=24, state="readonly")
        # combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=3)


        self.txt_search = tk.StringVar()
        txtsearch = ttk.Entry(table_frame, textvariable=self.txt_search, width=24, font=("arial", 13, "bold"))
        txtsearch.grid(row=0, column=2, padx=3)


        btnsearch = tk.Button(table_frame, command=self.search_data, font=("arial", 11, "bold"), text="Search", fg="black", height=2)
        btnsearch.grid(row=0, column=3, padx=3)

        btnshowall = tk.Button(table_frame, command=self.fetch_data, font=("arial", 11, "bold"), text="Show All", fg="black", height=2)
        btnshowall.grid(row=0, column=4, padx=3)

        ################## Show Data Table ##################
        details_table = tk.Frame(table_frame, bd=2, relief="ridge")  
        details_table.place(x=0, y=55, width=795, height=403)

        scroll_x = ttk.Scrollbar(details_table, orient="horizontal")
        scroll_y = ttk.Scrollbar(details_table, orient="vertical")

        self.cust_details_table = ttk.Treeview(details_table, column=("ref", "name", "custmother", "gender", "post", "mobile",
                                                                       "email", "nationality", "idproof", "idnumber", "address"),
                                                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")
        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("ref", text="Refer No")
        self.cust_details_table.heading("name", text="Name")
        self.cust_details_table.heading("custmother", text="Mother's Name")
        self.cust_details_table.heading("gender", text="Selecr Gender")
        self.cust_details_table.heading("post", text="Postal Code")
        self.cust_details_table.heading("mobile", text="Mobile Number")
        self.cust_details_table.heading("email", text="Email")
        self.cust_details_table.heading("nationality", text="Nationality")
        self.cust_details_table.heading("idproof", text="ID Proof")
        self.cust_details_table.heading("idnumber", text="ID Number")
        self.cust_details_table.heading("address", text="Address")

        self.cust_details_table["show"] = "headings"

        self.cust_details_table.column("ref", width=100)
        self.cust_details_table.column("name", width=100)
        self.cust_details_table.column("custmother", width=100)
        self.cust_details_table.column("gender", width=100)
        self.cust_details_table.column("post", width=100)
        self.cust_details_table.column("mobile", width=100)
        self.cust_details_table.column("email", width=100)
        self.cust_details_table.column("nationality", width=100)
        self.cust_details_table.column("idproof", width=100)
        self.cust_details_table.column("idnumber", width=100)
        self.cust_details_table.column("address", width=100)

        self.cust_details_table.pack(fill="both", expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()




    # ***************** Add Data To DataBase **********************
    def add_data(self):
        if not self.var_mobile.get() or not self.var_mother.get():
            messagebox.showerror(title="error", message="Can't Left Blank")
        else:
            try:
                conn = mysql.connector.connect(host="127.0.0.1", username="root", password="passwordxx", database="Customers")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into CUSTOMER values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                        self.var_ref.get(),
                                                                        self.var_custname.get(),
                                                                        self.var_mother.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_post.get(),
                                                                        self.var_mobile.get(),
                                                                        self.var_email.get(),
                                                                        self.var_nationality.get(),
                                                                        self.var_idproof.get(),
                                                                        self.var_idnumber.get(),
                                                                        self.var_address.get(),

                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(title="message", message="Customer Data Has Been Added")
            except Exception as es:
                messagebox.showwarning(title="Warning", message=f"Something Went Wrong {es}", parent=self.root)
    

    # ************* Fetch Data ******************
    def fetch_data(self):
        conn = mysql.connector.connect(host="127.0.0.1", username="root", password="passwordxx", database="Customers")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("","end", values=i)
            conn.commit()
        conn.close()



    def get_cursor(self, event):
        cursor_row = self.cust_details_table.focus()
        content = self.cust_details_table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_custname.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_idproof.set(row[8])
        self.var_idnumber.set(row[9])
        self.var_address.set(row[10])


    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror(title="errot", message="Please Fill Mobile Field")
        else:
            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="passwordxx", database="Customers")
            my_cursor = conn.cursor()
            my_cursor.execute("update CUSTOMER set name=%s, custmother=%s, gender=%s, post=%s, mobile=%s, email=%s, nationality=%s, idproof=%s, idnumber=%s, address=%s where ref=%s", (
                                                                        self.var_custname.get(),
                                                                        self.var_mother.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_post.get(),
                                                                        self.var_mobile.get(),
                                                                        self.var_email.get(),
                                                                        self.var_nationality.get(),
                                                                        self.var_idproof.get(),
                                                                        self.var_idnumber.get(),
                                                                        self.var_address.get(),
                                                                        self.var_ref.get()
                                                                                                     ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(title="Update", message="Details Updated Successfully!", parent=self.root)

    # Delete
    def delete(self):
        del_message = messagebox.askyesno("Hotel Management System", "Do you want delete this customer", parent=self.root)
        if del_message > 0:
            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="passwordxx", database="Customers")
            my_cursor = conn.cursor()
            query = "delete from CUSTOMER  where ref=%s"
            values = (self.var_ref.get(),)
            my_cursor.execute(query,values)
        else:
            if not del_message:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_custname.set("")
        self.var_mother.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_idnumber.set("")
        self.var_address.set("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))


    # Search Data
    def search_data(self):
        conn = mysql.connector.connect(
            host="127.0.0.1", 
            username="root", 
            password="passwordxx", 
            database="Customers"
            )
        my_cursor = conn.cursor()

        column_name = str(self.search_var.get())  # Replace with your actual column name
        search_value = str(self.txt_search.get())

        query = f"SELECT * FROM CUSTOMER WHERE {column_name} LIKE %s"
        my_cursor.execute(query, ('%' + search_value + '%',))



        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("", "end", values=i)
            conn.commit()
        conn.close()
            






        
        


if __name__ == "__main__":
    root = tk.Tk()
    cw = Customer_wind(root)
    root.mainloop()
