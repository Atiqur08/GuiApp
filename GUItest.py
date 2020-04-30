from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image

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

        about=Menu(menubar, tearoff=0)
        menubar.add_cascade(label="About", menu=about)
        about.add_command(label="About and licence",command=About)

        Tk.config(self,menu=menubar)

 		self.frames = {} 
        for F in (StartPage, PageOne, CoronaTips, COVID, Prevention):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
 
        self.show_frame(StartPage)
 
    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
 
class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        header=Label(self, text="                                             FIRST-AID___________", font=("Verdana", 12,"bold"),bg="grey",fg="white",width="1536",height="6",anchor=W,justify=LEFT)
        header.pack(padx=10,pady=10)
        
        

        fram1 = LabelFrame(self,text="CoronaTips",padx=20,pady=20)
        fram1.place(x=20,y=650)
        lbl1=Label(fram1,text="Coronavirus is a class of virus responsible for.......").pack()
        button1=ttk.Button(fram1,text="Learn More...",command=lambda : controller.show_frame(CoronaTips)).pack(side="bottom")
        
        fram2 = LabelFrame(self,text="COVID-19",padx=20,pady=20)
        fram2.place(x=570,y=650)
        lbl2=Label(fram2,text="COVID-19 is a respiratory disease caused by SARS-CoV 2 virus...").pack()
        button2=ttk.Button(fram2,text="Learn More...",command=lambda : controller.show_frame(COVID)).pack(side="bottom")
        
        fram3 = LabelFrame(self,text="WHAT YOU CAN DO",padx=20,pady=20)
        fram3.place(x=1140,y=650)
        lbl3=Label(fram3,text="It can be prevented if the following techniques are utilized.....").pack()
        button3=ttk.Button(fram3,text="Learn More...",command=lambda : controller.show_frame(Prevention)).pack(side="bottom")

        fram4 = LabelFrame(self,padx=350,pady=150)
        fram4.place(x=700,y=300)
        button4=ttk.Button(fram4,text="NEXT",command=lambda : controller.show_frame(PageOne)).grid(row=2,column=2)

        photo=PhotoImage(file="C:/Users/Atiqur/Desktop/GuiApp/health2.gif")
        lbl5=Label(self,image=photo)
        lbl5.image=photo
        lbl5.place(x=800,y=100)

        photo1=PhotoImage(file="C:/Users/Atiqur/Desktop/GuiApp/Picture5.gif")
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=30)
                                
                                                                                            
                                                            
 
class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label =ttk.Label(self, text='Page One', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
 
        button1 = ttk.Button(self, text='BACK',command=lambda : controller.show_frame(StartPage))
        button1.pack()

class CoronaTips(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label=Label(self, text='TIPS', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button3=ttk.Button(self, text='HOME',command=lambda : controller.show_frame(StartPage))
        button3.pack()

class COVID(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label=Label(self, text='About COVID-19', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
 
        button3=ttk.Button(self, text='HOME',command=lambda : controller.show_frame(StartPage))
        button3.pack()


class Prevention(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label=Label(self, text='WHAT YOU CAN DO', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
 
        button3=ttk.Button(self, text='HOME',command=lambda : controller.show_frame(StartPage))
        button3.pack()


app = MainWindow()
app.mainloop()