
from Admin import Admin
from CUSTUMER import Customer
from OWNER import Owner 
from LAPTOP import Laptop

import time  

def gap():
    # Prints blank lines to separate sections2
    print("\n" * 10)

def get_input():
    choice = input("Enter required input: ")
    return choice

def menu():
    gap()
    print("                    =========================== WELCOME TO Online Laptop STORE ===============================")
    print("                              ====================== Choose Your Role : ========================")
    print("                                                    1-Customer")
    print("                                                    2-Admin")
    print("                                                    3-Exit")
    choice = get_input()

    # Creating instances of Admin and Customer
    admin = Admin()
    customer = Customer()

    if choice == "1":
        gap()
        customer.registr()  # Assumes `register` is defined in Customer class

    elif choice == "2":
        # Admin login screen
        is_logged_in = False
        while not is_logged_in:
            gap()
            print("                       ************************ Welcome to Admin Portal ************************")
            print("                                                    1. LOGIN")
            print("                                                    2. EXIT")
            admin_choice = get_input()

            if admin_choice == "1":
                is_logged_in = admin.login() 
            elif admin_choice == "2":
                print("                                   \t    Thanks for using this program!")
                is_logged_in = True
            else:
                gap()
                print("                                 INVALID OPTION! Please try again...\n")
                time.sleep(1)
                
    elif choice == "3":
        gap()
        print("                                          Thanks for Visiting Our Online Laptop Store :)")

    else:
        gap()
        print("                                 INVALID OPTION! Please try again...\n")
        time.sleep(1)
        menu()  

if __name__ == "__main__":
    # Initialize an Owner and some predefined laptops
    owner = Owner()
    laptops_list = [
        # Apple Laptops

        Laptop("Apple", "MacBook Air 2014", 499, "4GB/128GB SSD", "Intel i3 4th Gen"),
        Laptop("Apple", "MacBook Pro 2015", 799, "8GB/256GB SSD", "Intel i5 5th Gen"),
        Laptop("Apple", "MacBook Air 2017", 899, "8GB/256GB SSD", "Intel i5 7th Gen"),
        Laptop("Apple", "MacBook Pro 2018", 1299, "16GB/512GB SSD", "Intel i7 8th Gen"),
        Laptop("Apple", "MacBook Pro 2019", 1499, "16GB/1TB SSD", "Intel i7 9th Gen"),
        Laptop("Apple", "MacBook Air 2020", 999, "8GB/256GB SSD", "Intel i3 10th Gen"),
        Laptop("Apple", "MacBook Pro 2020", 1599, "16GB/512GB SSD", "Intel i5 10th Gen"),
        Laptop("Apple", "MacBook Air M1 2020", 1249, "8GB/256GB SSD", "Apple M1"),
        Laptop("Apple", "MacBook Pro M1 2020", 1599, "16GB/512GB SSD", "Apple M1"),
        Laptop("Apple", "MacBook Pro 14 2021", 2399, "16GB/1TB SSD", "Apple M1 Pro"),
        Laptop("Apple", "MacBook Pro 16 2021", 3499, "32GB/1TB SSD", "Apple M1 Max"),
        Laptop("Apple", "MacBook Air M2 2022", 1399, "16GB/512GB SSD", "Apple M2"),
        Laptop("Apple", "MacBook Pro 13 2022", 1499, "16GB/512GB SSD", "Apple M2"),
        Laptop("Apple", "MacBook Pro 15 2023", 2899, "32GB/1TB SSD", "Apple M2 Max"),
        Laptop("Apple", "MacBook Air Retina", 1599, "8GB/256GB SSD", "Intel i5 11th Gen"),
        Laptop("Apple", "MacBook Pro Classic", 1099, "8GB/512GB SSD", "Intel i5 6th Gen"),


        
        # Lenovo Laptops
        Laptop("Lenovo", "IdeaPad S145", 399, "4GB/1TB HDD", "Intel i3 4th Gen"),
        Laptop("Lenovo", "ThinkPad T440", 499, "8GB/256GB SSD", "Intel i5 4th Gen"),
        Laptop("Lenovo", "IdeaPad 330", 599, "8GB/1TB HDD", "Intel i3 7th Gen"),
        Laptop("Lenovo", "Yoga 720", 749, "8GB/512GB SSD", "Intel i5 8th Gen"),
        Laptop("Lenovo", "IdeaPad Slim 3", 449, "4GB/128GB SSD", "Intel i3 10th Gen"),
        Laptop("Lenovo", "ThinkPad X250", 599, "8GB/256GB SSD", "Intel i5 7th Gen"),
        Laptop("Lenovo", "ThinkPad X1 Carbon", 1299, "16GB/512GB SSD", "Intel i7 10th Gen"),
        Laptop("Lenovo", "Legion Y530", 1099, "16GB/512GB SSD", "Intel i7 9th Gen"),
        Laptop("Lenovo", "Legion 7i", 1599, "16GB/1TB SSD", "Intel i9 11th Gen"),
        Laptop("Lenovo", "IdeaPad Flex 5", 699, "8GB/256GB SSD", "Intel i5 11th Gen"),
        Laptop("Lenovo", "ThinkPad E14", 949, "16GB/512GB SSD", "Intel i7 12th Gen"),
        Laptop("Lenovo", "IdeaPad Gaming 3", 1349, "16GB/512GB SSD", "Intel i7 12th Gen"),
        Laptop("Lenovo", "ThinkPad X1 Yoga", 2299, "16GB/1TB SSD", "Intel i9 12th Gen"),
        Laptop("Lenovo", "Yoga Slim 7", 1299, "16GB/512GB SSD", "Intel i7 12th Gen"),
        Laptop("Lenovo", "ThinkPad P15", 2499, "32GB/1TB SSD", "Intel i9 12th Gen"),
        
        # Dell Laptops
        Laptop("Dell", "Inspiron 14", 399, "4GB/500GB HDD", "Intel i3 4th Gen"),
        Laptop("Dell", "Inspiron 15", 499, "8GB/1TB HDD", "Intel i5 5th Gen"),
        Laptop("Dell", "Latitude 3490", 649, "8GB/512GB SSD", "Intel i3 8th Gen"),
        Laptop("Dell", "XPS 13 9370", 1249, "16GB/512GB SSD", "Intel i7 8th Gen"),
        Laptop("Dell", "Alienware 17 R4", 1899, "16GB/1TB SSD", "Intel i7 9th Gen"),
        Laptop("Dell", "Inspiron 14 2-in-1", 849, "8GB/512GB SSD", "Intel i5 10th Gen"),
        Laptop("Dell", "Inspiron 15 3000", 699, "8GB/256GB SSD", "Intel i3 10th Gen"),
        Laptop("Dell", "XPS 15 7590", 1599, "16GB/1TB SSD", "Intel i9 10th Gen"),
        Laptop("Dell", "XPS 13 9310", 1399, "16GB/512GB SSD", "Intel i7 11th Gen"),
        Laptop("Dell", "Alienware m15 R6", 2899, "32GB/1TB SSD", "Intel i9 12th Gen"),
        Laptop("Dell", "Latitude 7410", 1599, "16GB/512GB SSD", "Intel i7 12th Gen"),
        Laptop("Dell", "XPS 17", 2499, "32GB/1TB SSD", "Intel i9 12th Gen"),
        Laptop("Dell", "Inspiron 16", 899, "16GB/512GB SSD", "Intel i7 11th Gen"),
        Laptop("Dell", "Alienware Aurora R13", 3499, "64GB/2TB SSD", "Intel i9 13th Gen"),
        Laptop("Dell", "Precision 5550", 2299, "32GB/1TB SSD", "Intel i9 12th Gen"),
        
        # HP Laptops
        Laptop("HP", "Pavilion x360", 399, "4GB/1TB HDD", "Intel i3 4th Gen"),
        Laptop("HP", "ProBook 450 G2", 549, "8GB/256GB SSD", "Intel i5 5th Gen"),
        Laptop("HP", "EliteBook 840 G3", 799, "8GB/512GB SSD", "Intel i5 6th Gen"),
        Laptop("HP", "Envy 13", 949, "16GB/512GB SSD", "Intel i5 8th Gen"),
        Laptop("HP", "Spectre x360", 1599, "16GB/1TB SSD", "Intel i7 9th Gen"),
        Laptop("HP", "Omen 15", 1349, "16GB/512GB SSD", "Intel i7 10th Gen"),
        Laptop("HP", "Pavilion 15", 699, "8GB/512GB SSD", "Intel i5 10th Gen"),
        Laptop("HP", "ZBook Fury 15 G7", 3299, "32GB/1TB SSD", "Intel i9 10th Gen"),
        Laptop("HP", "Omen 17", 2599, "32GB/1TB SSD", "Intel i9 11th Gen"),
        Laptop("HP", "ProBook 450 G8", 999, "16GB/512GB SSD", "Intel i5 11th Gen"),
        Laptop("HP", "Pavilion Aero 13", 899, "16GB/512GB SSD", "Intel i7 11th Gen"),
        Laptop("HP", "ZBook Create G7", 2999, "32GB/1TB SSD", "Intel i9 11th Gen"),
        Laptop("HP", "Envy x360 15", 1249, "16GB/1TB SSD", "Intel i7 12th Gen"),
        Laptop("HP", "Spectre x360 14", 1999, "32GB/1TB SSD", "Intel i9 12th Gen"),
        Laptop("HP", "ProBook 650", 749, "8GB/256GB SSD", "Intel i3 10th Gen"),
        
        # Asus Laptops
        Laptop("Asus", "X540LA", 399, "4GB/500GB HDD", "Intel i3 4th Gen"),
        Laptop("Asus", "VivoBook 15 X540UA", 549, "8GB/1TB HDD", "Intel i5 6th Gen"),
        Laptop("Asus", "ZenBook 14 UX430", 799, "8GB/512GB SSD", "Intel i7 8th Gen"),
        Laptop("Asus", "TUF Gaming FX505", 999, "16GB/512GB SSD", "Intel i7 9th Gen"),
        Laptop("Asus", "ROG Zephyrus M", 1499, "16GB/1TB SSD", "Intel i9 9th Gen"),
        Laptop("Asus", "VivoBook S14", 899, "8GB/512GB SSD", "Intel i5 10th Gen"),
        Laptop("Asus", "ZenBook Flip 13", 1249, "16GB/512GB SSD", "Intel i7 10th Gen"),
        Laptop("Asus", "TUF Dash F15", 1549, "16GB/1TB SSD", "Intel i7 11th Gen"),
        Laptop("Asus", "ROG Zephyrus G14", 1799, "32GB/1TB SSD", "Intel i9 11th Gen"),
        Laptop("Asus", "ROG Strix G15", 1999, "32GB/1TB SSD", "Intel i9 12th Gen"),
        Laptop("Asus", "ZenBook Pro Duo", 3299, "32GB/1TB SSD", "Intel i9 12th Gen"),
        Laptop("Asus", "VivoBook 14", 599, "8GB/256GB SSD", "Intel i3 11th Gen"),
        Laptop("Asus", "ZenBook 15", 1499, "16GB/512GB SSD", "Intel i7 12th Gen"),
        Laptop("Asus", "ExpertBook B9", 1299, "16GB/512GB SSD", "Intel i7 12th Gen"),
        Laptop("Asus", "Chromebook Flip", 399, "4GB/64GB SSD", "Intel i3 7th Gen"),
    ]


    # Add laptop to owner's collection
    for laptop in laptops_list:
        owner.add_laptop(laptop)  
    owner.printing()
    # Display menu
    menu()
