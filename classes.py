class Company:
    def __init__(self,name,number,company_name):
        self.name = name
        self.number = number
        self.company_name = company_name
        
    def info(self):
        self.comp_name(self.company_name)
        print("Employe Name ", self.name)
        print("Employe Number ",self.number)
        
    def comp_name(self,company_name):
        self.company_name = company_name
        print("Company Name ",company_name)
        

class infoCom(Company):
    def __init__(self,name, number,company_name):
        super().__init__(name, number,company_name)
        self.dob = "3 Nov 2020"
        
    def welcome(self):
        self.info()
        print("Date of Joining",self.dob)
        
class Address(infoCom):
    pass

comp = Address("Birender",20418,'Bamko')
comp.welcome()        
