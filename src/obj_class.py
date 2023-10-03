
#Task is to create a  Python program to represent vehicles using a class. Each car should have attributes for maximum speed and mileage.
# with Updating the class with the default color for all vehicles," white", then create a display method to show all the properties of an object
#and a methods to assign seating capacity to a vehicle.
# and create two objects that should have a max speed of 200kph and mileage of 50000kmpl with five seating capacities, 
#and another car object should have a max speed of 180kph and 75000kmpl with four seating capacities.

class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def seat_capacity(self, cap):
        self.cap = cap

    def display_properties(self):
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.cap)

# Creating objects of the Vehicle class
vehicle1 = Vehicle(200, 50000)
vehicle1.seat_capacity(5)
vehicle1.display_properties()

vehicle2 = Vehicle(180, 75000)
vehicle2.seat_capacity(4)
vehicle2.display_properties()