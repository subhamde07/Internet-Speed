from tkinter import *
import speedtest
from speedtest import Speedtest


def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10 ** 6), 2)) + "Mbps"
    up = str(round(sp.upload() / (10 ** 6), 2)) + "Mbps"
    leb_down.config(text=down)
    leb_up.config(text=up)


sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("400x500")
sp.config(bg="Black")

leb = Label(sp, text="Internet Speed Test", font=("Time New Roman", 25, "bold"), fg="Blue")
leb.place(x=40, y=50, width=310, height=35)

leb = Label(sp, text="Download Speed", font=("Time New Roman", 15, "bold"), fg="Black")
leb.place(x=85, y=130, width=220, height=30)
leb_down = Label(sp, text="00", font=("Time New Roman", 30, "bold"), bg="Black", fg="Green")
leb_down.place(x=85, y=180, width=220, height=37)

leb = Label(sp, text="Upload Speed", font=("Time New Roman", 15, "bold"), fg="Black")
leb.place(x=85, y=260, width=220, height=30)
leb_up = Label(sp, text="00", font=("Time New Roman", 30, "bold"), bg="Black", fg="Green")
leb_up.place(x=85, y=310, width=220, height=37)

button = Button(sp, text="Check Speed", font=("Time New Roman", 20, "bold"), relief=RAISED, bg="Red", fg="Yellow",
                command=speedcheck)
button.place(x=85, y=400, width=220, height=35)
sp.mainloop()

