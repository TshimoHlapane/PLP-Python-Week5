# Parent Class: Animal/Vehicle
class Movement:
    def move(self):
        pass  # Base method, will be overridden

# Child Class: F1Car
class F1Car(Movement):
    def move(self):
        print("Racing on the track! 🏎️💨")

# Child Class: Goat
class Goat(Movement):
    def move(self):
        print("Running around the field! 🐐")

# Child Class: Yacht
class Yacht(Movement):
    def move(self):
        print("Sailing on the water! ⛵️")

# Create objects
f1_car = F1Car()
goat = Goat()
yacht = Yacht()

# Call the move method
f1_car.move()  # Output: Racing on the track! 🏎️💨
goat.move()    # Output: Running around the field! 🐐
yacht.move()   # Output: Sailing on the water! ⛵️
