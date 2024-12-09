class Laptop:
    def __init__(self, cpu_gpu="", ram_storage="", price=0.0, model="", company="", category=""):
        self.cpu_gpu = cpu_gpu
        self.ram_storage = ram_storage
        self.price = price
        self.model = model
        self.company = company

    def display_info(self):
        print(f" \t \t  \t \t   Company: {self.company}")
        print(f" \t \t  \t \t  \t \t CPU_GPU: {self.cpu_gpu}")
        print(f" \t \t  \t \t  \t \t RAM/Storage: {self.ram_storage}")
        print(f" \t \t  \t \t  \t \t Price: ${self.price}")
        print(f" \t \t  \t \t  \t \t Published in Year: {self.model}")  
        print()


    # Getter methods
    def get_comapny(self):
        return self.company

    def get_cpu_gpu(self):
        return self.cpu_gpu

    def get_ram_storage(self):
        return self.ram_storage

    def get_price(self):
        return self.price

    def get_model(self):
        return self.model

    # Setter methods
    def set_comapny(self, company):
        self.company = company

    def set_cpu_gpu(self, title):
        self.cpu_gpu = title

    def set_ram_storage(self, ram_storage):
        self.ram_storage = ram_storage

    def set_price(self, price):
        self.price = price

    def set_model(self, model):
        self.model = model
