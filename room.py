import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strptime
from datetime import datetime

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Room Booking Details")
        self.root.geometry("1240x610+230+270")

        # ************Variables **********************
        self.var_contact = tk.StringVar()
        self.var_checkin = tk.StringVar()
        self.var_checkou = tk.StringVar()
        self.var_roomtype = tk.StringVar()
        self.var_roomaval = tk.StringVar()
        self.var_meal = tk.StringVar()
        self.var_noofdays = tk.StringVar()
        self.var_padtax = tk.StringVar()
        self.var_subtotal = tk.StringVar()
        self.var_totalcost = tk.StringVar()




        ################ Title ###########################
        lbl_title = tk.Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black",fg="gold")
        lbl_title.place(x=0, y=0, width=1240, height=50) 


        ################ Logo ###########################
        img2 = Image.open("./images/logohotel.png")
        img2 = img2.resize((100, 40))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbling = tk.Label(self.root, image=self.photoimg2, bd=0, relief="ridge")
        lbling.place(x=5, y=2, width=100, height=40)









        ################ Label Frame ####################
        labelframeleft = tk.LabelFrame(self.root, bd=2, relief="ridge", text="Room Booking Details", padx=2, pady=10, font=("times new roman", 14, "bold"))
        labelframeleft.place(x=5, y=55, width=425, height=490)

        # Cust Ref
        lbl_cust_contact = tk.Label(labelframeleft, text="Customer Contact", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky="w")
        entry_contact = ttk.Entry(labelframeleft,textvariable=self.var_contact, width=20, font=("arial", 13, "bold"))
        entry_contact.grid(row=0, column=1, sticky="w")

        # Fetch Data Button
        btnadd = tk.Button(labelframeleft,command=self.fetch_contact, font=("arial", 12, "bold"), text="Fetch Data", fg="black", width=7, height=1)
        btnadd.place(x=290, y=2)


        #Check in Date
        check_in_date = tk.Label(labelframeleft, text="Check In Date", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky="w")
        txtcheck_in_date = ttk.Entry(labelframeleft,textvariable=self.var_checkin,  width=29, font=("arial", 13, "bold"))
        txtcheck_in_date.grid(row=1, column=1)


        #Check in Date
        check_out_date = tk.Label(labelframeleft, text="Check Out Date", font=("arial", 12, "bold"), padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky="w")
        txtcheck_out_date = ttk.Entry(labelframeleft,textvariable=self.var_checkou, width=29, font=("arial", 13, "bold"))
        txtcheck_out_date.grid(row=2, column=1)

        #Room Tyoe
        check_out_date = tk.Label(labelframeleft, text="Room Type", font=("arial", 12, "bold"), padx=2, pady=6)
        check_out_date.grid(row=3, column=0, sticky="w")

        combo_room_type = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,  font=("arial", 13, "bold"), width=27, state="readonly")
        combo_room_type['values'] = ("Single", "Double", "Luxuary")
        combo_room_type.current(0)
        combo_room_type.grid(row=3, column=1)


        #Available Room
        lbl_room_avl = tk.Label(labelframeleft, text="Available Room", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_room_avl.grid(row=4, column=0, sticky="w")
        txt_lbl_room_avl = ttk.Entry(labelframeleft,textvariable=self.var_roomaval,  width=29, font=("arial", 13, "bold"))
        txt_lbl_room_avl.grid(row=4, column=1)

        #Meal
        lbl_meal = tk.Label(labelframeleft, text="Meal", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_meal.grid(row=5, column=0, sticky="w")
        txt_meal = ttk.Entry(labelframeleft,textvariable=self.var_meal,  width=29, font=("arial", 13, "bold"))
        txt_meal.grid(row=5, column=1)


        #Number of days
        lbl_no_days = tk.Label(labelframeleft, text="Number of Days", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_no_days.grid(row=6, column=0, sticky="w")
        txt_no_days = ttk.Entry(labelframeleft,textvariable=self.var_noofdays,  width=29, font=("arial", 13, "bold"), state="readonly")
        txt_no_days.grid(row=6, column=1)


        # Paid Tax
        lbl_tax_paid = tk.Label(labelframeleft, text="Tax Paid", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_tax_paid.grid(row=7, column=0, sticky="w")
        txt_tax_paid = ttk.Entry(labelframeleft,textvariable=self.var_padtax,  width=29, font=("arial", 13, "bold"), state="readonly")
        txt_tax_paid.grid(row=7, column=1)

        # Sub Total
        lbl_sub_total = tk.Label(labelframeleft, text="Sub Total", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_sub_total.grid(row=8, column=0, sticky="w")
        txt_sub_total = ttk.Entry(labelframeleft,textvariable=self.var_subtotal,  width=29, font=("arial", 13, "bold"),state="readonly")
        txt_sub_total.grid(row=8, column=1)

        # Total Cost
        lbl_total_cost = tk.Label(labelframeleft, text="Total Cost", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_total_cost.grid(row=9, column=0, sticky="w")
        txt_total_cost = ttk.Entry(labelframeleft,textvariable=self.var_totalcost,  width=29, font=("arial", 13, "bold"),state="readonly")
        txt_total_cost.grid(row=9, column=1)

        #######Bill Button ################
        btnadd = tk.Button(labelframeleft, command=self.total, font=("arial", 13, "bold"), text="Bill", fg="black", width=7, height=1)
        btnadd.grid(row=10, column=0, padx=2,pady=2, sticky="w")


        ################ Btns ##########################
        btn_frame = tk.Frame(labelframeleft, bd=2, relief="ridge", bg="black")
        btn_frame.place(x=0, y=350, width=418, height=40)

        btnadd = tk.Button(btn_frame, command=self.add_data, font=("arial", 11, "bold"), text="Add", fg="black", width=9, height=2)
        btnadd.grid(row=0, column=0, padx=2)

        btnupdate = tk.Button(btn_frame, command=self.update, font=("arial", 11, "bold"), text="Update", fg="black", width=9, height=2)
        btnupdate.grid(row=0, column=1, padx=2)

        btndelete = tk.Button(btn_frame, command=self.delete, font=("arial", 11, "bold"), text="Delete", fg="black", width=9, height=2)
        btndelete.grid(row=0, column=2, padx=2)

        btnreset = tk.Button(btn_frame,command=self.reset, font=("arial", 11, "bold"), text="Reset", fg="black", width=9, height=2)
        btnreset.grid(row=0, column=3, padx=2)


        ########## Right Sided Image #######################
        img3 = Image.open("./images/bed.jpg")
        img3 = img3.resize((500, 240))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbling = tk.Label(self.root, image=self.photoimg3, bd=0, relief="ridge")
        lbling.place(x=750, y=55, width=485, height=240)





        ################# Table Frame ################################
        table_frame = tk.LabelFrame(self.root, bd=2, relief="ridge", text="View Details And Search System", padx=2, pady=10, font=("times new roman", 14, "bold"))
        table_frame.place(x=435, y=280, width=803, height=265)

        lblsearchby = tk.Label(table_frame, text="Search By: ", font=("arial", 13, "bold"), bg="red", fg="black")
        lblsearchby.grid(row=0, column=0, sticky="w", padx=3)

        self.search_var = tk.StringVar()
        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, values=["Contact", "RoomAlloted"], font=("arial", 13, "bold"), width=24, state="readonly")
        combo_search.grid(row=0, column=1, padx=3)


        self.txt_search = tk.StringVar()
        txtsearch = ttk.Entry(table_frame, textvariable=self.txt_search, width=24, font=("arial", 13, "bold"))
        txtsearch.grid(row=0, column=2, padx=3)


        btnsearch = tk.Button(table_frame, command=self.search_data, font=("arial", 11, "bold"), text="Search", fg="black", height=2)
        btnsearch.grid(row=0, column=3, padx=3)

        btnshowall = tk.Button(table_frame, command=self.fetch_data,font=("arial", 11, "bold"), text="Show All", fg="black", height=2)
        btnshowall.grid(row=0, column=4, padx=3)





        ################## Show Data Table ##################
        details_table = tk.Frame(table_frame, bd=2, relief="ridge")  
        details_table.place(x=0, y=55, width=795, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient="horizontal")
        scroll_y = ttk.Scrollbar(details_table, orient="vertical")

        self.room_table = ttk.Treeview(details_table, column=("contact", "checkin", "checkou", "roomtype", "roomaval", "meal",
                                                                       "noofdays"),
                                                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact No")
        self.room_table.heading("checkin", text="Check In Date")
        self.room_table.heading("checkou", text="Check out Date")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomaval", text="Room Aval")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noofdays", text="No of Days")


        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkou", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomaval", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noofdays", width=100)

        self.room_table.pack(fill="both", expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # ********* Fetch Data Preview  ****************
    def fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror(title="Errot", message="Please Fill Contact Feild", parent=self.root)
        else:
            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="passwordxx", database="Customers")
            my_cursor = conn.cursor()
            query = ("select * from CUSTOMER where mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchall()

            if not len(row):
                messagebox.showerror(title="Error", message="This contact number doesn't exits", parent=self.root)
            else:
                column_names = [i[0] for i in my_cursor.description]
                conn.commit()
                conn.close()

                show_data_frame = tk.LabelFrame(self.root, text="Customer Data Preview", font=("times new roman", 12, "bold italic"), bd=4, relief="ridge", padx=2)
                show_data_frame.place(x=450, y=65, width=280, height=180)

                for i in range(1, 9):
                    lbl_name = tk.Label(show_data_frame, text=column_names[i].capitalize(), font=("times new roman", 12, "italic"))
                    lbl_name.grid(row=0+i-1, column=0, sticky="w")

                    lbl = tk.Label(show_data_frame, text=row[0][i], font=("times new roman", 12, "italic"))
                    lbl.grid(row=i-1, column=1,sticky="w", padx=5)




    # ***************** Add Data To DataBase **********************
    def add_data(self):
        if not self.var_contact.get() or not self.var_checkin.get():
            messagebox.showerror(title="error", message="Can't Left Blank")
        else:
            try:
                conn = mysql.connector.connect(host="127.0.0.1", username="root", password="passwordxx", database="Customers")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into Room values(%s,%s,%s,%s,%s,%s,%s)", (
                                                                        self.var_contact.get(),
                                                                        self.var_checkin.get(),
                                                                        self.var_checkou.get(),
                                                                        self.var_roomtype.get(),
                                                                        self.var_roomaval.get(),
                                                                        self.var_meal.get(),
                                                                        self.var_noofdays.get()
                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(title="message", message="Room Data Has Been Added")
            except Exception as es:
                messagebox.showwarning(title="Warning", message=f"Something Went Wrong {es}", parent=self.root)


    # ************* Fetch Data ******************
    def fetch_data(self):
        conn = mysql.connector.connect(host="127.0.0.1", username="root", password="passwordxx", database="Customers")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("","end", values=i)
            conn.commit()
        conn.close()


    # Get Cursor
    def get_cursor(self, event):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkou.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomaval.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])


    # Update
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror(title="error", message="Please Fill Contact Field")
        else:
            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="passwordxx", database="Customers")
            my_cursor = conn.cursor()
            my_cursor.execute("update Room set Checkin=%s, Checkout=%s, Roomtype=%s, RoomAlloted=%s, Meal=%s, Numberofdays=%s where Contact=%s", (
                                                                        self.var_checkin.get(),
                                                                        self.var_checkou.get(),
                                                                        self.var_roomtype.get(),
                                                                        self.var_roomaval.get(),
                                                                        self.var_meal.get(),
                                                                        self.var_noofdays.get(),
                                                                        self.var_contact.get()

                                                                                                     ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(title="Update", message="Details Updated Successfully!", parent=self.root)

    # Delete
    def delete(self):
        del_message = messagebox.askyesno("Hotel Management System", "Do you want to deleate the room details?", parent=self.root)
        if del_message > 0:
            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="passwordxx", database="Customers")
            my_cursor = conn.cursor()
            query = "delete from Room  where Contact=%s"
            values = (self.var_contact.get(),)
            my_cursor.execute(query,values)
            messagebox.showinfo("Hotel Management System", "Record Deleated Sucessfully!", parent=self.root)

        else:
            if not del_message:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def total(self):
        indate = self.var_checkin.get()
        outdate = self.var_checkou.get()

        indate = datetime.strptime(indate, "%d/%m/%Y")
        outdate = datetime.strptime(outdate, "%d/%m/%Y")
        self.var_noofdays.set(abs(outdate-indate).days)


        if self.var_meal.get() == "Break Fast" and self.var_roomtype.get() == "Single":
            break_fast_price = float(300)
            luxary_room_price = float(1000)
            one_day_price = float(break_fast_price+luxary_room_price)
            total_price = float(float(self.var_noofdays.get()) * one_day_price)

            tax =  "Rs: {:.2f}".format(total_price * 0.1)
            sub_total =  "Rs: {:.2f}".format(total_price)
            total_cost =  "Rs: {:.2f}".format(total_price + total_price * 0.1)

            self.var_padtax.set(tax)
            self.var_subtotal.set(sub_total)
            self.var_totalcost.set(total_cost)
        elif self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Luxuary":
            break_fast_price = float(500)
            luxary_room_price = float(2000)
            one_day_price = float(break_fast_price+luxary_room_price)
            total_price = float(float(self.var_noofdays.get()) * one_day_price)

            tax =  "Rs: {:.2f}".format(total_price * 0.1)
            sub_total =  "Rs: {:.2f}".format(total_price)
            total_cost =  "Rs: {:.2f}".format(total_price + total_price * 0.1)

            self.var_padtax.set(tax)
            self.var_subtotal.set(sub_total)
            self.var_totalcost.set(total_cost)


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

        query = f"SELECT * FROM Room WHERE {column_name} LIKE %s"
        my_cursor.execute(query, ('%' + search_value + '%',))



        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", "end", values=i)
            conn.commit()
        else:
            messagebox.showwarning(title="warning", message="Record Not Found😛")
        conn.close()



            
    # Reset
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkou.set("")
        self.var_roomtype.set("")
        self.var_roomaval.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_padtax.set("")
        self.var_subtotal.set("")
        self.var_totalcost.set("")




                



            







if __name__ == "__main__":
    root = tk.Tk()
    cw = Roombooking(root)
    root.mainloop()