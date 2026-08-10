customer_name=input("Enter customer name: ")
age=int(input("Enter age: "))
number_of_tickets=int(input("Enter number of tickets: ")) 
if(age<12):
    cost=(120*number_of_tickets)
elif(age>=12 and age<=59):
    cost=(200*number_of_tickets)
elif(age>=60):
    cost=(150*number_of_tickets)
if(number_of_tickets>=5):
    discount=(cost/100)*10
else:
    discount=0
print(f"Customer name: {customer_name}")
print(f"Age: {age}")
print(f"Number of tickets: {number_of_tickets}")
print(f"Cost: {cost}")
print(f"Discount: {discount}")
print(f"Total amount: {cost-discount}")


