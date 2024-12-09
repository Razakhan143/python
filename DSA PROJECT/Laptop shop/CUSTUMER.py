# import time
# from OWNER import Owner 

# class Customer(Owner):

#     def __init__(self):
#         pass



    
#     def gap(self): 
#         print("\n" * 10)

#     def get_input(self):
#         while True:
#             try:
#                 return int(input("Enter your choice: "))
#             except ValueError:
#                 print("Invalid input. Please enter a number.")

#     # Register function for creating a customer account
#     def registr(self):
#         print("                                         Hello Customer! Register yourself\n")
#         reguser = input("                                         Enter the Username: ")
#         regpass = input("                                         Enter the Password: ")

#         # Write customer credentials to 'customer.txt'
#         with open("customer.txt", "w") as reg:
#             reg.write(f"{reguser} {regpass}\n")

#         self.gap()
#         print("\nRegistration Successful\n")
#         print(f"<Hello> <{reguser}> ")
#         self.menu()

#     # Purchase a Laptop by entering details
#     def buying(self):
#         print("\nEnter the model of the Laptop you want to purchase:")
#         print("Note: Model should be in 'xxx - xxx' format")
#         comany_name = input("Model: ")

#         # Asking for payment details for purchasing
#         print("\n\nEnter the following Account details for Purchasing:\n")
#         full_name = input("Enter your Full Name: ")
#         account_no = input("Enter the 8-digit Credit Card Number (without spaces): ")
#         expire_m = input("Enter Expiry Month: ")
#         expire_d = input("Enter Expiry Day: ")
#         cvv = input("Enter the CVV Number: ")

#         self.gap()
#         print("                       ******************* Thanks for purchasing the Laptop! ************************ \n\n")

#     # Customer menu for selecting book categories
#     def menu(self):
#         while True:
#             self.gap()
#             print("        \t\t        ==================== Choose your desired Laptop_Company ======================")
#             print("                                                        1---HP")
#             print("                                                        2---Dell")
#             print("                                                        3---Lenovo")
#             print("                                                        4---Asus")
#             print("                                                        5---Apple")
#             print("                                                        6---EXIT")
#             print("                                                     Enter Your Choice:")

#             choice = self.get_input()

#             if choice == 1:
#                 self.gap()
#                 Owner.display_HP(self)  
#                 self.buying()
#             elif choice == 2:
#                 self.gap()
#                 Owner.display_Dell(self) 
#                 self.buying()
#             elif choice == 3:
#                 self.gap()
#                 Owner.display_Lenovo(self)  
#                 self.buying()
#             elif choice == 4:
#                 self.gap()
#                 Owner.display_Asus(self)  
#                 self.buying()
#             elif choice == 5:
#                 self.gap()
#                 Owner.display_Apple(self)  
#                 self.buying()
#             elif choice == 6:
#                 self.gap()
#                 print("                                    Thanks for Visiting Our Online Laptop Store!")
#                 break
#             else:
#                 print("                                 INVALID OPTION! Please try again...\n")
#                 time.sleep(1)






import time
from OWNER import Owner 

class Customer(Owner):
    def __init__(self):
        super().__init__()  # Ensure 'head' is initialized from the Owner class

    def gap(self): 
        print("\n" * 10)

    def get_input(self):
        while True:
            try:
                return int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Register function for creating a customer account
    def registr(self):
        print("                                         Hello Customer! Register yourself\n")
        reguser = input("                                         Enter the Username: ")
        regpass = input("                                         Enter the Password: ")

        # Write customer credentials to 'customer.txt'
        with open("customer.txt", "w") as reg:
            reg.write(f"{reguser} {regpass}\n")

        self.gap()
        print("\nRegistration Successful\n")
        print(f"<Hello> <{reguser}> ")
        self.menu()

    # Purchase a Laptop by entering details
    def buying(self):
        print("\nEnter the model of the Laptop you want to purchase:")
        print("Note: Model should be in 'xxx - xxx' format")
        comany_name = input("Model: ")

        # Asking for payment details for purchasing
        print("\n\nEnter the following Account details for Purchasing:\n")
        full_name = input("Enter your Full Name: ")
        account_no = input("Enter the 8-digit Credit Card Number (without spaces): ")
        expire_m = input("Enter Expiry Month: ")
        expire_d = input("Enter Expiry Day: ")
        cvv = input("Enter the CVV Number: ")

        self.gap()
        print("                       ******************* Thanks for purchasing the Laptop! ************************ \n\n")

    # Customer menu for selecting book categories
    def menu(self):
        while True:
            self.gap()
            print("        \t\t        ==================== Choose your desired Laptop_Company ======================")
            print("                                                        1---HP")
            print("                                                        2---Dell")
            print("                                                        3---Lenovo")
            print("                                                        4---Asus")
            print("                                                        5---Apple")
            print("                                                        6---EXIT")
            print("                                                     Enter Your Choice:")

            choice = self.get_input()

            if choice == 1:
                self.gap()
                Owner.display_HP(self)  
                self.buying()
            elif choice == 2:
                self.gap()
                Owner.display_Dell(self) 
                self.buying()
            elif choice == 3:
                self.gap()
                Owner.display_Lenovo(self)  
                self.buying()
            elif choice == 4:
                self.gap()
                Owner.display_Asus(self)  
                self.buying()
            elif choice == 5:
                self.gap()
                Owner.display_Apple(self)  
                self.buying()
            elif choice == 6:
                self.gap()
                print("                                    Thanks for Visiting Our Online Laptop Store!")
                break
            else:
                print("                                 INVALID OPTION! Please try again...\n")
                time.sleep(1)
