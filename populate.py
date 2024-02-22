import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ModelProject5.settings')
import django
django.setup()
from testapp.models import Student
from faker import Faker
from random import *
fake=Faker()
def phoneindgen():
    d1= randint(6,9)
    num = str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        frollno=fake.random_int(min=1,max=999)
        fname=fake.name()
        fdob=fake.date()
        fmarks=fake.random_int(min=1,max=100)
        femail=fake.email()
        fphoneindgen=phoneindgen()
        faddress=fake.address()
        student_record = Student.objects.get_or_create(rollno=frollno,name=fname,dob=fdob,marks=fmarks,email=femail,phonenumber=fphoneindgen,address=faddress)
n = int(input("Enter the number of records to insert into the database: "))
populate(n)
print(f"{n} Records Inserted Successfully")
print('*'*30)
