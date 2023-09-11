from Car import Car
from Criteria import Criteria
from Renter import Renter
from CarRentalCompany import CarRentalCompany

# Create car rental facade
car_rental = CarRentalCompany()

# Create cars and add them to the car rental system
car1 = Car("Toyota", "Camry", "ABC123", "Economy", 50)
car2 = Car("Honda", "Civic", "XYZ789", "Economy", 55)
car3 = Car("Ford", "Mustang", "DEF456", "Luxury", 100)

car_rental.add_car(car1, None, None)  # Add car1 without date restrictions
car_rental.add_car(car2, None, None)  # Add car2 without date restrictions
car_rental.add_car(car3, None, None)  # Add car3 without date restrictions

# Create a renter
renter = Renter("Doe", "John", "DL12345", "1990-01-15")

# Define criteria
criteria = Criteria()
criteria.cost_criteria(60)  # Set maximum cost criteria

# Test renting a car
print("Renting a car:")
car_rental.rent_car(renter, "2023-09-15", criteria)

# Test returning a car
print("\nReturning the car:")
car_rental.return_car(renter, "2023-09-15")

# Check bookings
print("\nBookings:")
bookings = car_rental.get_bookings()
for booking in bookings:
    print(f"Renter: {booking.renter.first_name} {booking.renter.last_name}, Car: {booking.car.make} {booking.car.model}, Date: {booking.date}")
