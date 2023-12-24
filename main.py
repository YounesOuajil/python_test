from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database
import sqlite3


db = Database( "Employee.db")

pr=Tk()

pr.title('Système de gestion des employés')
pr.configure(bg="#283593")
pr.geometry('1240x580')
pr.resizable(width=False, height=False)

log_fr = Frame(pr , bg="#283593")
log_fr.place(x=0,y=0,width=1240,height=700)

photo=PhotoImage(file="C:\\Users\\youne\\Downloads\\logo.png.png")
espace=Label(log_fr, image=photo,bg="#283593")
espace.place(x=570,y=80)

#username label and text entry box
usernameLabel = Label(log_fr, text="Nom d'utilisateur",font=("Calibri",18,"bold"),background="#283593").place(x=520,y=180)
username = StringVar()
usernameEntry = Entry(log_fr, textvariable=username,width=20,font=("calibri,18")).place(x=520,y=220)  

#password label and password entry box
passwordLabel = Label(log_fr,text="Mot de passe",font=("Calibri",18,"bold"),background="#283593").place(x=540,y=260) 
password = StringVar()
passwordEntry = Entry(log_fr, textvariable=password,width=20,font=("calibri,18"), show='*').place(x=520,y=300)  


#def of login fonc
global  username1  #that's the given username
global  password1  #that's the given password
global  username2  #that's the given username
global  password2  #that's the given password

username1 = "admine" 
password1 = "123456"

username2 = "user" 
password2 = "654321"

def clear_nom_pass():
      username.set("")
      password.set("")

def test_entre():
    if   username.get()==username1 and  password.get()==password1 :
    
      
     
 
      

      name = StringVar()
      age = StringVar()
      job = StringVar()
      gender = StringVar()
      email = StringVar()
      mobile = StringVar()

     #--------------------->>>>entries frame
      ent_fr = Frame(pr , bg="#283593")
      ent_fr.place(x=0,y=0,width=360,height=510)

      title = Label(ent_fr,text="les informations des employés",font=("Calibri",18,"bold"),bg="#283593",fg="#000000")
      title.place(x=50,y=1)
      #-pour le nom
      lbl_name = Label(ent_fr,text="Nom :",font=("Calibri",16,"bold"),bg="#283593",fg="#000000")
      lbl_name.place(x=10,y=50)
      name_entr = Entry(ent_fr,textvariable =name ,width=20,font=("calibri,16"))
      name_entr.place(x=120,y=50)
      #-pour le trav secreter
      lbl_job = Label(ent_fr,text="Role :",font=("Calibri",16,"bold"),bg="#283593",fg="#000000")
      lbl_job.place(x=10,y=90)
      job_entr = Entry(ent_fr,textvariable = job,width=20,font=("calibri,16"))
      job_entr.place(x=120,y=90)
      #-pour le gen
      lbl_gender= Label(ent_fr,text="Sex :",font=("Calibri",16,"bold"),bg="#283593",fg="#000000")
      lbl_gender.place(x=10,y=130)
      choix_box_gender = ttk.Combobox(ent_fr,textvariable = gender,state="readonly",width=18,font=("Calibri",16,"bold"))
      choix_box_gender['values']=("Masculin","Féminin")
      choix_box_gender.place(x=120,y=130)
      #-pour l age
      lbl_age = Label(ent_fr,text="Age :",font=("Calibri",16,"bold"),bg="#283593",fg="#000000")
      lbl_age.place(x=10,y=170)
      age_entr = Entry(ent_fr,textvariable = age,width=20,font=("calibri,16"))
      age_entr.place(x=120,y=170)
      #-por l email
      lbl_email = Label(ent_fr,text="Emaile :",font=("Calibri",16,"bold"),bg="#283593",fg="#000000")
      lbl_email.place(x=10,y=210)
      email_entr = Entry(ent_fr,textvariable = email,width=20,font=("calibri,16"))
      email_entr.place(x=120,y=210)
      #-por l contacte
      lbl_contact = Label(ent_fr,text="Mobile :",font=("Calibri",16,"bold"),bg="#283593",fg="#000000")
      lbl_contact.place(x=10,y=250)
      contact_entr = Entry(ent_fr,textvariable = mobile,width=20,font=("calibri,16"))
      contact_entr.place(x=120,y=250)
      #-address
      lbl_address = Label(ent_fr,text="Adrress :",font=("Calibri",16,"bold"),bg="#283593",fg="#000000")
      lbl_address.place(x=10,y=290)
      addres_inser_place=Text(ent_fr,width=30,height=2,font=("Calibri",16,"bold"),bg="white",fg="#000000")
      addres_inser_place.place(x=10,y=330)

      def clear():
        name.set("")
        age.set("")
        job.set("")
        gender.set("")
        email.set("")
        mobile.set("")
        addres_inser_place.delete(1.0,END)

      #deffine add emp
      def add_employee():
           if name_entr.get() ==""   or  age_entr.get ==""   or  job_entr.get=="" or email_entr.get==""  or contact_entr.get==""  or choix_box_gender.get()=="" or email_entr.get=="" or addres_inser_place.get(1.0,END)=="":
              messagebox.showerror("Errore","Veuillez entrer toutes les valeurs")
              return
           db.insert(
             name_entr.get(),
             age_entr.get(), 
             job_entr.get(),
             email_entr.get(),
             choix_box_gender.get(),
             contact_entr.get(),
             addres_inser_place.get(1.0,END))
           messagebox.showinfo("Success","un nouvel employé a été ajouter")   
           clear()
           displayAll()
   

      def displayAll():
          vu.delete(*vu.get_children())
          for row in db.fetch():
             vu.insert("",END,values=row)      

      def clear():
         name.set("")
         age.set("")
         job.set("")
         gender.set("")
         email.set("")
         mobile.set("")
         addres_inser_place.delete(1.0,END)
     

      def delet():
         db.remouve(row[0])
         clear()
         displayAll()



      def update():
          if name_entr.get() ==""   or  age_entr.get ==""   or  job_entr.get=="" or email_entr.get==""  or contact_entr.get==""  or choix_box_gender.get()=="" or email_entr.get=="" or addres_inser_place.get(1.0,END)=="":
             messagebox.showerror("Errore","Veuillez entrer toutes les valeurs")
             return
          db.update(row[0],
                name_entr.get(),
                age_entr.get(), 
                job_entr.get(),
                email_entr.get(),
                choix_box_gender.get(),
                contact_entr.get(),
                addres_inser_place.get(1.0,END))
          messagebox.showinfo('success',"Les données ont été modifier avec succès") 
          clear()
          displayAll()

        #----------->buttons frame
      btn_fr = Frame(ent_fr,bg="#283593",bd=1,relief=SOLID)
      btn_fr.place(x=1,y=400,width=355,height=100)
        #----ajouter
      btnadd = Button (btn_fr, text = 'Ajouter',cursor='hand2' ,width=14, height=1, font=(" Calibri", 16) , fg='white', bg='#16a085' , command=add_employee).place(x=4,y=5)
        #----modifier
      btnUpd = Button (btn_fr,text = 'Modifier',cursor='hand2',width=14,height=1,font=(" Calibri", 16) ,fg='white',bg='#2980b9',command=update ).place(x=4,y=50)
        #----delt
      btndel = Button (btn_fr,text = 'Supprimer',cursor='hand2',width=14,height=1,font=(" Calibri ", 16) ,fg='white',bg='#c0392b',command=delet ).place(x=170,y=5)
        #----clear
      btnclr = Button (btn_fr,text = 'Effacer',cursor='hand2',width=14,height=1,font=(" Calibri", 16) ,fg='white',bg='#339c12',command=clear ).place(x=170,y=50)

     
        #------------->define
      def masquer():
        pr.geometry("360x580")
      def afficher():
        pr.geometry('1240x580')

      btnmasquer = Button(pr,text='Masquer',cursor='hand2',bg='#78909C',width=14,font=(" Calibri", 16),bd=1,command= masquer)
      btnmasquer.place(x=4,y=510)

      btnafficher = Button(pr,text='Afficher',cursor='hand2',bg="#455A64",width=14,font=(" Calibri", 16),bd=1,command=afficher)
      btnafficher.place(x=185,y=510)



      def getData(event):
         selected_row= vu.focus()
         data= vu.item(selected_row)
         global row
         row= data["values"]
         name.set(row[1])
         age.set(row[2])
         job.set(row[3])
         email.set(row[4])
         gender.set(row[5])
         mobile.set(row[6])
         addres_inser_place.delete(1.0,END) #sup le contenu qui deja exicte est le romplace avec row 7 car il a 2 line
         addres_inser_place.insert(END,row[7])



        #--------------->table vieu

      vieu_fr = Frame(pr,bg="white")
      vieu_fr.place(x=365,y=1,width=875,height=610)

      stl= ttk.Style()
      stl.configure("mystyle.Treeview",font=("calibri",13),rowheight=50)
      stl.configure("mystyle.Treeview.heading",font=('calibri',13))

      vu = ttk.Treeview(vieu_fr,columns=(1,2,3,4,5,6,7,8),style=('mystyle.Treeview'))
      vu.heading("1",text="ID")
      vu.column("1",width="40")

      vu.heading("2",text="NOM")
      vu.column("2",width="140")

      vu.heading("3",text="AGE")
      vu.column("3",width="50")

      vu.heading("4",text="ROLE")
      vu.column("4",width="120")

      vu.heading("5",text="EMAILE")
      vu.column("5",width="150")

      vu.heading("6",text="SEX")
      vu.column("6",width="90")

      vu.heading("7",text="MOBILE")
      vu.column("7",width="150")


      vu.heading("8",text="ADRRESS")
      vu.column("8",width="150")

      vu['show']= 'headings'#organise vieu
      vu.bind("<ButtonRelease-1>",getData)
      displayAll()
      vu.place(x=1,y=1,height=610,width=875)


      displayAll()
    elif username2 == username.get() and password2 == password.get() :    
      
     #####################################################################à
     
      user_id=StringVar()

      name2 = StringVar()
      age2 = StringVar()
      job2 = StringVar()
      gender2 = StringVar()
      email2 = StringVar()
      mobile2 = StringVar()
      id_serch= StringVar()
      entre_de_id=StringVar()

      ent_fr1 = Frame(log_fr, bg="#2c3e50")
      ent_fr1.place(x=0,y=0,width=1240,height=700)

      ti= Label(ent_fr1,text="Entrez votre ID pour rechercher",font=("Calibri",16,"bold"),bg="#2c3e50",fg="black").place(x=500,y=140)
      ti_ent=Entry(ent_fr1,textvariable=entre_de_id,width=20,font=("calibri,16")).place(x=540,y=210)
      
      
    

        
      def activ():


         def displ2():
           tv.delete(*tv.get_children())
           for row1 in db.ser(entre_de_id.get()):
            tv.insert("",END,value=row1)

         tree_frame = Frame(ent_fr1,bg="#2c3e50")
         tree_frame.place(x=1,y=1,width=1400,height=610)
         
         style= ttk.Style()
         style.configure("mystyle.Treeview",font=("calibri",13),rowheight=50)
         style.configure("mystyle.Treeview.heading",font=('calibri',13))

         tv = ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style='mystyle.Treeview')
       
         tv.heading("1",text="ID")
         tv.column("1",width="40")

         tv.heading("2",text="NOM")
         tv.column("2",width="140")

         tv.heading("3",text="AGE")
         tv.column("3",width="50")

         tv.heading("4",text="ROLE")
         tv.column("4",width="90")

         tv.heading("5",text="EMAILE")
         tv.column("5",width="120")

         tv.heading("6",text="SEX")
         tv.column("6",width="60")

         tv.heading("7",text="MOBILE")
         tv.column("7",width="100")


         tv.heading("8",text="ADRRESS")
         tv.column("8",width="190")
      
         tv["show"]="headings"
         tv.place(x=200,y=1,height=610,width=800)
        
         displ2()
         btnbackmain= Button(tree_frame, text="Retour",cursor='hand2', width=14, height=1, font=(" Calibri", 16) , fg='white', bg='#16a085', command =test_entre) 
         btnbackmain.place(x=1,y=1)
       

      
      btnserch= Button(ent_fr1, text="Rechercher",cursor='hand2', width=14, height=1, font=(" Calibri", 16) , fg='white', bg='#16a085', command =activ) 
      btnserch.place(x=540,y=280)
      
    
      


      ########################################################################à
           
    elif  username.get() =="admin" and password.get() != "123456":
        messagebox.showerror("Errore","Erreur de mot de passe")
        clear_nom_pass()
        return

    elif  username.get() !="admin" and password.get() == "123456":
        messagebox.showerror("Errore","Erreur de nom")
        clear_nom_pass()
        return
    elif  username.get() =="user" and password.get() != "654321":
        messagebox.showerror("Errore","Erreur de mot de passe")
        clear_nom_pass()
        return  
    elif  username.get() !="user" and password.get() == "654321":
        messagebox.showerror("Errore","Erreur de nom")
        clear_nom_pass()
        return
    elif  username.get() !="user" and username.get() !="admin" and password.get() != "654321" and password.get()  != "123456":
        messagebox.showerror("Errore","Erreur de nom et de mot de pass")
        clear_nom_pass()
        return    


#when you press this button, test_entre is called
btnlog= Button(log_fr, text="Entrer",cursor='hand2', width=14, height=1, font=(" Calibri", 16) , fg='white', bg='#E64A19', command =test_entre) 
btnlog.place(x=523,y=370)


pr.mainloop()
