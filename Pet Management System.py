
class Pet:
    def __init__(self, name, animal_type, age): #__init__ is a constructor function
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def display_info(self):
        print(f"Pet Name: {self.name}")
        print(f"Type: {self.animal_type}")
        print(f"Age: {self.age} years")

# objects
pet1 = Pet("Tomi", "Dog", 5)
pet2 = Pet("Mano", "Cat", 3)

# Display pet info
pet1.display_info()
print()  # Blank line
pet2.display_info()



































#class and __init__ constructor

#Object creation

#Instance methods

#Attributes (name, type, age)

