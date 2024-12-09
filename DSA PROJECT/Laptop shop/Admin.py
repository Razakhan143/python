import time
from OWNER import Owner
from LAPTOP import Laptop  


class Admin(Owner):
    
    def gap(self):
        print("\n" * 10)

    def get_input(self):
        while True:
            try:
                return int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")

    def login(self):
        self.gap()
        print("                                                Enter the Following Details:")
        user = input("                                                USERNAME : ")
        password = input("                                                PASSWORD : ")
        
        # Check credentials in a file (assuming 'login.txt' exists with credentials in 'username password' format per line)
        login_successful = False
        with open("login_details.txt", "r") as file:
            for line in file:
                u, p = line.strip().split()
                if u == user and p == password:
                    login_successful = True
                    break

        if login_successful:
            print(f"\nHello {user}\n<LOGIN SUCCESSFUL>")
            self.admin_menu()
        else:
            print("\n\t\t\t\t\t\tLOGIN ERROR!!!\n\t\t\t\t\t\tPlease check your username and password ....\n")
            input("Press Enter to try again...")
            self.login()  

    # Admin main menu for managing books
    def admin_menu(self):
        self.gap()
        print("                                       ***************** Welcome Admin  *******************")
        print("                                                    1---Inventory management")
        print("                                                    2---Exit")
        
        choice = self.get_input()
        if choice == 1:
            self.inventory()
        elif choice == 2:
            self.gap()
            print("                                   Thanks for Visiting Our Online Laptop Shop :) ")
        else:
            print("                                 INVALID OPTION! Please try again...\n")
            self.admin_menu()

    # Inventory management screen
    def inventory(self):
        active = True
        while active:
            self.gap()
            print("                                      ************* Welcome to Inventory Control *************")
            print("                                                        1-Adding Laptop")
            print("                                                        2-Removing Laptop")
            print("                                                        3-Update Price")
            print("                                                        4-Display Laptop are in Inventory")
            print("                                                        5-Back to Main Menu")

            choice = self.get_input()
            if choice == 1:
                self.add_latop()
            elif choice == 2:
                self.remove_latop()
            elif choice == 3:
                self.update_laptop_price()
            elif choice == 4:
                list_laptop=["HP","Dell","lenovo","Asus","Apple"]
                for laptop in list_laptop:
                    print(f"Laptop Mnufacturing Comany Name: {laptop}")
                    self.display_laptop_by_category(laptop)
            elif choice == 5:
                active = False
                self.admin_menu()
            else:
                print("                                 INVALID OPTION! Please try again...\n")
                time.sleep(2)

    # Add a Laptop
    def add_latop(self):
        print("\n\t\t\t\t\t\t   --> Enter Latop details")
        company = input("\t\t\t\t\t\t   --> Company Name: ")
        model = int(input("\t\t\t\t\t\t   --> MODEL Name: "))
        cpu_gpu = input("\t\t\t\t\t\t   --> Processor and GPU: ")
        ram_storage = input("\t\t\t\t\t\t   --> RAM/STORAGE: ")
        price = float(input("\t\t\t\t\t\t   --> Price: "))
        
        new_latop = Laptop(cpu_gpu, ram_storage, price, model, company)
        Owner.add_latop(new_latop)
        print("\t\t\t\t\t\t   --> Latop added successfully!\n")
        time.sleep(0.5)

    # Remove a latop by title
    def remove_latop(self):
        model = input("\t\t\t\t\t\t   --> Enter the model of the latop to remove: ")
        Owner.remove_latop(model)
        time.sleep(1)

    # Update the price of a latop by title
    def update_latop_price(self):
        model = input("\t\t\t\t\t\t   --> Enter the title of the latop to update its price: ")
        Owner.modify_latop(model)  
        time.sleep(1)

    # Display latop by category
    def display_latop_by_category(self):
        self.gap()
        print("                                ************* Choose Your Desired Latop Comapny Name *************")
        print("                                                        1---HP")
        print("                                                        2---Dell")
        print("                                                        3---Lenovo")
        print("                                                        4---Asus")
        print("                                                        5---Apple")
        print("                                                        6---Back to Inventory")

        choice = self.get_input()
        if choice == 1:
            self.gap()
            Owner.display_HP()
        elif choice == 2:
            self.gap()
            Owner.display_Dell()
        elif choice == 3:
            self.gap()
            Owner.display_Lenovo()
        elif choice == 4:
            self.gap()
            Owner.display_Asus()
        elif choice == 5:
            self.gap()
            Owner.display_Apple()
        elif choice == 6:
            self.inventory()
        else:
            print("                                 INVALID OPTION! Please try again...\n")
            time.sleep(1)
            self.display_Laptop_by_category()










