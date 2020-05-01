from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

LARGE_FONT = ("Times", 12)

def Open():
        print("You did it!!")

def About():
       messagebox.showinfo("About and Licence","This software is free and open source and is created by students of Jorhat Engineering College, Assam, India")
 
class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("First-Aid") 

        self.iconbitmap('C:/Users/Atiqur/Desktop/GuiApp/Tkintericon.ico')

        self.geometry("%dx%d+0+0"%self.maxsize())

        
                                

        container=Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)   
        container.grid_columnconfigure(0,weight=1) 

        
        menubar=Menu(container)
        
        submenu=Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=submenu)
        
        submenu.add_command(label="Open",command=Open)
        submenu.add_separator()
        submenu.add_command(label="Exit",command=quit)

        info=Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Info",menu=info)
        info.add_command(label="Coronatips",command=lambda:self.show_frame(CoronaTips))
        info.add_separator()
        info.add_command(label="COVID-19",command=lambda:self.show_frame(COVID))
        info.add_separator()
        info.add_command(label="Prevention",command=lambda:self.show_frame(Prevention))

        about=Menu(menubar, tearoff=0)
        menubar.add_cascade(label="About", menu=about)
        about.add_command(label="About and licence",command=About)

        Tk.config(self,menu=menubar)

        self.frames = {} 
        for F in (StartPage, PageOne, PageTwo, CoronaTips, COVID, Prevention):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
 
        self.show_frame(StartPage)
 
    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
 
class StartPage(Frame,Tk):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        

        
        header=Label(self, text="                                   FIRST-AID : ANTI COVID-19 AND ANTI POVERTY INITIATIVE                                                                                                                              JORHAT ENGINEERING COLLEGE, ASSAM, INDIA", font=("Cambria", 12),bg="grey",fg="white",width="1536",height="6",anchor=W,justify=LEFT)
        header.pack(padx=10,pady=10)
        
        
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self, text="THIS IS THE FOOT-NOTE", font=("Verdana", 12,"bold"),bg="grey",fg="white",width="1520",height="3",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

       

        #fram1 = LabelFrame(self,text="CoronaTips",padx=20,pady=20)
        #fram1.place(x=50,y=600)
        #lbl1=Label(fram1,text="Coronavirus is a class of virus responsible for.......").pack()
        #button1=ttk.Button(fram1,text="Learn More...",command=lambda : controller.show_frame(CoronaTips)).pack(side="bottom")
        
        #fram2 = LabelFrame(self,text="COVID-19",padx=20,pady=20)
        #fram2.place(x=570,y=600)
        #lbl2=Label(fram2,text="COVID-19 is a respiratory disease caused by SARS-CoV 2 virus...").pack()
        #button2=ttk.Button(fram2,text="Learn More...",command=lambda : controller.show_frame(COVID)).pack(side="bottom")
        
        #fram3 = LabelFrame(self,text="WHAT YOU CAN DO",padx=20,pady=20)
        #fram3.place(x=1140,y=600)
        #lbl3=Label(fram3,text="It can be prevented if the following techniques are utilized.....").pack()
        #button3=ttk.Button(fram3,text="Learn More...",command=lambda : controller.show_frame(Prevention)).pack(side="bottom")
        photo3=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/test1.png"))
        lbl7=Label(self,image=photo3)
        lbl7.image=photo3
        lbl7.place(x=148,y=185)

        photo4=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/Poverty1.png"))
        lbl8=Label(self,image=photo4)
        lbl8.image=photo4
        lbl8.place(x=870,y=185)


        fram4 = LabelFrame(self,padx=125,pady=80,relief="solid",borderwidth=10)
        fram4.place(x=150,y=302)
        label1=Label(fram4,text="It will only produce a speculated result based on the questions asked about your travel history, medical history etc. This tool can help you understand what to do next about COVID-19",wraplength=250,font=("Cambria",12)).pack()

        button4=ttk.Button(fram4,text="Check",command=lambda : controller.show_frame(PageOne)).pack(side="bottom")

        fram5 = LabelFrame(self,padx=125,pady=77,relief="solid",borderwidth=10)
        fram5.place(x=870,y=297)
        label2=Label(fram5,text="This tool will help the below poverty line community with financial assisstance since their income sources has been cut-off with the onset of nationwide lockdown",wraplength=250,font=("Cambria",12)).pack()
        button5=ttk.Button(fram5,text="NEXT",command=lambda : controller.show_frame(PageTwo)).pack(side="bottom")

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)

        


        
                                                                                            
                                                            
 
class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        header=Label(self,bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)
        
        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        frame1=LabelFrame(self,padx=200,pady=150,relief="solid")
        frame1.place(x=400,y=300)
        lbl=Label(frame1,text="This is a new one").pack()
        button1 = ttk.Button(frame1, text='BACK',command=lambda : controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(frame1, text='NEXT')
        button2.pack()

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)


class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        header=Label(self,bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        label =ttk.Label(self, text='Page Two', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
 
        button1 = ttk.Button(self, text='BACK',command=lambda : controller.show_frame(StartPage))
        button1.pack()

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)


class CoronaTips(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        header=Label(self,bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        label=Label(self, text='TIPS', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button3=ttk.Button(self, text='HOME',command=lambda : controller.show_frame(StartPage))
        button3.pack()

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)

class COVID(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        header=Label(self,bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        label=Label(self, text='About COVID-19', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
 
        button3=ttk.Button(self, text='HOME',command=lambda : controller.show_frame(StartPage))
        button3.pack()

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)



class Prevention(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        header=Label(self,bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)
        label=Label(self, text='WHAT YOU CAN DO', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
 
        button3=ttk.Button(self, text='HOME',command=lambda : controller.show_frame(StartPage))
        button3.pack()

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)



app = MainWindow()
app.mainloop()