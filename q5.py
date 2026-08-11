seats=["Available", "Booked", "Available", "Available", "Booked", "Available", "Booked", "Available"]
for i in range(len(seats)):
    print(f"Seat {i+1}: {seats[i]}")
seat_number=int(input("Enter seat number: "))
if(seats[seat_number-1]=="Available"):
    seats[seat_number-1]=="Booked"
    print("Seat booked successfully")
else:
    print("Seat already booked")
    print(f"Seat: {seats}")
total_seats=len(seats)
booked_seats=seats.count("Booked")
available_seats=seats.count("Available")
print(f"Total seats: {total_seats}")
print(f"Booked seats: {booked_seats}")
print(f"Available seats: {available_seats}")    
