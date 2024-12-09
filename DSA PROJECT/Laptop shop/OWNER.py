from LAPTOP import Laptop
class Node(Laptop):
    def __init__(self, laptop):
        self.laptop = laptop
        self.next = None

class Owner(Laptop):
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
        print("\n\t\t\t\t\t Laptop added successfully!")
    


    # Remove a Laptop from the linked list by title
    def remove_laptop(self, model_to_remove):
        if not self.head:
            print("\n\t\t\t\t\t\t No laptop to Remove!")
            return

        if self.head.laptop.get_model() == model_to_remove:
            self.head = self.head.next
            print("\n\t\t\t\t\t\t Laptop Removed Successfully!")
            return

        current = self.head
        while current.next:
            if current.next.laptop.get_model() == model_to_remove:
                current.next = current.next.next
                print("\n\t\t\t\t\t\t Laptop Removed Successfully!")
                return
            current = current.next
        print("\n\t\t\t\t\t\t Laptop Not Found!")

    # Modify a book in the linked list by title
    def modify_laptop(self, model_to_modify):
        if not self.head:
            print("\n\t\t\t No Laptop to Modify!")
            return

        current = self.head
        while current:
            if current.laptop.get_model() == model_to_modify:  
                new_price = float(input("\t\t\t\t\t\t Enter New Price: "))
                current.laptop.set_price(new_price)
                print("\n\t\t\t\t\t\t Laptop Modified Successfully!")
                return
            current = current.next
        print("\n\t\t\t\t\t\t Laptop Not Found!")


    # Display all laptops in the linked list
    def display_laptop(self):
        
        if not self.head:
            print("\n\t\t\t\t\t\t No Laptop to Display!")
            return

        print("\n\t\t\t\t\t\t List of Laptops:")
        current = self.head
        while current:
            current.laptop.display_info()
            current = current.next

    # # Display laptops by category
    def display_laptop_by_category(self, category):
        print(f"\n\t\t\t\t\t\t List of {category} Laptops:")
        current = self.head
        if current:
            print("\n\t\t\t\t\t\t No laptop to Display.")
            return
        while current:
            if current.laptop.model == category:
                current.laptop.display_info()
            current = current.next
    # def display_laptop(self):
    #     if not self.head:
    #         print("\nNo laptops to display!")
    #         return

    #     print("\nList of laptops:")
    #     current = self.head
    #     while current:
    #         current.laptop.display_info()
    #         current = current.next

    # def display_laptop_by_category(self, category):
    #     if not self.head:
    #         pass
    #     if not hasattr(self, 'head'):
    #         print("\nError: This function requires an Owner object.")
    #         return

    #     print(f"\n\t\t\t\t\t\t List of {category} Laptops:")
    #     current = self.head
    #     found = False
    #     while current:
    #         if current.laptop.get_company() == category:
    #             current.laptop.display_info()
    #             found = True
    #         current = current.next
    #     if not found:
    #         print(f"\n\t\t\t\t\t\t No laptops found in the category: {category}.")



    def printing(self):
        current = self.head
        while current.next:
            current = current.next
            print(current.laptop.model, current.laptop.price, current.laptop.ram_storage, current.laptop.company)



    # Convenience methods for specific categories
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
