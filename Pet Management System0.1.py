class Pet:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def display_info(self):
        print(f"\nPet Name: {self.name}")
        print(f"Type: {self.animal_type}")
        print(f"Age: {self.age} years")


# Ya Empty list ha
pets = []

while True:
    print("\n===== Pet Management System =====")
    print("1. Add new pet")
    print("2. Show all pets")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        # Input new pet
        name = input("Enter pet name: ")
        pet_type = input("Enter pet type (Dog, Cat, etc.): ")
        age = int(input("Enter pet age: "))

        # Create object and store in list
        new_pet = Pet(name, pet_type, age)
        pets.append(new_pet)
        print("Pet added successfully!")

    elif choice == '2':
        if len(pets) == 0:
            print("No pets added yet.")
        else:
            print("\n--- All Pets ---")
            for pet in pets:
                pet.display_info()

    elif choice == '3':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
