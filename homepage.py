from email.policy import strict
from fileinput import filename
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random,os
import tempfile
from time import strftime


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.title('Billing Project Made by Vinod Kumar Sharma ,Using Python')
        self.root.geometry('1360x768+0+0')
        self.root.iconbitmap(r'img\icon.ico')

        #**********************Variables***********************
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.serch_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()




        #Product Category list
        self.Category=['Select Option','Clothing','LifeStyle','Mobiles']
        
        #sub category of Clothing

        self.SubCatClothing=['Pant','T-Shirt','Shirt']
        #pant
        self.pant=['Levis','Mufti','Spykar']
        self.prise_levis=5000
        self.prise_mufti=700
        self.prise_spykar=8000
        #T-shirt
        self.t_shirt=['Polo','RoadSter','JackJonse']
        self.prise_polo=1500
        self.prise_Roadster=1800
        self.prise_JackJones=1700
        #Shirt
        self.shirt=['Peter England','Louis Phillipe','Park Ayenue']
        self.prise_Peter=2100
        self.prise_Loui=2700
        self.prise_Park=1740

        #sub category of life style
        self.SubCatLifeStyle=['Bath Soap','Face Creame','Hair Oil']
        #bathshop
        self.bath_soap=['LifeBuy','Lux','Santoor','Pearl']
        self.prise_life=20
        self.prise_lux=20
        self.prise_santoor=20
        self.prise_pearl=30
        #Face Cream
        self.Face_cream=['Fair&Lovely','Ponds','Olay','Garnier']
        self.prise_fair=20
        self.prise_ponds=200
        self.prise_olay=20
        self.prise_garnier=30
        #Hair Oil
        self.Hair_oil=['Parachute','Jashmiin','Bajaj']
        self.prise_para=25
        self.prise_jashmin=22
        self.prise_bajaj=30


        #su category of Mobiles
        self.SubCatMobiles=['Iphone','Sumsung','Xiome','RealMe','One+']
        #Iphone
        self.Iphone=['Iphone-X','Iphone-11','Iphone-12']
        self.prise_ix=40000
        self.prise_i11=60000
        self.prise_i12=85000
        #Sumsung
        self.Sumsung=['Sumsung M16','Sumsung M12','sumsung M21']
        self.prise_sm16=16000
        self.prise_sm12=17000
        self.prise_sm21=18000
        #Xiome
        self.Xiome=['Red11','Redme-12','RedmePro']
        self.prise_r11=11000
        self.prise_r12=12000
        self.prise_rpro=13000
        #RealMe
        self.RealMe=['RealMe 12','RealMe 13','RealMe Pro']
        self.prise_rel_12=21000
        self.prise_rel13=22000
        self.prise_relpro=100000
        #one+
        self.OnePlus=['OnePlus1','OnePlus2','OnePlus3']
        self.prise_one1=45000
        self.prise_one2=50000
        self.prise_one3=55000
        
        #*****img 1`*************`

        img_1=Image.open('img/b1.jpg')
        img_1=img_1.resize((453,130))
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img=Label(self.root,image=self.photoimg_1)
        lbl_img.place(x=0,y=0,height=130,width=453)

        #*****img 2`*************`

        img_2=Image.open('img/girls.jpg')
        img_2=img_2.resize((453,130))
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img=Label(self.root,image=self.photoimg_2)
        lbl_img.place(x=455,y=0,height=130,width=453)


        #*****img 3`*************`

        img_3=Image.open('img/girl1.jpg')
        img_3=img_3.resize((453,130))
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        lbl_img=Label(self.root,image=self.photoimg_3)
        lbl_img.place(x=910,y=0,height=130,width=453)

        #******billing software***************
        lbl_title=Label(self.root,text='BILLING SOFTWARE USING PYTHON BY Wifi Google Gyan',font=('times new roman',30,'bold'),bg='white',fg='blue')
        lbl_title.place(x=0,y=130,width=1366,height=45)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(lbl_title,font=('times new roman',16,'bold'),bg='white',fg='DeepPink')
        lbl.place(x=0,y=0,width=120,height=45)
        time()

        #********** main Frame  **************
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg='white')
        Main_Frame.place(x=0,y=175,width=1357,height=593)

        #************1st frame***************
        Cust_Frame=LabelFrame(Main_Frame,text='Customer',font=('times new roman',12,'bold'),bg='white',fg='red')
        Cust_Frame.place(x=0,y=5,width=350,height=110)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=('times new roman',12,'bold'),bg='white')
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=('times new roman',12,'bold'),width=24)
        self.entry_mob.grid(row=0,column=1,sticky=W)

        self.lblCustName=Label(Cust_Frame,text="Customer Name ",font=('times new roman',12,'bold'),bg='white')
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=('times new roman',12,'bold'),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W)

        self.lblEmail=Label(Cust_Frame,text="Email ID ",font=('times new roman',12,'bold'),bg='white')
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=('times new roman',12,'bold'),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W)

        #******************Product Label frame*********************

        Product_Frame=LabelFrame(Main_Frame,text='Product',font=('times new roman',12,'bold'),bg='white',fg='red')
        Product_Frame.place(x=360,y=5,width=550,height=110)
        #Category
        self.lblCategory=Label(Product_Frame,text="Select Categories ",font=('times new roman',12,'bold'),bg='white')
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)
       
        self.Category_var=StringVar()
        self.Combo_category=ttk.Combobox(Product_Frame,value=self.Category,textvariable=self.Category_var,font=('times new roman',10,'bold'),state='readonly')
        self.Combo_category.current(0)
        self.Combo_category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_category.bind('<<ComboboxSelected>>',self.Categories)

        #sub Category
        self.lblSubCategory=Label(Product_Frame,text="Sub Categories ",font=('times new roman',12,'bold'),bg='white')
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.SubCategory_var=StringVar()
        self.ComboSubcategory=ttk.Combobox(Product_Frame,value=[''],textvariable=self.SubCategory_var,font=('times new roman',10,'bold'),state='readonly')
        self.ComboSubcategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubcategory.bind('<<ComboboxSelected>>',self.Product_add)
        #Product Name
        self.lblCategory=Label(Product_Frame,text="Product Name ",font=('times new roman',12,'bold'),bg='white')
        self.lblCategory.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,font=('times new roman',10,'bold'),state='readonly')
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind('<<ComboboxSelected>>',self.price)

        #price
        self.lblPrise=Label(Product_Frame,text="Prise ",font=('times new roman',12,'bold'),bg='white')
        self.lblPrise.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrise=ttk.Combobox(Product_Frame,textvariable=self.prices,font=('times new roman',10,'bold'),state='readonly')
        self.ComboPrise.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #Qty
        self.lblQty=Label(Product_Frame,text="Qty ",font=('times new roman',12,'bold'),bg='white')
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        
        self.txtQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('times new roman',12,'bold'),width=20)
        self.txtQty.grid(row=1,column=3,sticky=W)

        #serch 
        Serch_Frame=Frame(Main_Frame,bd=2,bg='white')
        Serch_Frame.place(x=920,y=5,width=420,height=50)

        self.lblBill=Label(Serch_Frame,text="Bill Number ",font=('times new roman',12,'bold'),bg='red',fg='white')
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry=ttk.Entry(Serch_Frame,textvariable=self.serch_bill,font=('times new roman',12,'bold'),width=20)
        self.txt_Entry.grid(row=0,column=1,padx=2,sticky=W)

        self.BtnSerch=Button(Serch_Frame,command=self.find_bill,text='Serch',font=('arial',15,'bold'),bg='blue',fg='white',width=10,cursor='hand2')
        self.BtnSerch.grid(row=0,column=2,padx=2)
        

        # center frame 

        MiddelFrame=Frame(Main_Frame,bd=10)
        MiddelFrame.place(x=10,y=120,width=900,height=340)



        #*****center 1`*************`

        img_center1=Image.open('img/good.jpg')
        img_center1=img_center1.resize((450,340))
        self.photoimg_center1=ImageTk.PhotoImage(img_center1)

        lbl_img=Label(MiddelFrame,image=self.photoimg_center1)
        lbl_img.place(x=0,y=0,height=340,width=450)

        #*****center1`*************`

        img_center2=Image.open('img/mall.jpg')
        img_center2=img_center2.resize((450,340))
        self.photoimg_center2=ImageTk.PhotoImage(img_center2)

        lbl_img=Label(MiddelFrame,image=self.photoimg_center2)
        lbl_img.place(x=450,y=0,height=340,width=450)


        #RightFrame Bill aria

        RightLabelFrame=LabelFrame(Main_Frame,Main_Frame,text='Bill Aria',font=('times new roman',12,'bold'),bg='white',fg='red')
        RightLabelFrame.place(x=920,y=45,width=425,height=345)
        
        Scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=Scroll_y.set,bg='white',fg='blue',font=('times new roman',12,'bold'))
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        #Bill counter label frame
        Bottom_Frame=LabelFrame(Main_Frame,Main_Frame,text='Bill Counter',font=('times new roman',12,'bold'),bg='white',fg='red')
        Bottom_Frame.place(x=0,y=390,width=1340,height=120)
        #sub total
        self.lblSubTotal=Label(Bottom_Frame,text="Sub Total ",font=('times new roman',12,'bold'),bg='white')
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        self.txtSubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=('times new roman',12,'bold'),width=20)
        self.txtSubTotal.grid(row=0,column=1,sticky=W)
        #gov tax
        self.lbl_tax=Label(Bottom_Frame,text="Tax",font=('times new roman',12,'bold'),bg='white')
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=('times new roman',12,'bold'),width=20)
        self.txt_tax.grid(row=1,column=1,sticky=W)
        #total
        self.lblAmountTotal=Label(Bottom_Frame,text="Total Amount",font=('times new roman',12,'bold'),bg='white')
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        
        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=('times new roman',12,'bold'),width=20)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W)

        #Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg='white')
        Btn_Frame.place(x=320,y=10)

        #add to cart
        self.BtnAddToCart=Button(Btn_Frame,text='Add To Cart',bd=10,height=1,font=('arial',15,'bold'),bg='orange',fg='white',width=12,cursor='hand2',command=self.additem)
        self.BtnAddToCart.grid(row=0,column=0,padx=2)

        #Generate Bill
        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,text='Generate Bill',bd=10,height=1,font=('arial',15,'bold'),bg='orange',fg='white',width=12,cursor='hand2')
        self.Btngenerate_bill.grid(row=0,column=1,padx=2)

        #Save bill
        self.Btnsave_bill=Button(Btn_Frame,command=self.save_bill,text='Save Bill',bd=10,height=1,font=('arial',15,'bold'),bg='orange',fg='white',width=10,cursor='hand2')
        self.Btnsave_bill.grid(row=0,column=2,padx=2)

        #Print
        self.Btn_print=Button(Btn_Frame,command=self.iprint,text='Print',bd=10,height=1,font=('arial',15,'bold'),bg='orange',fg='white',width=10,cursor='hand2')
        self.Btn_print.grid(row=0,column=3,padx=2)

        #Clear
        self.Btn_clear=Button(Btn_Frame,command=self.clear,text='Clear',bd=10,height=1,font=('arial',15,'bold'),bg='orange',fg='white',width=10,cursor='hand2')
        self.Btn_clear.grid(row=0,column=4,padx=2)

        #Exit
        self.Btn_exit=Button(Btn_Frame,text='Exit',command=self.root.destroy,bd=10,height=1,font=('arial',15,'bold'),bg='orange',fg='white',width=10,cursor='hand2')
        self.Btn_exit.grid(row=0,column=5,padx=2)

        #text area
        self.welcome()

        self.l=[]
    #*************Function declaration*****************

    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,'\tWelcome Wifi Google Gyan Moll')
        self.textarea.insert(END,f'\n Bill Number : {self.bill_no.get()}')
        self.textarea.insert(END,f'\n Customer Name : {self.c_name.get()}')
        self.textarea.insert(END,f'\n Phone Number : {self.c_phone.get()}')
        self.textarea.insert(END,f'\n Customer Email : {self.c_email.get()}')

        self.textarea.insert(END,'\n ===========================================')
        self.textarea.insert(END,'\n Products\t\tQTY\t\tPrice')
        self.textarea.insert(END,'\n ===========================================\n')

    def additem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=='':
            messagebox.showerror('Error','Please Select The product Name')
        else:
            self.textarea.insert(END,f'\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}')
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)-(self.prices.get()))*Tax)/100))))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+(((sum(self.l))-(self.prices.get()))*Tax)/100))))

    def gen_bill(self):
        if self.product.get()=='':
            messagebox.showerror('Error','Please Add To Cart Product')
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,'\n ===========================================')
            self.textarea.insert(END,f'\n Sub Amount :\t{self.sub_total.get()}')
            self.textarea.insert(END,f'\n Tax Amount :\t{self.tax_input.get()}')
            self.textarea.insert(END,f'\n Total Amount :\t{self.total.get()}')
            self.textarea.insert(END,'\n ===========================================\n')
    def save_bill(self):
        op=messagebox.askyesno('Save Bill','Do you want to save the Bill ?')
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open(r'bills/'+str(self.bill_no.get())+'.txt','w')
            f1.write(self.bill_data)
            op=messagebox.showinfo('Saved',f'Bill no  {self.bill_no.get()} saved successfully.')
            f1.close()
    def iprint(self):
        q=self.textarea.get(1.0,'end-1c')
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,'print')
    
    def find_bill(self):
        found="no"
        for i in os.listdir('bills/'):
            if i.split('.')[0]==self.serch_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found='yes'
        if found=='no':
            messagebox.showerror('Error','Invalid Bill Number')
    
    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set('')
        self.c_phone.set('')
        self.c_email.set('')
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.serch_bill.set('')
        self.product.set('')
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set('')
        self.sub_total.set('')
        self.tax_input.set('')
        self.welcome()

    def Categories(self,event=''):
        if self.Category_var.get()=='Clothing':#['Select Option','Clothing','LifeStyle','Mobiles']
            self.ComboSubcategory.config(value=self.SubCatClothing)
            self.ComboSubcategory.current(0)

        if self.Category_var.get()=='LifeStyle':
            self.ComboSubcategory.config(value=self.SubCatLifeStyle)
            self.ComboSubcategory.current(0)

        if self.Category_var.get()=='Mobiles':
            self.ComboSubcategory.config(value=self.SubCatMobiles)
            self.ComboSubcategory.current(0)
    
    def Product_add(self,event=''):
        #clothing : 'Pant','T-Shirt','Shirt'
        if self.SubCategory_var.get()=='Pant':
            self.ComboProduct.config(value=self.pant)
            self.ComboProduct.current(0)

        if self.SubCategory_var.get()=='T-Shirt':
            self.ComboProduct.config(value=self.t_shirt)
            self.ComboProduct.current(0)

        if self.SubCategory_var.get()=='Shirt':
            self.ComboProduct.config(value=self.shirt)
            self.ComboProduct.current(0)

        #Lifestyle : 'Bath Soap','Face Creame','Hair Oil'
        if self.SubCategory_var.get()=='Bath Soap':
            self.ComboProduct.config(value=self.bath_soap)
            self.ComboProduct.current(0)

        if self.SubCategory_var.get()=='Face Creame':
            self.ComboProduct.config(value=self.Face_cream)
            self.ComboProduct.current(0)

        if self.SubCategory_var.get()=='Hair Oil':
            self.ComboProduct.config(value=self.Hair_oil)
            self.ComboProduct.current(0)
        
        #Mobiles : 'Iphone','Sumsung','Xiome','RealMe','One+'
        if self.SubCategory_var.get()=='Iphone':
            self.ComboProduct.config(value=self.Iphone)
            self.ComboProduct.current(0)

        if self.SubCategory_var.get()=='Sumsung':
            self.ComboProduct.config(value=self.Sumsung)
            self.ComboProduct.current(0)

        if self.SubCategory_var.get()=='Xiome':
            self.ComboProduct.config(value=self.Xiome)
            self.ComboProduct.current(0)
        if self.SubCategory_var.get()=='RealMe':
            self.ComboProduct.config(value=self.RealMe)
            self.ComboProduct.current(0)

        if self.SubCategory_var.get()=='One+':
            self.ComboProduct.config(value=self.OnePlus)
            self.ComboProduct.current(0)
    def price(self,event=''):
        #Pant  : 'Levis','Mufti','Spykar'
        if self.ComboProduct.get()=='Levis':
            self.ComboPrise.config(value=self.prise_levis)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='Mufti':
            self.ComboPrise.config(value=self.prise_mufti)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='Spykar':
            self.ComboPrise.config(value=self.prise_spykar)
            self.ComboPrise.current(0)
            self.qty.set(1)
        #T-shirt : 'Polo','RoadSter','JackJonse'
        if self.ComboProduct.get()=='Polo':
            self.ComboPrise.config(value=self.prise_polo)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='RoadSter':
            self.ComboPrise.config(value=self.prise_Roadster)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='JackJonse':
            self.ComboPrise.config(value=self.prise_JackJones)
            self.ComboPrise.current(0)
            self.qty.set(1)
        #Shirt  : 'Peter England','Louis Phillipe','Park Ayenue'
        if self.ComboProduct.get()=='Peter England':
            self.ComboPrise.config(value=self.prise_Peter)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='Louis Phillipe':
            self.ComboPrise.config(value=self.prise_Loui)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='Park Ayenue':
            self.ComboPrise.config(value=self.prise_Park)
            self.ComboPrise.current(0)
            self.qty.set(1)
        #bathshop : 'LifeBuy','Lux','Santoor','Pearl'
        if self.ComboProduct.get()=='LifeBuy':
            self.ComboPrise.config(value=self.prise_life)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='Lux':
            self.ComboPrise.config(value=self.prise_lux)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='Santoor':
            self.ComboPrise.config(value=self.prise_santoor)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='Pearl':
            self.ComboPrise.config(value=self.prise_pearl)
            self.ComboPrise.current(0)
            self.qty.set(1)
        #Face Cream : 'Fair&Lovely','Ponds','Olay','Garnier'

        if self.ComboProduct.get()=='Fair&Lovely':
            self.ComboPrise.config(value=self.prise_fair)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='Ponds':
            self.ComboPrise.config(value=self.prise_ponds)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='Olay':
            self.ComboPrise.config(value=self.prise_olay)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='Garnier':
            self.ComboPrise.config(value=self.prise_garnier)
            self.ComboPrise.current(0)
            self.qty.set(1)
        #Hair Oil : 'Parachute','Jashmiin','Bajaj'
        if self.ComboProduct.get()=='Parachute':
            self.ComboPrise.config(value=self.prise_para)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='Jashmiin':
            self.ComboPrise.config(value=self.prise_jashmin)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='Bajaj':
            self.ComboPrise.config(value=self.prise_bajaj)
            self.ComboPrise.current(0)
            self.qty.set(1)
        #Iphone : 'Iphone-X','Iphone-11','Iphone-12'
        if self.ComboProduct.get()=='Iphone-X':
            self.ComboPrise.config(value=self.prise_ix)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='Iphone-11':
            self.ComboPrise.config(value=self.prise_i11)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='Iphone-12':
            self.ComboPrise.config(value=self.prise_i12)
            self.ComboPrise.current(0)
            self.qty.set(1)
        #Sumsung : 'Sumsung M16','Sumsung M12','sumsung M21'
        if self.ComboProduct.get()=='Sumsung M16':
            self.ComboPrise.config(value=self.prise_sm16)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='Sumsung M12':
            self.ComboPrise.config(value=self.prise_sm12)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='sumsung M21':
            self.ComboPrise.config(value=self.prise_sm21)
            self.ComboPrise.current(0)
            self.qty.set(1)
        #Xiome : 'Red11','Redme-12','RedmePro'
        if self.ComboProduct.get()=='Red11':
            self.ComboPrise.config(value=self.prise_r11)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='Redme-12':
            self.ComboPrise.config(value=self.prise_r12)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='RedmePro':
            self.ComboPrise.config(value=self.prise_rpro)
            self.ComboPrise.current(0)
            self.qty.set(1)
        #RealMe : 'RealMe 12','RealMe 13','RealMe Pro'
        if self.ComboProduct.get()=='RealMe 12':
            self.ComboPrise.config(value=self.prise_rel_12)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='RealMe 13':
            self.ComboPrise.config(value=self.prise_rel13)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='RealMe Pro':
            self.ComboPrise.config(value=self.prise_relpro)
            self.ComboPrise.current(0)
            self.qty.set(1)
        #one+ : 'OnePlus1','OnePlus2','OnePlus3'

        if self.ComboProduct.get()=='OnePlus1':
            self.ComboPrise.config(value=self.prise_one1)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='OnePlus2':
            self.ComboPrise.config(value=self.prise_one2)
            self.ComboPrise.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=='OnePlus3':
            self.ComboPrise.config(value=self.prise_one3)
            self.ComboPrise.current(0)
            self.qty.set(1)


       
        



if __name__=='__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()

