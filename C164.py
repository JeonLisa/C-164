from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("PLANET ENCYCLOPEDIA")
root.configure(background="plum2")
label_heading=Label(root,text="Planets",font=("Roman"),bg="plum2")
label_heading.place(relx=0.2,rely=0.1,anchor=CENTER)
label_planet_name=Label(root,font=("Roman",18,"bold"),bg="plum2")
label_planet_name.place(relx=0.5,rely=0.25,anchor=CENTER)
label_gravity_radius=Label(root,font=("Roman"),bg="plum2")
label_gravity_radius.place(relx=0.5,rely=0.8,anchor=CENTER)
label_planet_info=Label(root,font=("Roman",10,"bold"),bg="plum2",wraplength=200)
label_planet_info.place(relx=0.5,rely=0.9,anchor=CENTER)
label_image=Label(root,bg="orchid4",highlightthickness=5,borderwidth=2,relief=SOLID)
label_image.place(relx=0.5,rely=0.5,anchor=CENTER)
def planetinfo():
    print("high")
button_show=Button(root,command=planetinfo,text="Show Info")
button_show.place(relx=0.5,rely=0.18,anchor=CENTER)
root.mainloop()