parking=(int(input("enter parking hours: ")))
if(parking<=2):
    charge = 30*parking
elif(parking>=3 and parking<=5):
    charge=25*parking
elif(parking>5):
    charge=20*parking
else:
    print("Invalid hours")
service=0
if(charge>150):
    sevice=20
print(f"Parking charge: {charge}")
print(f"Service charge: {service}")
print(f"Total amount: {charge+service}")
