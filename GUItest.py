from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

LARGE_FONT = ("Times", 12)


def About():
       messagebox.showinfo("About","This GUI application is created by 5 students(Atiqur, Bivob, Arunabh, Saurav, Radai) of Jorhat Engineering College, Assam, India")
def Help():
       messagebox.showinfo("Help","This GUI application is created using Tkinter module in Python")
  
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
        
        
        submenu.add_command(label="Exit",command=quit)

        info=Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Info",menu=info)
        info.add_command(label="Coronatips",command=lambda:self.show_frame(CoronaTips))
        info.add_separator()
        info.add_command(label="COVID-19",command=lambda:self.show_frame(COVID))
        info.add_separator()
        info.add_command(label="Prevention",command=lambda:self.show_frame(Prevention))

        about=Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=about)
        about.add_command(label="About",command=About)
        about.add_separator()
        about.add_command(label="Help",command=Help)

        Tk.config(self,menu=menubar)

        self.frames = {} 
        for F in (StartPage, Sym1, Sym2, Pov1, Pov2,Safe,Warning, Risk, NoRisk, CoronaTips, COVID, Prevention):
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
        
        
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self, text="THIS IS THE FOOT-NOTE", font=("Verdana", 12,"bold"),bg="grey",fg="white",width="1520",height="3",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        
        photo3=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/test1.png"))
        lbl7=Label(self,image=photo3)
        lbl7.image=photo3
        lbl7.place(x=148,y=185)

        photo4=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/Poverty1.png"))
        lbl8=Label(self,image=photo4)
        lbl8.image=photo4
        lbl8.place(x=870,y=185)

        fram4 = LabelFrame(self,padx=30,pady=80,relief="solid",borderwidth=10,bg="white")
        fram4.place(x=150,y=302)
        label1=Label(fram4,text="It will only produce a speculated result based on the questions asked about your travel history, medical history etc. This tool can help you understand what to do next about COVID-19",wraplength=431,bg="white",font=("Cambria",16)).pack()

        button4=ttk.Button(fram4,text="CHECK",command=lambda : controller.show_frame(Sym1)).place(x=170,y=170)

        fram5 = LabelFrame(self,padx=29,pady=95,relief="solid",borderwidth=10,bg="white")
        fram5.place(x=870,y=297)
        label2=Label(fram5,text="This tool will help the below poverty line community with financial assisstance since their income sources has been cut-off with the onset of nationwide lockdown",wraplength=430,bg="white",font=("Cambria",16)).pack()
        button5=ttk.Button(fram5,text="PROCEED",command=lambda : controller.show_frame(Pov1)).place(x=180,y=160)

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)

        


        
                                                                                            
                                                            
 
class Sym1(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)
        
        header=Label(self,bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)
        
        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        frame1=LabelFrame(self,padx=50,pady=50,relief="solid",bg="white")
        frame1.place(x=330,y=250)
        lbl=Label(frame1,text="COVID-19 Screening Tool",bg="white",font=("Times",18,"bold"),anchor=W,justify=LEFT)
        lbl.grid(row=0,column=0,sticky=W)

        label=Label(frame1,bg="white").grid(row=1,column=0)
        label=Label(frame1,bg="white").grid(row=2,column=0)

        label=Label(frame1,text="-> You will answer a few questions about symptoms, travel etc.",wraplength=400,bg="white",font=("Times",14),anchor=W,justify=LEFT)
        label.grid(row=3,column=0,sticky=W)

        label=Label(frame1,bg="white").grid(row=4,column=0)

        label=Label(frame1,text="-> Your answers will not be shared publicly without your permission",wraplength=400,bg="white",font=("Times",14),anchor=W,justify=LEFT)
        label.grid(row=5,column=0,sticky=W)

        label=Label(frame1,bg="white").grid(row=6,column=0)

        label=Label(frame1,text="-> Recommendations provided by this tool do not constitute medical advice and should not be used to diagnose or treat medical conditions",wraplength=700,bg="white",font=("Times",14),anchor=W,justify=LEFT)
        label.grid(row=7,column=0,sticky=W)

        label=Label(frame1,bg="white").grid(row=8,column=0)
        label=Label(frame1,bg="white").grid(row=9,column=0)

        button1 = ttk.Button(frame1, text='BACK',command=lambda : controller.show_frame(StartPage))
        button1.grid(row=10,column=0,sticky=W)
        button2 = ttk.Button(frame1, text='PROCEED',command=lambda: controller.show_frame(Sym2))
        button2.grid(row=10,column=1,sticky=W)

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)

class Sym2(Frame):


    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        header=Label(self,text="CHECK IT!",font=("Times",18,"bold"),bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=5)
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)
        
        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        frame1=LabelFrame(self,padx=50,pady=50,relief="solid",bg="white")
        frame1.place(x=300,y=180)
        lbl=Label(frame1,text="Check your Symptoms", font=("Times",22,"bold"),bg="white").grid(row=0,column=0,sticky=W)
        label=Label(frame1,text="Symptoms may appear 2-14 days after exposure to the virus. People with these symptoms or combinations of symptoms may have COVID-19:",wraplength=700,bg="white",font=("Times",12,"bold"),anchor=W,justify=LEFT).grid(row=1,column=0,sticky=W)
        
        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()
        var9=IntVar()
        v1=IntVar()
        v2=IntVar()
        v3=IntVar()
        v4=IntVar()
        v5=IntVar()
        v6=IntVar()
        v7=IntVar()
        v8=IntVar()
        v9=IntVar()
        
        label1=Label(frame1,text="1. Dry Cough",bg="white",font=("Times",14)).grid(row=3,column=0,sticky=W)
        c1=Checkbutton(frame1,variable=var1,command=lambda:click1(var1),bg="white",activebackground="white")
        c1.grid(row=3,column=3)

        label1=Label(frame1,text="2. Shortness of breath/difficulty breathing",bg="white",font=("Times",14)).grid(row=5,column=0,sticky=W)
        c2=Checkbutton(frame1,variable=var2,command=lambda:click2(var2),bg="white",activebackground="white")
        c2.grid(row=5,column=3)

        label1=Label(frame1,text="3. Fever and chills",bg="white",font=("Times",14)).grid(row=7,column=0,sticky=W)
        c3=Checkbutton(frame1,variable=var3,command=lambda:click3(var3),bg="white",activebackground="white")
        c3.grid(row=7,column=3)

        label1=Label(frame1,text="4. Sore throat",bg="white",font=("Times",14)).grid(row=9,column=0,sticky=W)
        c4=Checkbutton(frame1,variable=var4,command=lambda:click4(var4),bg="white",activebackground="white")
        c4.grid(row=9,column=3)

        label1=Label(frame1,text="5. Muscle pain",bg="white",font=("Times",14)).grid(row=11,column=0,sticky=W)
        c5=Checkbutton(frame1,variable=var5,command=lambda:click5(var5),bg="white",activebackground="white")
        c5.grid(row=11,column=3)

        label1=Label(frame1,text="6. Chest Pain",bg="white",font=("Times",14)).grid(row=13,column=0,sticky=W)
        c6=Checkbutton(frame1,variable=var6,command=lambda:click6(var6),bg="white",activebackground="white")
        c6.grid(row=13,column=3)

        label1=Label(frame1,text="7. Did you travel internationally in the last two to three weeks?",bg="white",font=("Times",14)).grid(row=15,column=0,sticky=W)
        c7=Checkbutton(frame1,bg="white",variable=var7,command=lambda:click7(var7),activebackground="white")
        c7.grid(row=15,column=3)

        label1=Label(frame1,text="8. Do you have any severe underlying medical conditions?(Heart or lung disease,diabetes etc.)",bg="white",font=("Times",14)).grid(row=17,column=0,sticky=W)
        c8=Checkbutton(frame1,bg="white",variable=var8,command=lambda:click8(var8),activebackground="white")
        c8.grid(row=17,column=3)

        label=Label(frame1,bg="white").grid(row=18,column=0)

        def none():
            if(var9.get()==1):
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
                c1.config(state=DISABLED)
                c2.config(state=DISABLED)
                c3.config(state=DISABLED)
                c4.config(state=DISABLED)
                c5.config(state=DISABLED)
                c6.config(state=DISABLED)
                c7.config(state=DISABLED)
                c8.config(state=DISABLED)
            else:
                c1.config(state=ACTIVE)
                c2.config(state=ACTIVE)
                c3.config(state=ACTIVE)
                c4.config(state=ACTIVE)
                c5.config(state=ACTIVE)
                c6.config(state=ACTIVE)
                c7.config(state=ACTIVE)
                c8.config(state=ACTIVE)
            click9(var9)

        
        c9=Checkbutton(frame1,text="NO, I DO NOT HAVE ANY OF THE ABOVE SYMPTOMS",variable=var9,command=none)
        c9.grid(row=19,column=0)

        label=Label(frame1,bg="white").grid(row=20,column=0)
        

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
        def click9(var9):
            global v9
            v9=var9
            return v9

        V1=click1(var1)
        V2=click2(var2)
        V3=click3(var3)
        V4=click4(var4)
        V5=click5(var5)
        V6=click6(var6)
        V7=click7(var7)
        V8=click8(var8)
        V9=click9(var9)
        
        def no_symp():
            controller.show_frame(Safe)
            c1.config(state=ACTIVE)
            c2.config(state=ACTIVE)
            c3.config(state=ACTIVE)
            c4.config(state=ACTIVE)
            c5.config(state=ACTIVE)
            c6.config(state=ACTIVE)
            c7.config(state=ACTIVE)
            c8.config(state=ACTIVE)
            

        def submit():
            if(V9.get()==1):
                no_symp()
                V9.set("0")
            elif((V1.get()==0) and (V2.get()==0) and (V3.get()==0) and (V4.get()==0) and (V5.get()==0) and (V6.get()==0) and (V7.get()==0) and (V8.get()==0) and (V9.get()==0)):
                
                messagebox.showerror("Error!","You have not selected any field!!")
            else:
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
               
                if(len(my_list)==4):
                    controller.show_frame(Warning)
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


        btn=ttk.Button(frame1,text="SUBMIT",command=sub_unch).grid(row=22,column=2,sticky=E)

        
        def back_unch():
            controller.show_frame(Sym1)
            uncheck()
            V9.set("0")
            c1.config(state=ACTIVE)
            c2.config(state=ACTIVE)
            c3.config(state=ACTIVE)
            c4.config(state=ACTIVE)
            c5.config(state=ACTIVE)
            c6.config(state=ACTIVE)
            c7.config(state=ACTIVE)
            c8.config(state=ACTIVE)

        button1 = ttk.Button(frame1, text='BACK',command=back_unch)
        button1.grid(row=22,column=0,sticky=W)
        
        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)


class Pov1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        header=Label(self,text="INTRODUCTION",font=("Cambria",16,"bold"),bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        frame=LabelFrame(self,bg="white",padx=50,pady=50,borderwidth=5,relief="solid")
        frame.place(x=370,y=210)

        label =Label(frame, text='ABOUT & ELIGIBILITY', font=("Cambria",18,"bold"),bg="white")
        label.grid(row=0,column=1,sticky=W)

        label1=Label(frame,text="* This tool was conceived with the aim of providing financial assistance to economically backward community and to support them during the period of lockdown",wraplength=700,bg="white",font=("Cambria",14),anchor=W,justify=LEFT)
        label1.grid(row=1,column=1,sticky=W)
        label2=Label(frame,text="* This initiative is only for daily wage workers and other economically backward groups",wraplength=500,bg="white",font=("Cambria",14),anchor=W,justify=LEFT)
        label2.grid(row=2,column=1,sticky=W)
        label3=Label(frame,text="* How to apply: You have to fill up a form in the next page with your personal & family info, your financial background etc",wraplength=700,bg="white",font=("Cambria",14),anchor=W,justify=LEFT)
        label3.grid(row=3,column=1,sticky=W)
        label4=Label(frame,text="* Only one member from each family can apply",wraplength=500,bg="white",font=("Cambria",14),anchor=W,justify=LEFT)
        label4.grid(row=4,column=1,sticky=W)
        label5=Label(frame,text="* After submitting your form, we will contact you shortly after",wraplength=700,bg="white",font=("Cambria",14),anchor=W,justify=LEFT)
        label5.grid(row=5,column=1,sticky=W)
        button1 = ttk.Button(frame, text='GO BACK',command=lambda : controller.show_frame(StartPage))
        button1.grid(row=7,column=1,sticky=N)
        button2=ttk.Button(frame, text='APPLY',command=lambda : controller.show_frame(Pov2))
        button2.grid(row=6,column=1,sticky=N)

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)

class Pov2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        header=Label(self,text="REGISTRATION",font=("Cambria",16,"bold"),bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        name=StringVar()

        frame=LabelFrame(self,padx=20,pady=20,bg="white",borderwidth=5,relief="solid")
        frame.place(x=200,y=150)

        label =Label(frame, text='APPLICATION FORM(rudimentary)', font=("Cambria",18,"bold"),bg="white")
        label.grid(row=0,column=0,sticky=N)

        label1=Label(frame, text="'*' marked fields are compulsory",font=("Cambria",10),bg="white",anchor=W,justify=LEFT)
        label1.grid(row=1,column=0,sticky=W)

        label=Label(frame,bg="white").grid(row=2,column=0)

        label2=Label(frame, text="*Full Name",font=("Times",12),bg="white",anchor=W,justify=LEFT)
        label2.grid(row=3,column=0,sticky=W)

        entry1=ttk.Entry(frame,textvariable=name,width=50)
        entry1.grid(row=3,column=3)

        label=Label(frame,bg="white").grid(row=4,column=0)

        label2=Label(frame, text="*Gender",font=("Times",12),bg="white",anchor=W,justify=LEFT)
        label2.grid(row=5,column=0,sticky=W)

       
        var=IntVar()
        var.set("0")


        radio1=Radiobutton(frame,text="Male",bg="white",font=("Times",12),variable=var,value=1,activebackground="white")
        radio1.grid(row=5,column=1,sticky=W)

        radio2=Radiobutton(frame,text="Female",bg="white",font=("Times",12),variable=var,value=2,activebackground="white")
        radio2.grid(row=5,column=2,sticky=W)

        radio3=Radiobutton(frame,text="Others",bg="white",font=("Times",12),variable=var,value=3,activebackground="white")
        radio3.grid(row=5,column=3,sticky=W)

        label=Label(frame,bg="white").grid(row=6,column=0)

        label3=Label(frame,text="*Caste",bg="white",font=("Times",12),anchor=W,justify=LEFT)
        label3.grid(row=7,column=0,sticky=W)

        entry2=ttk.Entry(frame,width=30)
        entry2.grid(row=7,column=3)

        label=Label(frame,bg="white").grid(row=8,column=0)


        label4=Label(frame,text="*Source of income",bg="white",font=("Times",12),anchor=W,justify=LEFT)
        label4.grid(row=9,column=0,sticky=W)

        entry3=ttk.Entry(frame,width=30)
        entry3.grid(row=9,column=3)

        label=Label(frame,bg="white").grid(row=10,column=0)


        label5=Label(frame,text="*Family members(nos)",bg="white",font=("Times",12),anchor=W,justify=LEFT)
        label5.grid(row=11,column=0,sticky=W)

        entry4=ttk.Entry(frame,width=30)
        entry4.grid(row=11,column=3)

        label=Label(frame,bg="white").grid(row=12,column=0)

        label6=Label(frame,text="*Address",bg="white",font=("Times",12),anchor=W,justify=LEFT)
        label6.grid(row=13,column=0,sticky=W)

        entry5=ttk.Entry(frame,width=100)
        entry5.grid(row=13,column=3)

        label=Label(frame,bg="white").grid(row=14,column=0)

        label7=Label(frame,text="*Mobile Number",bg="white",font=("Times",12),anchor=W,justify=LEFT)
        label7.grid(row=15,column=0,sticky=W)

        entry6=ttk.Entry(frame,width=40)
        entry6.grid(row=15,column=3)

        label=Label(frame,bg="white").grid(row=16,column=0)
        label=Label(frame,bg="white").grid(row=17,column=0)

        def do_something():
            messagebox.showerror("Error!","You have not filled all the field(s)!!")


        def submit():
            if((len(entry1.get())==0) or (len(entry2.get())==0) or (len(entry3.get())==0) or (len(entry4.get())==0) or (len(entry5.get())==0) or (len(entry6.get())==0) or (var.get()==0)):
                do_something()
            else:
                messagebox.showinfo("Registration Successfull!!","Thank You "+name.get()+". We will contact you shortly for further details.")
                controller.show_frame(StartPage)
                entry1.delete(0,'end')
                entry2.delete(0,'end')
                entry3.delete(0,'end')
                entry4.delete(0,'end')
                entry5.delete(0,'end')
                entry6.delete(0,'end')
                var.set(None)

        def back():
            controller.show_frame(Pov1)
            entry1.delete(0,'end')
            entry2.delete(0,'end')
            entry3.delete(0,'end')
            entry4.delete(0,'end')
            entry5.delete(0,'end')
            entry6.delete(0,'end')
            var.set(None)




 
        button1 = ttk.Button(frame, text='BACK',command=back)
        button1.grid(row=20,column=2,sticky=N)
        button2=ttk.Button(frame, text='SUBMIT',command=submit)
        button2.grid(row=19,column=2,sticky=N)

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)



class Safe(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        header=Label(self,bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        frame=LabelFrame(self,padx=100,pady=100,bg="white",relief="solid",borderwidth=5)
        frame.place(x=200,y=200)

        label =Label(frame, text='SAFE',bg="white",font=("Times",38,"bold"))
        label.pack()

        label=Label(frame,bg="white").pack()

        label =Label(frame, text="You do not have symptoms typical to this infection. You are not infected. Stay safe and practice caution.",bg="white",wraplength=900,font=("Times",18,"bold"))
        label.pack()
        label=Label(frame,bg="white").pack()
        label=Label(frame,bg="white").pack()
        button1 = ttk.Button(frame, text='CHECK AGAIN',command=lambda :controller.show_frame(Sym2))
        button1.pack()
        button2=ttk.Button(frame, text='HOME', command=lambda: controller.show_frame(StartPage)).pack()

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)

class Warning(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        header=Label(self,bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        frame=LabelFrame(self,padx=50,pady=100,bg="white",relief="solid",borderwidth=5)
        frame.place(x=350,y=200)

        label =Label(frame, text='WARNING!!',bg="white",font=("Times",38,"bold"))
        label.pack()

        label=Label(frame,bg="white").pack()

        label =Label(frame, text='Your symptoms are not very serious. But they suggest that you might have some sort of infection. You should consult your doctor for further diagnosis.',bg="white",wraplength=900,font=("Times",18,"bold"))
        label.pack()
        label=Label(frame,bg="white").pack()
        label=Label(frame,bg="white").pack()
        button1 = ttk.Button(frame, text='CHECK AGAIN',command=lambda :controller.show_frame(Sym2))
        button1.pack()
        button2=ttk.Button(frame, text='HOME', command=lambda: controller.show_frame(StartPage))
        button2.pack()

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)
class Risk(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        header=Label(self,bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        frame=LabelFrame(self,padx=100,pady=100,bg="white",relief="solid",borderwidth=5)
        frame.place(x=300,y=200)

        label =Label(frame, text='WARNING!!',bg="white",font=("Times",38,"bold"))
        label.pack()

        label=Label(frame,bg="white").pack()

        label =Label(frame, text='Your symptoms look serious. Go and seek medical attention immediately.',bg="white",wraplength=900,font=("Times",18,"bold"))
        label.pack()
        label=Label(frame,bg="white").pack()
        label=Label(frame,bg="white").pack()
        button1 = ttk.Button(frame, text='CHECK AGAIN',command=lambda :controller.show_frame(Sym2))
        button1.pack()
        button2=ttk.Button(frame, text='HOME', command=lambda: controller.show_frame(StartPage)).pack()

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)

class NoRisk(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        header=Label(self,bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        frame=LabelFrame(self,padx=100,pady=100,bg="white",relief="solid",borderwidth=5)
        frame.place(x=250,y=200)

        label =Label(frame, text='NORMAL',bg="white",font=("Times",38,"bold"))
        label.pack()

        label=Label(frame,bg="white").pack()

        label =Label(frame, text="Your symptoms look normal. You are probably not infected. But practice extreme caution and prevention",bg="white",wraplength=900,font=("Times",18,"bold"))
        label.pack()
        label=Label(frame,bg="white").pack()
        label=Label(frame,bg="white").pack()
        button1 = ttk.Button(frame, text='CHECK AGAIN',command=lambda :controller.show_frame(Sym2))
        button1.pack()
        button2=ttk.Button(frame, text='HOME', command=lambda: controller.show_frame(StartPage)).pack()

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)




class Prevention(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        header=Label(self,bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        frame=LabelFrame(self,bg="white",padx=50,pady=30,relief="solid",borderwidth=5)
        frame.place(x=350,y=200)

        label=Label(frame, text='What You Can Do', font=("Times",18,"bold"),bg="white")
        label.grid(row=0,column=0)

        label=Label(frame,bg="white").grid(row=1,column=0)

        label=Label(frame, text='* Washing your hands is the best way to help you stay healthy. Wet your hands with clean, running water. Turn off the tap and apply soap. Lather your hands by rubbing them together. Get the backs of your hands, between your fingers, and under your nails. Scrub your hands for 20 seconds. Rinse your hands under clean, running water.',wraplength=700,anchor=W,justify=LEFT, font=("Times",14),bg="white")
        label.grid(row=2,column=0,sticky=W)

        label=Label(frame,bg="white").grid(row=3,column=0)

        label=Label(frame, text='* The main way COVID-19 spreads is between people. Physical distancing helps to stop the spread. Avoid physical contact with other people. Stay at least 6 feet away from people when outside your home.',wraplength=700,anchor=W,justify=LEFT, font=("Times",14),bg="white")
        label.grid(row=4,column=0,sticky=W)

        label=Label(frame,bg="white").grid(row=5,column=0)

        label=Label(frame, text='* If you have COVID-19 or have symptoms, isolate yourself in your home and stay away from others, including those in your household.',wraplength=700,anchor=W,justify=LEFT, font=("Times",14),bg="white")
        label.grid(row=6,column=0,sticky=W)

        label=Label(frame,bg="white").grid(row=7,column=0)

        label=Label(frame, text='* There is currently no vaccine or cure for COVID-19 but researchers are working to find one.',wraplength=700,anchor=W,justify=LEFT, font=("Times",14),bg="white")
        label.grid(row=8,column=0,sticky=W)

        label=Label(frame,bg="white").grid(row=9,column=3)
        label=Label(frame,bg="white").grid(row=10,column=3)

        button3=ttk.Button(frame, text='HOME',command=lambda : controller.show_frame(StartPage))
        button3.grid(row=11,column=1,sticky=W)

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)

class COVID(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        header=Label(self,bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)

        frame=LabelFrame(self,bg="white",padx=50,pady=50,relief="solid",borderwidth=5)
        frame.place(x=350,y=200)

        label=Label(frame, text='About COVID-19', font=("Times",18,"bold"),bg="white")
        label.grid(row=0,column=0)

        label=Label(frame,bg="white").grid(row=1,column=0)

        label=Label(frame, text='* COVID-19 is the new respiratory disease spreading around the world and it is caused by a coronavirus. COVID-19 is short for “coronavirus disease 2019.”',wraplength=700,anchor=W,justify=LEFT, font=("Times",14),bg="white")
        label.grid(row=2,column=0,sticky=W)

        label=Label(frame,bg="white").grid(row=3,column=0)

        label=Label(frame, text='* The virus is thought to spread mainly between people who are in close contact with one another (about 6 feet) and through respiratory droplets produced when an infected person coughs or sneezes.',wraplength=700,anchor=W,justify=LEFT, font=("Times",14),bg="white")
        label.grid(row=4,column=0,sticky=W)

        label=Label(frame,bg="white").grid(row=5,column=0)

        label=Label(frame, text='* People are most contagious when they are the sickest. But those who don’t have a lot of symptoms can still pass the virus on to others.',wraplength=700,anchor=W,justify=LEFT, font=("Times",14),bg="white")
        label.grid(row=6,column=0,sticky=W)

        label=Label(frame,bg="white").grid(row=7,column=0)

        label=Label(frame, text='* There is currently no vaccine or cure for COVID-19 but researchers are working to find one.',wraplength=700,anchor=W,justify=LEFT, font=("Times",14),bg="white")
        label.grid(row=8,column=0,sticky=W)

        label=Label(frame,bg="white").grid(row=9,column=3)
        label=Label(frame,bg="white").grid(row=10,column=3)

        button3=ttk.Button(frame, text='HOME',command=lambda : controller.show_frame(StartPage))
        button3.grid(row=11,column=1,sticky=W)

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)



class CoronaTips(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        header=Label(self,bg="grey",fg="white",width="1536",height="8")
        header.pack(padx=10,pady=10)
        
        photo2=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/Perfect1.png"))
        lbl7=Label(self,image=photo2)
        lbl7.image=photo2
        lbl7.place(x=0,y=125)

        footer=Label(self,bg="grey",fg="white",width="1520",height="5",anchor=N,justify=CENTER)
        footer.place(x=0,y=722)
        frame=LabelFrame(self,bg="white",padx=50,pady=50,relief="solid",borderwidth=5)
        frame.place(x=350,y=180)

        label=Label(frame, text='Supporting Yourself', font=("Times",18,"bold"),bg="white")
        label.grid(row=0,column=0)

        label=Label(frame,bg="white").grid(row=1,column=0)

        label=Label(frame, text='* Eat well-balanced meals. This means lots of fruits, vegetables, whole grains, and protein. Try to limit the amount of sugar and salt. Stay hydrated. Drink water with every meal, in between each meal, and when you work out. Make sure to sleep. Try to get seven to nine hours if possible.',wraplength=700,anchor=W,justify=LEFT, font=("Times",14),bg="white")
        label.grid(row=2,column=0,sticky=W)

        label=Label(frame,bg="white").grid(row=3,column=0)

        label=Label(frame, text='* Exercise, stretch, or take walks outside while practicing physical distancing. Movement can raise your level of endorphins, the chemicals that promote a positive mindset.',wraplength=700,anchor=W,justify=LEFT, font=("Times",14),bg="white")
        label.grid(row=4,column=0,sticky=W)

        label=Label(frame,bg="white").grid(row=5,column=0)

        label=Label(frame, text='* Practice mindfulness, which can help you stay calm. Various meditation apps are offering free services and specific COVID-19 programming.',wraplength=700,anchor=W,justify=LEFT, font=("Times",14),bg="white")
        label.grid(row=6,column=0,sticky=W)

        label=Label(frame,bg="white").grid(row=7,column=0)

        label=Label(frame, text='* Limit your trips to the grocery store or pharmacy as much as possible. When you go, try to only buy what you need to be sure there’s enough for everyone else.',wraplength=700,anchor=W,justify=LEFT, font=("Times",14),bg="white")
        label.grid(row=8,column=0,sticky=W)

        label=Label(frame,bg="white").grid(row=9,column=3)
        

        button3=ttk.Button(frame, text='HOME',command=lambda : controller.show_frame(StartPage))
        button3.grid(row=11,column=1,sticky=W)

        photo1=ImageTk.PhotoImage(Image.open("C:/Users/Atiqur/Desktop/GuiApp/New.png"))
        lbl6=Label(self,image=photo1)
        lbl6.image=photo1
        lbl6.place(x=30,y=20)



app = MainWindow()
app.mainloop()