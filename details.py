import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox


class Details_wind:
    def __init__(self, root):
        self.root = root
        self.root.title("Room Details")
        self.root.geometry("1240x610+230+270")

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
        labelframeleft = tk.LabelFrame(self.root, bd=2, relief="ridge", text="Add New Rooms", padx=2, pady=10, font=("times new roman", 14, "bold"))
        labelframeleft.place(x=5, y=55, width=520, height=350)

        # Floor
        lbl_floor = tk.Label(labelframeleft, text="Floor", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky="w")

        self.var_floor = tk.StringVar()
        entry_floor = ttk.Entry(labelframeleft, textvariable=self.var_floor, width=20, font=("arial", 13, "bold"))
        entry_floor.grid(row=0, column=1, sticky="w", padx=5)

        # Room No
        lbl_roomno = tk.Label(labelframeleft, text="Room No", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_roomno.grid(row=1, column=0, sticky="w")

        self.var_roomno = tk.StringVar()
        entry_roomno = ttk.Entry(labelframeleft, textvariable=self.var_roomno, width=20, font=("arial", 13, "bold"))
        entry_roomno.grid(row=1, column=1, sticky="w", padx=5)


        # Room Type
        lbl_room_type = tk.Label(labelframeleft, text="Room Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_room_type.grid(row=2, column=0, sticky="w")

        self.var_roomtype = tk.StringVar()
        entry_room_type = ttk.Entry(labelframeleft, textvariable=self.var_roomtype, width=20, font=("arial", 13, "bold"))
        entry_room_type.grid(row=2, column=1, sticky="w", padx=5)


        ################ Btns ##########################
        btn_frame = tk.Frame(labelframeleft, bd=2, relief="ridge", bg="black")
        btn_frame.place(x=0, y=200, width=418, height=40)

        btnadd = tk.Button(btn_frame, command=self.add_data, font=("arial", 11, "bold"), text="Add", fg="black", width=9, height=2)
        btnadd.grid(row=0, column=0, padx=2)

        btnupdate = tk.Button(btn_frame, command=self.update, font=("arial", 11, "bold"), text="Update", fg="black", width=9, height=2)
        btnupdate.grid(row=0, column=1, padx=2)

        btndelete = tk.Button(btn_frame, command=self.delete, font=("arial", 11, "bold"), text="Delete", fg="black", width=9, height=2)
        btndelete.grid(row=0, column=2, padx=2)

        btnreset = tk.Button(btn_frame, command=self.reset, font=("arial", 11, "bold"), text="Reset", fg="black", width=9, height=2)
        btnreset.grid(row=0, column=3, padx=2)


        ################ Label Frame ####################
        table_frame = tk.LabelFrame(self.root, bd=2, relief="ridge", text="Show Room Details", padx=2, pady=10, font=("times new roman", 14, "bold"))
        table_frame.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient="horizontal")
        scroll_y = ttk.Scrollbar(table_frame, orient="vertical")

        self.room_table = ttk.Treeview(table_frame, column=("floor", "roomno", "roomtype"),
                                                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomtype", text="Room Type")

        self.room_table["show"] = "headings"

        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomtype", width=100)

        self.room_table.pack(fill="both", expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()



    # ***************** Add Data To DataBase **********************
    def add_data(self):
        if not self.var_floor.get() or not self.var_roomtype.get():
            messagebox.showerror(title="error", message="Can't Left Blank")
        else:
            try:
                conn = mysql.connector.connect(host="127.0.0.1", username="root", password="passwordxx", database="Customers")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)", (
                                                                        self.var_floor.get(),
                                                                        self.var_roomno.get(),
                                                                        self.var_roomtype.get()
                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(title="message", message="New Room Booked Sucessfully!")
            except Exception as es:
                messagebox.showwarning(title="Warning", message=f"Something Went Wrong {es}", parent=self.root)


    # ************* Fetch Data ******************
    def fetch_data(self):
        conn = mysql.connector.connect(host="127.0.0.1", username="root", password="passwordxx", database="Customers")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("","end", values=i)
            conn.commit()
        conn.close()



    # Get Cursor
    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomtype.set(row[2])




    # Update
    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror(title="error", message="Please Fill Contact Field")
        else:
            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="passwordxx", database="Customers")
            my_cursor = conn.cursor()
            my_cursor.execute("update details set Floor=%s, RoomType=%s where RoomNo=%s", (
                                                                        self.var_floor.get(),
                                                                        self.var_roomtype.get(),
                                                                        self.var_roomno.get()

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
            query = "delete from details  where roomno=%s"
            values = (self.var_roomno.get(),)
            my_cursor.execute(query,values)
            messagebox.showinfo("Hotel Management System", "Record Deleated Sucessfully!", parent=self.root)

        else:
            if not del_message:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    #Reset data
    def reset(self):
        self.var_floor.set("")
        self.var_roomno.set("")
        self.var_roomtype.set("")


if __name__ == "__main__":
    root = tk.Tk()
    cw = Details_wind(root)
    root.mainloop()