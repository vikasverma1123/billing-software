from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.attributes('-fullscreen',True)
        self.root.title("Billing Software")
        bg_color="#00008B"
        
        title=Label(self.root,text="Neotia Hospital Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        #****Variables of all Tests*******#
        self.cbc = IntVar()
        self.bmp = IntVar()
        self.lp = IntVar()
        self.lft = IntVar()
        self.tft = IntVar()
        self.cp = IntVar()
        self.bct= IntVar()
        self.btrf =IntVar()
        self.im = IntVar()
        self.ht = IntVar()
        self.vbs= IntVar()
        self.bc = IntVar()
        self.mu=  IntVar()
        self.upt = IntVar()
        self.ru = IntVar()
        self.upt = IntVar()
        self.upT = IntVar()
        self.ucc = IntVar()
        self.uet = IntVar()
        self.uht = IntVar()
        self.udt = IntVar()
        self.utf= IntVar()
        self.xr = IntVar()
        self.ct = IntVar()
        self.mri = IntVar()
        self.us = IntVar()
        self.nmi= IntVar()
        self.fs= IntVar()
        self.mg = IntVar()
        self.ag = IntVar()
       

        #=========Total Price & Tax Variable============#
        self.product_price = StringVar()
        self.product_price_CGST = StringVar()
        self.product_price_GST = StringVar()

        #-========= Customer ========-#
        self.c_name = StringVar()
        self.c_age = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x=random.randint(1,999999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()


        #Customer Detail Frame
        F1 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Patient Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl = Label(F1,text="Patient Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt = Entry(F1,width=16,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cage_lbl = Label(F1,text="Age",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cage_txt = Entry(F1,width=10,textvariable=self.c_age,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        cphone_lbl = Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cphone_txt = Entry(F1,width=16,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

        cbill_lbl = Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=6,padx=20,pady=5)
        cbill_txt = Entry(F1,width=16,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=7,padx=10,pady=5)

        bill_btn = Button(F1,text="Search",command=self.find_bill,width=10,bd=7, font="arial 12 bold").grid(row=0,column=8,pady=10,padx=10)

        #Tests Frame

        F2 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Test Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=1005,height=400)
        
        #F3 = LabelFrame(F2,bd=10,relief=GROOVE,text="Vita",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        #F3.place(x=0,y=0,width=340,height=140)
        
        cbc_lbl= Label(F2,text='Complete Blood Count(CBC)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=0,sticky="w")
        cbc_txt=Entry(F2,width=10,textvariable=self.cbc,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        bmp_lbl= Label(F2,text='Basic Metabolic Panel(BMP)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=0,sticky="w")
        bmp_txt=Entry(F2,width=10,textvariable=self.bmp,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        # F4 = LabelFrame(F2,bd=10,relief=GROOVE,text="50-50",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        # F4.place(x=0,y=150,width=340,height=200)
        
        lp_lbl= Label(F2,text='Lipid Panel',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=0,sticky="w")
        lp_txt=Entry(F2,width=10,textvariable=self.lp,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        lft_lbl= Label(F2,text='Liver Functional Test(LFTs)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=0,sticky="w")
        lft_txt=Entry(F2,width=10,textvariable=self.lft,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=1)
        tft_lbl= Label(F2,text='Thyroid Functional Test',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=0,sticky="w")
        tft_txt=Entry(F2,width=10,textvariable=self.tft,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=1)
       
        '''bis_lbl= Label(F2,text='50-50(188g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=0,sticky="w")
        bis_txt=Entry(F2,width=10,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=1)
        bis_lbl= Label(F2,text='50-50(188g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=0,sticky="w")
        bis_txt=Entry(F2,width=10,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=1)'''

        #F5 = LabelFrame(F2,bd=10,relief=GROOVE,text="Marie",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        #F5.place(x=350,y=20,width=280,height=300)
        
        cp_lbl= Label(F2,text='Coagulation Panel',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=0,sticky="w")
        cp_txt=Entry(F2,width=10,textvariable=self.cp,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=1)
        bct_lbl= Label(F2,text='Blood Chemestry Test',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=0,padx=10,pady=0,sticky="w")
        bct_txt=Entry(F2,width=10,textvariable=self.bct,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=1)
        btrf_lbl= Label(F2,text='Blood Type & Rh Factor',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=7,column=0,padx=10,pady=0,sticky="w")
        btrf_txt=Entry(F2,width=10,textvariable=self.btrf,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=1)
        im_lbl= Label(F2,text='Inflammatory Markers',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=8,column=0,padx=10,pady=0,sticky="w")
        im_txt=Entry(F2,width=10,textvariable=self.im,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=8,column=1,padx=10,pady=1)
        ht_lbl= Label(F2,text='Hematology Tests',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=9,column=0,padx=10,pady=0,sticky="w")
        ht_txt=Entry(F2,width=10,textvariable=self.ht,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=9,column=1,padx=10,pady=1)
        vbs_lbl= Label(F2,text='Viral and Bacterial Serology',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=10,column=0,padx=10,pady=0,sticky="w")
        vbs_txt=Entry(F2,width=10,textvariable=self.vbs,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=10,column=1,padx=10,pady=1)

        bc_lbl = Label(F2,text='Blood Culture',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=3,padx=10,pady=0,sticky="w")
        bc_txt=Entry(F2,width=10,textvariable=self.bc,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=4,padx=10,pady=1)

        mu_lbl = Label(F2,text='Microscopic Urinalysis',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=3,padx=10,pady=0,sticky="w")
        mu_txt=Entry(F2,width=10,textvariable=self.mu,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=4,padx=10,pady=1)
        upt_lbl = Label(F2,text='Urinary Protein Tests',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=3,padx=10,pady=0,sticky="w")
        upt_txt=Entry(F2,width=10,textvariable=self.upt,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=4,padx=10,pady=1)
        ru_lbl = Label(F2,text='Routine Urinalysis',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=3,padx=10,pady=0,sticky="w")
        ru_txt=Entry(F2,width=10,textvariable=self.ru,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=4,padx=10,pady=1)

        upt_lbl = Label(F2,text='Urinary Protein Tests',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=3,padx=10,pady=0,sticky="w")
        upt_txt=Entry(F2,width=10,textvariable=self.upt,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=4,padx=10,pady=1)
        upt_lbl = Label(F2,text='Urinary pH Test',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=3,padx=10,pady=0,sticky="w")
        upt_txt=Entry(F2,width=10,textvariable=self.upT,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=4,padx=10,pady=1)
        ucc_lbl = Label(F2,text='Urinary Creatinine Clearance',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=3,padx=10,pady=0,sticky="w")
        ucc_txt=Entry(F2,width=10,textvariable=self.ucc,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=4,padx=10,pady=1)

        uet_lbl = Label(F2,text='Urinary Electrolyte Tests',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=7,column=3,padx=10,pady=0,sticky="w")
        uet_txt=Entry(F2,width=10,textvariable=self.uet,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=4,padx=10,pady=1)
        
        uht_lbl = Label(F2,text='Urinary Hormone Tests',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=8,column=3,padx=10,pady=0,sticky="w")
        uht_txt=Entry(F2,width=10,textvariable=self.uht,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=8,column=4,padx=10,pady=1)

        udt_lbl = Label(F2,text='Urinary Drug Tests',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=9,column=3,padx=10,pady=0,sticky="w")
        udt_txt=Entry(F2,width=10,textvariable=self.udt,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=9,column=4,padx=10,pady=1)
        utf_lbl = Label(F2,text='Urinary Tract Infection(UTI)Tests',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=10,column=3,padx=10,pady=0,sticky="w")
        utf_txt=Entry(F2,width=10,textvariable=self.utf,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=10,column=4,padx=10,pady=1)


        xr_lbl = Label(F2,text='X-ray',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=7,column=5,padx=10,pady=0,sticky="w")
        xr_txt=Entry(F2,width=10,textvariable=self.xr,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=6,padx=10,pady=1)

        ct_lbl = Label(F2,text='Computed Tomography(CT)Scan',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=5,padx=10,pady=0,sticky="w")
        ct_txt=Entry(F2,width=10,textvariable=self.ct,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=6,padx=10,pady=1)
        mri_lbl = Label(F2,text='Magnetic Resonance Imaging (MRI)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=5,padx=10,pady=0,sticky="w")
        mri_txt=Entry(F2,width=10,textvariable=self.mri,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=6,padx=10,pady=1)
        us_lbl = Label(F2,text='Ultrasound',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=5,padx=10,pady=0,sticky="w")
        us_txt=Entry(F2,width=10,textvariable=self.us,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=6,padx=10,pady=1)
        nmi_lbl = Label(F2,text='Nuclear Medicine Imaging',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=5,padx=10,pady=0,sticky="w")
        nmi_txt=Entry(F2,width=10,textvariable=self.nmi,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=6,padx=10,pady=1)
        fs_lbl = Label(F2,text='Fluoroscopy',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=5,padx=10,pady=0,sticky="w")
        fs_txt=Entry(F2,width=10,textvariable=self.fs,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=6,padx=10,pady=1)
        mg_lbl = Label(F2,text='Mammography',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=5,padx=10,pady=0,sticky="w")
        mg_txt=Entry(F2,width=10,textvariable=self.mg,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=6,padx=10,pady=1)
        ag_lbl = Label(F2,text='Angiography',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=5,padx=10,pady=0,sticky="w")
        ag_txt=Entry(F2,width=10,textvariable=self.ag,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=6,padx=10,pady=1)

        #************BILL AREA*******************
        F3 = Frame(self.root,bd=10,relief=GROOVE)
        F3.place(x=1010,y=180,width=520,height=400)
        bill_title = Label(F3,text='Bill Area',font="ariel 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F3,orient=VERTICAL)
        self.textarea = Text(F3,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #*************BUTTON***************#
        F4 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=0,y=585,relwidth=1,height=155)
        
        total_price = Label(F4,text='Total Price',bg=bg_color,fg="white",font=('times new roman',16,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt = Entry(F4,width=18,textvariable=self.product_price,font="arial 12 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        total_cgst = Label(F4,text='Total CGST',bg=bg_color,fg="white",font=('times new roman',16,"bold")).grid(row=0,column=3,padx=20,pady=1,sticky="w")
        m1_txt = Entry(F4,width=18,textvariable=self.product_price_CGST,font="arial 12 bold",bd=7,relief=SUNKEN).grid(row=0,column=4,padx=10,pady=5)

        total_gst = Label(F4,text='Total GST',bg=bg_color,fg="white",font=('times new roman',16,"bold")).grid(row=1,column=3,padx=20,pady=1,sticky="w")
        m1_txt = Entry(F4,width=18,textvariable=self.product_price_GST,font="arial 12 bold",bd=7,relief=SUNKEN).grid(row=1,column=4,padx=10,pady=5)
        
        btn_F = Frame(F4,bd=7,relief=GROOVE)
        btn_F.place(x=930,width=585,height=105)
        
        total_btn = Button(btn_F,command=self.Total,text="Total",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 12 bold").grid(row=0,column=0,padx=7,pady=10)
        generate_btn = Button(btn_F,command=self.bill_area,text="Generate Bill",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 12 bold").grid(row=0,column=1,padx=7,pady=10)
        clear_btn = Button(btn_F,command=self.clear_data,text="Clear",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 12 bold").grid(row=0,column=2,padx=7,pady=10)
        exit_btn = Button(btn_F,command=self.Exit_app,text="Exit",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 12 bold").grid(row=0,column=3,padx=7,pady=10)
        
        self.welcome_bill()
    
    def Total(self):
        self.cb_c=self.cbc.get()*120
        self.v418=self.bmp.get()*200
        self.b_50_29=self.lp.get()*150
        self.b_50_63=self.lft.get()*100
        self.t_f_t = self.tft.get()*340
        self.b_50_188=self.cp.get()*300
        self.m33=self.bct.get()*500
        self.m63=self.btrf.get()*180
        self.m190=self.im.get()*300
        self.m250=self.ht.get()*400
        self.m400=self.vbs.get()*550
        self.p24=self.bc.get()*250
        self.mc24=self.mu.get()*350
        self.g200=self.upt.get()*305
        self.gday27=self.ru.get()*500
        self.gday60=self.upt.get()*105
        self.gday200=self.upT.get()*350
        self.gkaju28=self.ucc.get()*500
        self.gkaju60=self.uet.get()*100
        self.gkaju200=self.uht.get()*350
        self.gchoco60=self.udt.get()*120
        self.milkbikis264=self.utf.get()*450
        self.burbun20=self.xr.get()*150
        self.burbun150=self.ct.get()*200
        self.tar150=self.mri.get()*400
        self.sfc300=self.us.get()*450
        self.sc100=self.nmi.get()*180
        self.oats150=self.fs.get()*190
        self.tg29=self.mg.get()*240
        self.tg43=self.ag.get()*540
       
        self.total_product_price=float(
                                        (self.cb_c)+
                                        (self.v418)+
                                        (self.b_50_29)+
                                        (self.b_50_63)+
                                        (self.t_f_t)+
                                        (self.b_50_188)+
                                        (self.m33)+
                                        (self.m63)+
                                        (self.m190)+
                                        (self.m250)+
                                        (self.m400)+
                                        (self.p24)+
                                        (self.mc24)+
                                        (self.g200)+
                                        (self.gday27)+
                                        (self.gday60)+
                                        (self.gday200)+
                                        (self.gkaju28)+
                                        (self.gkaju60)+
                                        (self.gkaju200)+
                                        (self.gchoco60)+
                                        (self.milkbikis264)+
                                        (self.burbun20)+
                                        (self.burbun150)+
                                        (self.tar150)+
                                        (self.sfc300)+
                                        (self.sc100)+
                                        (self.oats150)+
                                        (self.tg29)+
                                        (self.tg43)
                                    
        )  
        self.product_price.set("Rs. "+str(self.total_product_price))
        self.cgst_tax=round((self.total_product_price*0.09),2)
        self.product_price_CGST.set("Rs. "+str(self.cgst_tax))
        self.gst_tax = round((self.total_product_price*0.09),2)
        self.product_price_GST.set("Rs. "+str(self.gst_tax))

        self.Total_bill= float(round(self.total_product_price+
                               self.cgst_tax+
                               self.gst_tax
                               ))
    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t\tWELCOME NEOTIA HOSPITAL \n")
        self.textarea.insert(END,f"\n Bill Number  : {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Patient Name : {self.c_name.get()}")
        self.textarea.insert(END,f"\n Age          : {self.c_age.get()}")
        self.textarea.insert(END,f"\n Phone Number : {self.c_phone.get()}\n")
        self.textarea.insert(END,f"\n===========================================================")
        self.textarea.insert(END,f"\n Tests\t\t\t\tQTY\t\tPrice")  
        self.textarea.insert(END,f"\n===========================================================")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Patient details are not filled")
        elif self.product_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Tests is Purchased")
        else:
            self.welcome_bill()
            if self.cbc.get()!=0:
                self.textarea.insert(END,f"\n Complete Blood Count(CBC)\t\t\t\t{self.cbc.get()}\t\t{self.cb_c}")
            if self.bmp.get()!=0:
                self.textarea.insert(END,f"\n Basic Metabolic Panel(BMP)\t\t\t\t{self.bmp.get()}\t\t{self.v418}")
            if self.lp.get()!=0:
                self.textarea.insert(END,f"\n Lipid Panel\t\t\t\t{self.lp.get()}\t\t{self.b_50_29}")
            if self.lft.get()!=0:
                self.textarea.insert(END,f"\n Liver Functional Test(LFTs)\t\t\t\t{self.lft.get()}\t\t{self.b_50_63}")
            if self.tft.get()!=0:
                self.textarea.insert(END,f"\n Thyroid Functional Test(TFT)\t\t\t\t{self.tft.get()}\t\t{self.t_f_t}")
            if self.cp.get()!=0:
                self.textarea.insert(END,f"\n Coagulation Panel\t\t\t\t{self.cp.get()}\t\t{self.b_50_188}")
            if self.bct.get()!=0:
                self.textarea.insert(END,f"\n Blood Chemestry Test\t\t\t\t{self.bct.get()}\t\t{self.m33}")
            if self.btrf.get()!=0:
                self.textarea.insert(END,f"\n Blood Type & Rh Factor\t\t\t\t{self.btrf.get()}\t\t{self.m63}")
            if self.im.get()!=0:
                self.textarea.insert(END,f"\n Inflammatory Markers\t\t\t\t{self.im.get()}\t\t{self.m190}")
            if self.ht.get()!=0:
                self.textarea.insert(END,f"\n Hematology Tests\t\t\t\t{self.ht.get()}\t\t{self.m250}")
            if self.vbs.get()!=0:
                self.textarea.insert(END,f"\n Viral and Bacterial Serology\t\t\t\t{self.vbs.get()}\t\t{self.m400}")
            if self.bc.get()!=0:
                self.textarea.insert(END,f"\n Blood Culture\t\t\t\t{self.bc.get()}\t\t{self.p24}")
            if self.mu.get()!=0:
                self.textarea.insert(END,f"\n Microscopic Urinalysis\t\t\t\t{self.mu.get()}\t\t{self.mc24}")
            if self.upt.get()!=0:
                self.textarea.insert(END,f"\n Urinary Protein Tests\t\t\t\t{self.upt.get()}\t\t{self.g200}")
            if self.ru.get()!=0:
                self.textarea.insert(END,f"\n Routine Urinalysis\t\t\t\t{self.ru.get()}\t\t{self.gday27}")
            if self.upt.get()!=0:
                self.textarea.insert(END,f"\n Urinary Protein Tests\t\t\t\t{self.upt.get()}\t\t{self.gday60}")
            if self.upT.get()!=0:
                self.textarea.insert(END,f"\n Urinary pH Test\t\t\t\t{self.upT.get()}\t\t{self.gday200}")
            if self.ucc.get()!=0:
                self.textarea.insert(END,f"\n Urinary Creatinine Clearance\t\t\t\t{self.ucc.get()}\t\t{self.gkaju28}")
            if self.uet.get()!=0:
                self.textarea.insert(END,f"\n Urinary Electrolyte Tests\t\t\t\t{self.uet.get()}\t\t{self.gkaju60}")
            if self.uht.get()!=0:
                self.textarea.insert(END,f"\n Urinary Hormone Tests\t\t\t\t{self.uht.get()}\t\t{self.gkaju200}")
            if self.udt.get()!=0:
                self.textarea.insert(END,f"\n Urinary Drug Tests\t\t\t\t{self.udt.get()}\t\t{self.gchoco60}")
            if self.utf.get()!=0:
                self.textarea.insert(END,f"\n Urinary Tract Infection (UTI) Tests\t\t\t\t{self.utf.get()}\t\t{self.milkbikis264}")
            if self.xr.get()!=0:
                self.textarea.insert(END,f"\n X-ray\t\t\t\t{self.xr.get()}\t\t{self.burbun20}")
            if self.ct.get()!=0:
                self.textarea.insert(END,f"\n Computed Tomography (CT) Scan\t\t\t\t{self.ct.get()}\t\t{self.burbun150}")
            if self.mri.get()!=0:
                self.textarea.insert(END,f"\n Magnetic Resonance Imaging (MRI)\t\t\t\t{self.mri.get()}\t\t{self.tar150}")
            if self.us.get()!=0:
                self.textarea.insert(END,f"\n Ultrasound\t\t\t\t{self.us.get()}\t\t{self.sfc300}")  
            if self.nmi.get()!=0:
                self.textarea.insert(END,f"\n Nuclear Medicine Imaging\t\t\t\t{self.nmi.get()}\t\t{self.sc100}")  
            if self.fs.get()!=0:
                self.textarea.insert(END,f"\n Fluoroscopy\t\t\t\t{self.fs.get()}\t\t{self.oats150}")
            if self.mg.get()!=0:
                self.textarea.insert(END,f"\n Mammography\t\t\t\t{self.mg.get()}\t\t{self.tg29}")
            if self.ag.get()!=0:
                self.textarea.insert(END,f"\n Angiography\t\t\t\t{self.ag.get()}\t\t{self.tg43}")
            
            self.textarea.insert(END,f"\n-----------------------------------------------------------")
            if self.product_price_CGST.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Products CGST\t\t\t{self.product_price_CGST.get()}")
            if self.product_price_GST.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Products GST\t\t\t{self.product_price_GST.get()}")  
            self.textarea.insert(END,f"\n Total Bill \t\t\tRs. {self.Total_bill}")
            self.textarea.insert(END,f"\n-----------------------------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.textarea.get("1.0",END)

            if not os.path.exists("Bills"):
                os.makedirs("Bills")            
            f1=open("Bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No: {self.bill_no.get()} saved Successfully")
        else:
            return
        
    def find_bill(self):
        present="no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"Bills/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present='yes'
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")
    
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to Clear?")
        if op>0:
            
            self.cbc.set(0)
            self.bmp.set(0)
            self.lp.set(0)
            self.lft.set(0)
            self.tft.set(0)
            self.cp.set(0)
            self.bct.set(0)
            self.btrf.set(0)
            self.im.set(0)
            self.ht.set(0)
            self.vbs.set(0)
            self.bc.set(0)
            self.mu.set(0)
            self.upt.set(0)
            self.ru.set(0)
            self.upt.set(0)
            self.upT.set(0)
            self.ucc.set(0)
            self.uet.set(0)
            self.uht.set(0)
            self.udt.set(0)
            self.utf.set(0)
            self.xr.set(0)
            self.ct.set(0)
            self.mri.set(0)
            self.us.set(0)
            self.nmi.set(0)
            self.fs.set(0)
            self.mg.set(0)
            self.ag.set(0)

            #=========Total Price & Tax Variable============#
            self.product_price.set("")
            self.product_price_CGST.set("")
            self.product_price_GST.set("")

            #-========= Customer ========-#
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x=random.randint(1,999999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()
root=Tk()
obj = Bill_App(root)
root.mainloop()