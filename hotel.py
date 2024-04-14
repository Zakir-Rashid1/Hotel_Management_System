import tkinter as tk
from PIL import Image, ImageTk
from customer import Customer_wind
from room import Roombooking
from details import Details_wind





class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1470x1000+0+0")

        ################ First Image ###########################
        img1 = Image.open("./images/hotel1.png")
        img1 = img1.resize((1470, 600))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbling = tk.Label(self.root, image=self.photoimg1, bd=4, relief="ridge")
        lbling.place(x=0, y=0, width=1470, height=140)

        ################ Title ###########################
        lbl_title = tk.Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black",fg="gold")
        lbl_title.place(x=0, y=140, width=1470, height=50) 
        
        ################ Logo ###########################
        img2 = Image.open("./images/logohotel.png")
        img2 = img2.resize((230, 140))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbling = tk.Label(self.root, image=self.photoimg2, bd=4, relief="ridge")
        lbling.place(x=0, y=0, width=230, height=140)



        ################ Main Frame ###########################
        main_frame = tk.Frame(self.root, bd=4, relief="ridge")
        main_frame.place(x=0, y=190, width=1470, height=620)

        ################ Menu ###########################
        lbl_menu = tk.Label(main_frame, text="MENU", font=("times new roman",20,"bold"), bg="black",fg="gold")
        lbl_menu.place(x=0, y=0, width=230)

         ################ Button Frame ###########################
        btn_frame = tk.Frame(main_frame, bd=4, relief="ridge")
        btn_frame.place(x=0, y=35, width=228, height=180)

        customer_btn = tk.Button(btn_frame, text="CUSTOMER", command=self.cus_details, width=27, font=("times new roman",14, "bold"), highlightbackground="black",fg="black", bd=0, cursor="hand")
        customer_btn.grid(row=0, column=0, pady=5)

        room_btn = tk.Button(btn_frame, command=self.room_booking, text="ROOM", width=27, font=("times new roman",14, "bold"), highlightbackground="black",fg="black", bd=0, cursor="hand")
        room_btn.grid(row=1, column=0, pady=5)

        detail_btn = tk.Button(btn_frame, command=self.details_wind, text="ROOM DETAIL", width=27, font=("times new roman",14, "bold"), highlightbackground="black",fg="black", bd=0, cursor="hand")
        detail_btn.grid(row=2, column=0, pady=5)

        # report_btn = tk.Button(btn_frame, text="REPORT", width=27, font=("times new roman",14, "bold"), highlightbackground="black",fg="black", bd=0, cursor="hand")
        # report_btn.grid(row=3, column=0, pady=5)

        # logout_btn = tk.Button(btn_frame, text="LOGOUT", width=27, font=("times new roman",14, "bold"), highlightbackground="black",fg="black", bd=0, cursor="hand")
        # logout_btn.grid(row=4, column=0, pady=5)



        ################## Right Side Image ###################
        img3 = Image.open("./images/slide3.jpg")
        img3 = img3.resize((1310, 620))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbling1 = tk.Label(main_frame, image=self.photoimg3, bd=4, relief="ridge")
        lbling1.place(x=225, y=0, width=1240, height=620)          


        ################## Down Image ###################
        img4 = Image.open("./images/myh.jpg")
        img4 = img4.resize((220, 210))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lbling1 = tk.Label(main_frame, image=self.photoimg4, bd=4, relief="ridge")
        lbling1.place(x=0, y=215, width=225, height=210)   

        img5 = Image.open("./images/khana.jpg")
        img5 = img5.resize((220, 195))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lbling1 = tk.Label(main_frame, image=self.photoimg5, bd=4, relief="ridge")
        lbling1.place(x=0, y=420, width=225, height=195)     


                                                         
                                                       

    def cus_details(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = Customer_wind(self.new_window)

    def room_booking(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = Roombooking(self.new_window)

    def details_wind(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = Details_wind(self.new_window)






if __name__ == "__main__":
    root = tk.Tk()
    hms = HotelManagementSystem(root)
    root.mainloop()