employee = ("Shyama", "Developer", 45000, 3)
name,designation,monthly_salary,experience=employee
annual_salary=monthly_salary*12
if(experience<2):
    bonus=annual_salary*0.05
elif(experience<=5):
    bonus=annual_salary*0.10
else:
    bonus=annual_salary*0.15
total_annual_compensation=annual_salary+bonus
print(f"Name: {name}")
print(f"Designation: {designation}")
print(f"Monthly Salary: {monthly_salary}")
print(f"Experience: {experience}")
print(f"Annual Salary: {annual_salary}")
print(f"Bonus: {bonus}")
print(f"Total Annual Compensation: {total_annual_compensation}")



