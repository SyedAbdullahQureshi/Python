
import datetime
import json

class BikeRental:
    def __init__(self, stock=0):
        self.stock = stock

    def display_stock(self):
        print(f"We have {self.stock} bikes available to rent.")
        return self.stock

    def rent_bike(self, quantity, rental_basis):
        if quantity <= 0:
            print("Number of bikes should be positive!")
            return None
        elif quantity > self.stock:
            print(f"Sorry! We have only {self.stock} bikes available to rent.")
            return None
        else:
            now = datetime.datetime.now()
            print(f"You have rented {quantity} bike(s) on {rental_basis} basis today at {now.hour} hours.")
            print("You will be charged $5 for each hour, $20 for a day, and $60 for a week.")
            print("We hope that you enjoy our service.")
            self.stock -= quantity
            return now

    def return_bike(self, request):
        rental_time, rental_basis, num_of_bikes = request
        bill = 0
        if rental_time and rental_basis and num_of_bikes:
            self.stock += num_of_bikes
            now = datetime.datetime.now()
            rental_period = now - rental_time
            if rental_basis == 'hourly':
                bill = round(rental_period.total_seconds() / 3600) * 5 * num_of_bikes
            elif rental_basis == 'daily':
                bill = round(rental_period.days) * 20 * num_of_bikes
            elif rental_basis == 'weekly':
                bill = round(rental_period.days / 7) * 60 * num_of_bikes
            
            if (3 <= num_of_bikes <= 5):
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7

            print(f"Thanks for returning your bike(s). Hope you enjoyed our service!")
            print(f"That would be ${bill}")
            return bill
        else:
            print("Are you sure you rented a bike with us?")
            return None

    def save_data(self, filename="shop.json"):
        with open(filename, 'w') as f:
            json.dump({"stock": self.stock}, f)

    def load_data(self, filename="shop.json"):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.stock = data.get("stock", 0)
        except (FileNotFoundError, json.JSONDecodeError):
            self.stock = 100  # Default stock

class Customer:
    def __init__(self):
        self.bikes = 0
        self.rental_basis = ""
        self.rental_time = 0

    def request_bike(self, shop, quantity, rental_basis):
        self.rental_time = shop.rent_bike(quantity, rental_basis)
        if self.rental_time:
            self.bikes = quantity
            self.rental_basis = rental_basis
        return self.rental_time

    def return_bike(self, shop):
        if self.rental_time and self.rental_basis and self.bikes:
            shop.return_bike((self.rental_time, self.rental_basis, self.bikes))
            self.bikes = 0
            self.rental_basis = ""
            self.rental_time = 0
        else:
            print("You don't have any bikes to return.")

    def save_data(self, filename="customer.json"):
        data = {
            "bikes": self.bikes,
            "rental_basis": self.rental_basis,
            "rental_time": self.rental_time.isoformat() if self.rental_time else None,
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_data(self, filename="customer.json"):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.bikes = data.get("bikes", 0)
                self.rental_basis = data.get("rental_basis", "")
                rental_time_str = data.get("rental_time")
                if rental_time_str:
                    self.rental_time = datetime.datetime.fromisoformat(rental_time_str)
                else:
                    self.rental_time = 0
        except (FileNotFoundError, json.JSONDecodeError):
            pass  # Keep default values if file doesn't exist or is empty

def main():
    shop = BikeRental()
    shop.load_data()
    customer = Customer()
    customer.load_data()

    while True:
        print("""
        ====== Bike Rental Shop ======
        1. Display available bikes
        2. Request a bike on hourly basis ($5 per hour)
        3. Request a bike on daily basis ($20 per day)
        4. Request a bike on weekly basis ($60 per week)
        5. Return a bike
        6. Exit
        """)

        choice = input("Enter choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue

        if choice == 1:
            shop.display_stock()
        
        elif choice == 2:
            try:
                num_of_bikes = int(input("How many bikes would you like to rent? "))
                customer.request_bike(shop, num_of_bikes, 'hourly')
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == 3:
            try:
                num_of_bikes = int(input("How many bikes would you like to rent? "))
                customer.request_bike(shop, num_of_bikes, 'daily')
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == 4:
            try:
                num_of_bikes = int(input("How many bikes would you like to rent? "))
                customer.request_bike(shop, num_of_bikes, 'weekly')
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == 5:
            customer.return_bike(shop)
        elif choice == 6:
            shop.save_data()
            customer.save_data()
            break
        else:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main() 
