import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ORM_InteQuest.settings')

# Configure Django settings
django.setup()


from demo.models import Employee
from django.db.models import Avg, Q

#FInd the Employee with Maximum Salery
print(Employee.objects.order_by('-esal')[0])

#FInd the Employee with Secound Highest Salery
print(Employee.objects.order_by('-esal')[1])

#Calculate Average Salery of Employee
print(Employee.objects.aggregate(Avg('esal')))

#Find Employee whose salery is greater than 3000
print(Employee.objects.filter(esal__gt=3000))

#Find Employee whose salery is greater than Equal to 3000
print(Employee.objects.filter(esal__gte=3000))

#Find all Employess whose dont have salery greater than 3000
print(Employee.objects.exclude(esal=3000))

#Find the Employees whose salery 3000 and name endswith a
print(Employee.objects.filter(Q(esal=3000) & Q(ename__endswith='a')))
print(Employee.objects.filter(Q(esal__gt=3000) & Q(ename__endswith='l')))
print(Employee.objects.filter(Q(esal=3000) & Q(ename__startswith='r')))

#Change the Salery of ram to 8000
Employee.objects.filter(ename='ram').update(esal=8000)

#Find If the Employee has salery has less than 3000 return True/False
print(Employee.objects.filter(esal__lt=3000).exists())

#Change Salery of all Employess to 6000
print(Employee.objects.all().update(esal=6000))