#Assigbement 1
# Object-Oriented Programming (OOP) in Python

# Parent Class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name} and my power is {self.power} - I use it to protect {self.city}.")

    def fly(self):
        print(f"{self.name} is flying!")

    def save_city(self):
        print(f"{self.name} is saving {self.city}!")

# Child Class (inherits from Superhero)
class TeleportingSuperhero(Superhero):
    def teleport(self):
        print(f"{self.name} teleported to the crime scene!")

# Create objects
hero1 = Superhero("Invincible", "Super Strength", "Baltimore")
hero2 = TeleportingSuperhero("Sky Blaze", "Fire Control", "Chicago")

# Use methods
hero1.introduce()
hero1.fly()
hero1.save_city()
print("\n")
hero2.introduce()
hero2.teleport()
