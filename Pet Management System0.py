class Pet:
    def __init__(self, name, animal_type, age):  # __init__ is a constructor function
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def display_info(self):
        print(f"\nPet Name: {self.name}")
        print(f"Type: {self.animal_type}")
        print(f"Age: {self.age} years")


# User se input lena
print("Enter details for first pet:")
name1 = input("Pet Name: ")
type1 = input("Pet Type (e.g., Dog, Cat): ")
age1 = int(input("Pet Age: "))

print("\nEnter details for second pet:")
name2 = input("Pet Name: ")
type2 = input("Pet Type (e.g., Dog, Cat): ")
age2 = int(input("Pet Age: "))

# Obj create
pet1 = Pet(name1, type1, age1)
pet2 = Pet(name2, type2, age2)

# pet info
pet1.display_info()
pet2.display_info()
