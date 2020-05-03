from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

LARGE_FONT = ("Times", 12)

global v1


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
        for F in (StartPage, Sym1, Sym2, Pov1, Pov2,Safe,Average, Risk, NoRisk, CoronaTips, COVID, Prevention):
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

        button4=ttk.Button(fram4,text="Check",command=lambda : controller.show_frame(Sym1)).pack()

        fram5 = LabelFrame(self,padx=125,pady=77,relief="solid",borderwidth=10)
        fram5.place(x=870,y=297)
        label2=Label(fram5,text="This tool will help the below poverty line community with financial assisstance since their income sources has been cut-off with the onset of nationwide lockdown",wraplength=250,font=("Cambria",12)).pack()
        button5=ttk.Button(fram5,text="NEXT",command=lambda : controller.show_frame(Pov1)).pack()

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)

        


        
                                                                                            
                                                            
 
class Sym1(Frame):

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
        button2 = ttk.Button(frame1, text='NEXT',command=lambda: controller.show_frame(Sym2))
        button2.pack()

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)

class Sym2(Frame):


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

        frame1=LabelFrame(self,padx=20,pady=20,relief="solid",bg="white")
        frame1.place(x=400,y=150)
        lbl=Label(frame1,text="Check the boxes corresponding to the descriptions that best fit you:", font=("Cambria",16,"bold"),bg="white").grid(row=0,column=0,sticky=W)
        
        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()
        v1=IntVar()
        v2=IntVar()
        v3=IntVar()
        v4=IntVar()
        v5=IntVar()
        v6=IntVar()
        v7=IntVar()
        v8=IntVar()
        
        label1=Label(frame1,text="1. Dry Cough",bg="white",font=("Cambria",12)).grid(row=3,column=0,sticky=W)
        c1=Checkbutton(frame1,variable=var1,command=lambda:click1(var1),bg="white",activebackground="white")
        c1.grid(row=3,column=3)

        label1=Label(frame1,text="2. Shortness of breath/difficulty breathing",bg="white",font=("Cambria",12)).grid(row=5,column=0,sticky=W)
        c2=Checkbutton(frame1,variable=var2,command=lambda:click2(var2),bg="white",activebackground="white")
        c2.grid(row=5,column=3)

        label1=Label(frame1,text="3. Fever and chills",bg="white",font=("Cambria",12)).grid(row=7,column=0,sticky=W)
        c3=Checkbutton(frame1,variable=var3,command=lambda:click3(var3),bg="white",activebackground="white")
        c3.grid(row=7,column=3)

        label1=Label(frame1,text="4. Sore throat",bg="white",font=("Cambria",12)).grid(row=9,column=0,sticky=W)
        c4=Checkbutton(frame1,variable=var4,command=lambda:click4(var4),bg="white",activebackground="white")
        c4.grid(row=9,column=3)

        label1=Label(frame1,text="5. Muscle pain",bg="white",font=("Cambria",12)).grid(row=11,column=0,sticky=W)
        c5=Checkbutton(frame1,variable=var5,command=lambda:click5(var5),bg="white",activebackground="white")
        c5.grid(row=11,column=3)

        label1=Label(frame1,text="6. Chest Pain",bg="white",font=("Cambria",12)).grid(row=13,column=0,sticky=W)
        c6=Checkbutton(frame1,variable=var6,command=lambda:click6(var6),bg="white",activebackground="white")
        c6.grid(row=13,column=3)

        label1=Label(frame1,text="7. Did you travel internationally in the last two to three weeks?",bg="white",font=("Cambria",12)).grid(row=15,column=0,sticky=W)
        c7=Checkbutton(frame1,bg="white",variable=var7,command=lambda:click7(var7),activebackground="white")
        c7.grid(row=15,column=3)

        label1=Label(frame1,text="8. Do you have any severe underlying medical conditions?(Heart or lung disease,diabetes etc.)",bg="white",font=("Cambria",12)).grid(row=17,column=0,sticky=W)
        c8=Checkbutton(frame1,bg="white",variable=var8,command=lambda:click8(var8),activebackground="white")
        c8.grid(row=17,column=3)


        my_list=[]
        
        def click1(var1):
            global v1
            v1=var1
            return v1
        
        def click2(var2):
            global v2
            v2=var2
            return v2
            
        def click3(var3):
            global v3
            v3=var3
            return v3
        
        def click4(var4):
            global v4
            v4=var4
            return v4
    
        def click5(var5):
            global v5
            v5=var5
            return v5
        def click6(var6):
            global v6
            v6=var6
            return v6
        def click7(var7):
            global v7
            v7=var7
            return v7
        def click8(var8):
            global v8
            v8=var8
            return v8

        V1=click1(var1)
        V2=click2(var2)
        V3=click3(var3)
        V4=click4(var4)
        V5=click5(var5)
        V6=click6(var6)
        V7=click7(var7)
        V8=click8(var8)
        
        

        def submit():
            if(V1.get()==1):
                my_list.append(V1)
            else:
                pass
            if(V2.get()==1):
                my_list.append(V2)
            else:
                pass
            if(V3.get()==1):
                my_list.append(V3)
            else:
                pass
            if(V4.get()==1):
                my_list.append(V4)
            else:
                pass
            if(V5.get()==1):
                my_list.append(V5)
            else:
                pass
            if(V6.get()==1):
                my_list.append(V6)
            else:
                pass
            if(V7.get()==1):
                my_list.append(V7)
            else:
                pass
            if(V8.get()==1):
                my_list.append(V8)
            else:
                pass
            if(len(my_list)==0):
                controller.show_frame(Safe)
            else:
                pass
            if(len(my_list)==4):
                controller.show_frame(Average)
            else:
                pass
            if(len(my_list)>4):
                controller.show_frame(Risk)
            else:
                pass
            if(len(my_list)<4):
                controller.show_frame(NoRisk)
            else:
                pass
        def uncheck():
            c1.deselect()
            V1=0
            c2.deselect()
            V2=0
            c3.deselect()
            V3=0
            c4.deselect()
            V4=0
            c5.deselect()
            V5=0
            c6.deselect()
            V6=0
            c7.deselect()
            V7=0
            c8.deselect()
            V8=0
            my_list.clear()
        def sub_unch():
            submit()
            uncheck()

        btn=ttk.Button(frame1,text="SUBMIT",command=sub_unch).grid(row=19,column=2,sticky=E)

        
        def back_unch():
            controller.show_frame(Sym1)
            uncheck()

        button1 = ttk.Button(frame1, text='BACK',command=back_unch)
        button1.grid(row=19,column=0,sticky=W)
        
        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)


class Pov1(Frame):
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

        label =ttk.Label(self, text='This is the first page of Anti Pov', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
 
        button1 = ttk.Button(self, text='BACK',command=lambda : controller.show_frame(StartPage))
        button1.pack()
        button2=ttk.Button(self, text='NEXT',command=lambda : controller.show_frame(Pov2))
        button2.pack()

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)

class Pov2(Frame):
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

        label =ttk.Label(self, text='Second page-POV2', font=("Cambria",16,"bold"))
        label.pack(pady=10, padx=10)
 
        button1 = ttk.Button(self, text='BACK',command=lambda : controller.show_frame(Pov1))
        button1.pack()
        button2=ttk.Button(self, text='NEXT')

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)

class Safe(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        header=Label(self,text="YOU ARE SAFE!!!!",bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        label =ttk.Label(self, text='Second page-POV2', font=("Cambria",16,"bold"))
        label.pack(pady=10, padx=10)
 
        button1 = ttk.Button(self, text='CHECK AGAIN',command=lambda :controller.show_frame(Sym2))
        button1.pack()
        button2=ttk.Button(self, text='HOME', command=lambda: controller.show_frame(StartPage)).pack()

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)

class Average(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        header=Label(self,text="You look fine,but if you are concerned then you can go check it at the doctor",bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        label =ttk.Label(self, text='Second page-POV2', font=("Cambria",16,"bold"))
        label.pack(pady=10, padx=10)
 
        button1 = ttk.Button(self, text='CHECK AGAIN',command=lambda :controller.show_frame(Sym2))
        button1.pack()
        button2=ttk.Button(self, text='HOME', command=lambda: controller.show_frame(StartPage)).pack()

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)
class Risk(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        header=Label(self,text="HIGH RISK!!!",bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        label =ttk.Label(self, text='Second page-POV2', font=("Cambria",16,"bold"))
        label.pack(pady=10, padx=10)
 
        button1 = ttk.Button(self, text='CHECK AGAIN',command=lambda :controller.show_frame(Sym2))
        button1.pack()
        button2=ttk.Button(self, text='HOME', command=lambda: controller.show_frame(StartPage)).pack()

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)
class NoRisk(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        header=Label(self,text="The symptoms are normal",bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        label =ttk.Label(self, text='Second page-POV2', font=("Cambria",16,"bold"))
        label.pack(pady=10, padx=10)
 
        button1 = ttk.Button(self, text='CHECK AGAIN',command=lambda :controller.show_frame(Sym2))
        button1.pack()
        button2=ttk.Button(self, text='HOME', command=lambda: controller.show_frame(StartPage)).pack()

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