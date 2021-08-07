from faker import Faker
fake = Faker()

first_name = fake.first_name()#Imię
last_name = fake.last_name()#Nazwisko
email = fake.email()#Email
private_phone_number = fake.phone_number() #Prywatny numer telefonu
business_phone_number = fake.phone_number() # Służbowy numer telefonu
job = fake.job() #Praca co robi
company = fake.company() #Nazwa firmy

class BaseContact:
    def __init__(self, first_name, last_name, email, private_phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.private_phone_number= private_phone_number

        #Variables
        self._label_lenght = 0
    @property
    def label_lenght(self):
        self._label_lenght = print(f"Długość imienia i nazwiska to: {(len(first_name)) +(len(last_name))}")
        return self._label_lenght

    
    def contact(self):
        print(f'Wybieram prywatny numer {private_phone_number} i dzwonię do {first_name} {last_name}')
        
    

class BusinessContact(BaseContact):
    def __init__(self, company, job, business_phone_number, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.company =company
        self.job = job
        self.business_phone_number = business_phone_number
   
    def contact_business(self):
        print(f'Wybieram numer służbowy{business_phone_number} i dzwonię do {first_name} {last_name}')
    

Person_one = BaseContact(first_name, last_name, email, private_phone_number)
Person_one = BusinessContact(first_name, last_name, email, private_phone_number, company, job, business_phone_number)

Person_one.contact()
Person_one.contact_business()
Person_one.label_lenght

