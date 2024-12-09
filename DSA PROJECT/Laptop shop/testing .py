class Laptop:
    def __init__(self, brand, model, price, category):
        self.brand = brand
        self.model = model
        self.price = price
        self.category = category

    def get_model(self):
        return self.model

    def get_comapny(self):
        return self.brand

    def set_price(self, new_price):
        self.price = new_price

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Category: {self.category}")


class Node:
    def __init__(self, laptop):
        self.laptop = laptop
        self.next = None


class Owner:
    def __init__(self):
        self.head = None

    def add_laptop(self, new_laptop):
        new_node = Node(new_laptop)
        if not self.head:
            self.head = new_node
            print("\n\t\t\t\t\t\t First laptop added.")
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print("\n\t\t\t\t\t\t Laptop added successfully!")

    def remove_laptop(self, model_to_remove):
        if not self.head:
            print("\n\t\t\t\t\t\t No laptop to remove!")
            return

        if self.head.laptop.get_model() == model_to_remove:
            self.head = self.head.next
            print("\n\t\t\t\t\t\t Laptop removed successfully!")
            return

        current = self.head
        while current.next:
            if current.next.laptop.get_model() == model_to_remove:
                current.next = current.next.next
                print("\n\t\t\t\t\t\t Laptop removed successfully!")
                return
            current = current.next
        print("\n\t\t\t\t\t\t Laptop not found!")

    def modify_laptop(self, model_to_modify):
        if not self.head:
            print("\n\t\t\t No laptop to modify!")
            return

        current = self.head
        while current:
            if current.laptop.get_model() == model_to_modify:
                new_price = float(input("\t\t\t\t\t\t Enter new price: "))
                current.laptop.set_price(new_price)
                print("\n\t\t\t\t\t\t Laptop modified successfully!")
                return
            current = current.next
        print("\n\t\t\t\t\t\t Laptop not found!")

    def display_laptop(self):
        if not self.head:
            print("\n\t\t\t\t\t\t No laptops to display!")
            return

        print("\n\t\t\t\t\t\t List of laptops:")
        current = self.head
        while current:
            current.laptop.display_info()  # Call the display_info method of Laptop
            current = current.next

    def display_laptop_by_category(self, category):
        if not self.head:
            print("\n\t\t\t\t\t\t No laptops to display.")
            return

        print(f"\n\t\t\t\t\t\t List of {category} laptops:")
        current = self.head
        while current:
            if current.laptop.get_comapny() == category:  # Corrected comparison
                current.laptop.display_info()  # Call the display_info method of Laptop
            current = current.next

    def display_HP(self):
        self.display_laptop_by_category("HP")

    def display_Dell(self):
        self.display_laptop_by_category("Dell")

    def display_Lenovo(self):
        self.display_laptop_by_category("Lenovo")

    def display_Asus(self):
        self.display_laptop_by_category("Asus")

    def display_Apple(self):
        self.display_laptop_by_category("Apple")


# Testing the full functionality

# Create the Owner (linked list) object
owner = Owner()

# Add some laptops to the list
laptop1 = Laptop("HP", "HP-123", 50000, "Laptop")
laptop2 = Laptop("Dell", "Dell-456", 60000, "Laptop")
laptop3 = Laptop("Lenovo", "Lenovo-789", 55000, "Laptop")

owner.add_laptop(laptop1)
owner.add_laptop(laptop2)
owner.add_laptop(laptop3)

# Display all laptops
print("\n\t\t\t\t\t\t Displaying all laptops:")
owner.display_laptop()

# Display laptops by category
print("\n\t\t\t\t\t\t Displaying all HP laptops:")
owner.display_HP()  # Display all HP laptops

# Modify a laptop's price
owner.modify_laptop("HP-123")  # Modify price for HP-123 laptop

# Remove a laptop
owner.remove_laptop("Dell-456")  # Remove Dell-456 laptop

# Display all laptops after removal
print("\n\t\t\t\t\t\t Displaying all laptops after removal:")
owner.display_laptop()
