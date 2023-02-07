class clinic:   
    doctor={"doctor_name":"",
           "doctor_phone":" ",
           }
    patient={
        "patient_name":" ",
        "patient_id":0,
        "patient_phone":" ",
        "patient_appointement":0,
        "patient_age":0
   }
    nurse={"nurse_name": "",
          "nurse_no":" ",}
    def __init__(self,doctor_name,doctor_phone, patient_name,  patient_id,patient_phone, patient_appointement,patient_age,nurse_name,nurse_no) :
     
      self.patient["patient_name"]=patient_name
      self.patient["patient_age"]=patient_age
      self.patient["patient_appointement"]=patient_appointement
      self.patient["patient_id"]=patient_id
      self.patient["patient_phone"]=patient_phone
      self.nurse["nurse_name"]=nurse_name
      self.nurse["nurse_no"]=nurse_no
      self.doctor["doctor_name"]=doctor_name
      self.doctor["doctor_phone"]=doctor_phone
    def get_doctor_data(self):
        print("The doctor data is :\n")
        print(self.doctor.items(),"\n")
    def get_patient_data(self):
        print("The patient data is :\n")
        print(self.patient.items(),"\n")
        
    def get_nurse_data(self):
        print("The nurse data is :\n")
        print(self.nurse.items(),"\n")
    def get_doc_name(self):
        print("doctor name is : ",self.doctor["doctor_name"])
    def get_doc_phone(self):
        print("doctor num is : ",self.doctor["doctor_phone"])
    def get_pat_name(self):
        print("patient name is : ",self.patient["patient_name"])
    def get_doc_id(self):
        print("patient id  is : ",self.patient["doctor_id"])
    def get_pat_phone(self):
        print("patient phone is : ",self.patient["patient_phone"])
    def get_pat_app(self):
        print("patient appointement is : ",self.patient["patient_phone"])
    def get_pat_age(self):
        print("patient age is : ",self.patient["patient_age"])
    def get_nus_name(self):
        print("nurse name is : ",self.nurse["nurse_name"])
    def get_nus_phone(self):
        print("nurse phone is : ",self.nurse["nurse_no"])
    








doctorName=input("Enter doctor name:")
doctorNum=int(input("Enter doctor phone:"))
n=int(input("Enter the number of patient you will enter their data:"))

for i in range(0,n) :
  patient_name=input("Enter patient name:")
  patient_id=i
  patient_phone=int(input("Enter patient phone :"))
  patient_app=float(input("Enter patient appointement name:"))
  patient_age=int(input("Enter patient age:"))
  
nurse_name=input("Enter nurse name:")
nurse_num=input("Enter nurse phone:")

c=clinic(doctorName,doctorNum,patient_name,patient_id,patient_phone,patient_app,patient_age,nurse_name,nurse_num)
c.get_doctor_data()
c.get_patient_data()
c.get_nurse_data()
c.get_doc_name()
c.get_nus_name()

