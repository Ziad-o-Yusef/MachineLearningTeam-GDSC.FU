#!/usr/bin/env python
# coding: utf-8

# In[14]:


class doctor:
    def __init__(self,d_id,name,field):
        self.d_id=d_id
        self.name=name
        self.field=field
    def show_doctor_data(self):
    print(" doctor ID : " + str(self.d_id))
    print(" doctor name : " + str(self.name))
    print("doctor field : " + str(self.field))
  global database_p
  def access_p(self,p_id):
    return database_p[p_id]

# In[4]:


class patient:
    def __init__(self,p_id,name,phone,address,medical_history):
        self.p_id=p_id
        self.name=name
        self.phone=phone
        self.address=address
        self.medical_history=medical_history
def show_patient_data(self):
    print(" patient ID : " + str(self.p_id))
    print("patient name : " + str(self.name))
    print("patient phone: " + str(self.phone))
    print("patient address: " + str(self.address))
    print("patient medical_history: " + str(self.medical_history))
def update_record(self,record):
    self.medical_history=record
def add_note(self,note):
    self.note=note

# In[5]:


class account_manager:
    def __init__(self,a_id,name,phone,money):
        self.a_id=a_id
        self.name=name
        self.phone=phone
    def show_manager_data(self):
        print(" manager ID : " + str(self.a_id))
        print("manager name : " + str(self.name))
        print("manager phone: " + str(self.phone))
         print("manager money: " + str(self.money))
        


# In[24]:


doc_id=0
pat_id=0
mang_id=0
database_d={}
database_p={}
database_a={}
def moderator():
    global doc_id
    global pat_id
    global mang_id
    global database_p
    global database_d
    global database_a
    selection=int(input("choice doctor [1], choice patient [2], choice account_manager[3]"))
    if selection == 1:
        name=input("doctor name :")
        field=input('doctor field : ')
        doc_obj=doctor(d_id,name,field)
        d_id=doc_id
        doc_id=doc_id+1
        database[d_id]=doc_obj
        return d_id
        
    elif selection==2:
        name=input("patient name :")
        phone=int(input('patient phone : '))
        address=input("patient address :" )
        medical_history=input("patient history :")
        pat_obj=patient(p_id,name,phone,address,medical_history)
        p_id=pat_id
        pat_id=pat_id+1
        database[p_id]=pat_obj
        return p_id
    else:
        name=input("manager name :")
        phone=int(input('manager phone : '))
        mang_obj=account_manager(a_id,name,phone)
        a_id=mang_id
        mang_id=mang_id+1
        database[a_id]=mang_obj
        return a_id
        


# In[26]:


moderator()


# In[ ]:




