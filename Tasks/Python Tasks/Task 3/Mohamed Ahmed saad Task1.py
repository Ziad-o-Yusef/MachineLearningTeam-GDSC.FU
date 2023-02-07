class Doctor :
    __id_doc=0
    def __init__(self, name_doc, field) :
        self.name_doc=name_doc
        Doctor.__id_doc+=1
        self.field=field
    def __str__(self) :
        return f"Doctor Name : {self.name_doc}\nID: {self.__id_doc}\nField: {self.field} "
    def set_doc(self) :
        list_doc={"Dr: Mohamed ":"Eyes", "Dr: Ahmed":"stomach" , "Dr: Saad":"Teeth"}
        print("\nhere some Doctors...!\n")
        print("1-Dr: Mohamed  (eyes)\n2-Dr: Ahmed (stomach)\n3-Dr: Saad (Teeth)")
        choice=int(input("\n\npls enter your choice: "))
        if(choice >3 or choice<0):
            print("wrong choice")
        else :
            if(choice==1):
                print(f"ok, you can go to Dr: Mohamed his field: {list_doc['Dr: Mohamed ']}")
            elif(choice==2):
                print(f"ok, you can go to Dr: Ahmed his field: {list_doc['Dr: Ahmed']}")
            elif(choice==3) :
                print(f"ok, you can go to Dr: Saad hid Field: {list_doc['Dr: Saad']}")          
    
    def display_info_doc(self) :
        return f"Doctor Name : {self.name_doc}\nID: {self.__id_doc}\nField: {self.field}"

class patient :
    __id_patient=0
    def __init__(self, name_patient , address, HMH) :
        self.name_patient=name_patient;
        patient.__id_patient+=1
        self.address=address
        self.HMH=HMH     
        
    def display_info_patient(self) :
        return f"ok this is your info ,\nName: {self.name_patient}\nID:{self.__id_patient}\nAddress: {self.address}\nHis Medical History: {self.HMH}"
    
    def update_info(self, name , address, HMH) :
        self.name_patient=name;
        self.address=address
        self.HMH=HMH  
        print("Done..!")
    
class Account_Manager:
    def __init__(self, name_of_medicien , price) :
        self.name_of_medicien=name_of_medicien
        self.price=price
        
    def set_medicien(self):
        med={
            "acoomad50mg" : 100,
            "onkkaw321MG" : 50,
            "asomcdv50mg" : 10,
            "hiwmvw10mg" : 41
        }
        sum=0
        print("here yu will choose some mediciens...!")
        print("\n1-( acoomad50mg ) price : 100$ \n2-( onkkaw321MG ) price : 50$\n3-( asomcdv50mg ) price : 10$\n4-( hiwmvw10mg ) price : 41$")
        choice=int(input("\n\npls enter your choice: "))
        if(choice>4):
            print("wrong choice , try again")
        else :
            if(choice == 1):
                sum+=med["acoomad50mg"]
            elif (choice==2) :
                sum+=med["asomcdv50mg"]
            elif (choice==3):
                sum+=med["hiwmvw10mg"]
            elif (choice==4):
                sum+=med["onkkaw321MG"]        
        print(f"ok the total is: {sum} , good now you can go pay..!")            
                
       
    def get_medicien__info(self) :
        print(f"the medicien called :{self.name_of_medicien} his price is : {self.price}")

# class Display_all_info (Account_Manager , patient , Doctor) :
#     def __init__(self, name_of_medicien, price, name_patient , __id_patient, address, HMH,name_doc, __id_doc, field):
#         super().__init__(name_of_medicien, price)
#         super().__init__(name_patient , __id_patient, address, HMH)
#         super().__init__(name_doc, __id_doc, field)
        
#     def display_all(self) :
#         Doctor.display_info_doc()
#         patient.display_info_patient()
#         Account_Manager.get_medicien__info()



print("\t\t\tHi ,  wellcome in our Hospital..!\n")
name=input("wellcome pls enter your name here: ")
address=input("enter your address: ")
HMH=input("pls enter the history of Medical: ")
pat1=patient(name,address,HMH)
pat1.display_info_patient()
print("do you want to update or not..?")
print("1-yes\n2-no")
choice=int(input("your choice :"))
if(choice==1):
    name=input(" pls enter your new name here: ")
    address=input("enter your new address: ")
    HMH=input("pls enter the new  history of Medical: ")
    pat1.update_info(name,address,HMH)

print("what do you want to do...?\n ")
print("1-go to specific Doctor to check my illness\n2-buy some mediciens")
x=int(input("pls enter your choice: "))
if(x>2 or x <0):
    print("wrong choice , try again")
else :
    if(x==1):
       doc1=Doctor("Mohab" ,5,"arms")
       doc1.set_doc()
       
    elif(x==2) :
        ac1=Account_Manager("fevac35mg" ,5)
        ac1.set_medicien()
        
    
    
print("thank you for choose our hospital...!")  
    