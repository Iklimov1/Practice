#class Point():
#    def __init__(self, x, y):
       # self.x = x
       # self.y = y

#p = Point(2, 8)
#print(f"The x value is {p.x}")
#print(f"The y value is {p.y}")

#another example to calculate the capacity on a flight 
#without overbooking passengers
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = [] #empty list of passengers
    #create method to add passengers
    def add_passenger(self, name):
        if not self.open_seats(): #aka if there arent open seats return false to break the adding of passengers
            return False
        self.passengers.append(name) #adds passengers name to the end of the list
        return True
    #create method that will say how many open seats there are before capacity
    def open_seats(self):
        # in order to calculate this, you need the capacity minus the length of the passenger list
        return self.capacity - len(self.passengers)
flight = Flight(3) #3 is the capacity (creating a limit for the flight)
people = ["harry", "ron", "hermione", "ginny"]
for person in people:#adding ppl to the flight
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight succesfully.")
    else:
        print(f"No available seats for {person} ")
