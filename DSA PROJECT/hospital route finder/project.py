from collections import deque
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  

class Graph:
    def __init__(self, vertex_labels):
        self.label_to_index = {label: i for i, label in enumerate(vertex_labels)}
        self.index_to_label = {i: label for label, i in self.label_to_index.items()}
        self.vertex_count = len(vertex_labels)
        self.adjacent_list = {i: [] for i in range(self.vertex_count)}

    def add_edge(self, v_label, u_label, weight=1):
        v = self.label_to_index.get(v_label)
        u = self.label_to_index.get(u_label)
        if v is not None and u is not None:
            self.adjacent_list[v].append((u, weight))
            self.adjacent_list[u].append((v, weight))

    def bfs_iterative(self, start, destination):
        start_index = self.label_to_index.get(start)
        destination_index = self.label_to_index.get(destination)

        if start_index is None or destination_index is None:
            return "Invalid start or destination label", 0

        visited = set()
        queue = deque([(start_index, 0, [self.index_to_label[start_index]])])
        result = ""

        while queue:
            node, total_distance, path = queue.popleft()

            if node == destination_index:
                result += "Best Route available to Hospital\n"
                result += f"Total distance covered: {total_distance} km\n"
                result += f"Path: {' -> '.join(path)}\n"
                return result, total_distance
            range_=0.07
            if random.random() < range_:
                traffic = random.randint(1, 2)
                obstacle_distance = random.randint(1, 2)
                if traffic == 1:
                    result += f"ROUTE CHANGED DUE TO TRAFFIC DELAY AT {self.index_to_label[node]}\n"
                else:
                    result += f"ROUTE CHANGED DUE TO ROAD CONSTRUCTION AT {self.index_to_label[node]}\n"
                result += f"Previous Route Path: {' -> '.join(path)}\n"
                total_distance += obstacle_distance
                queue.append((node, total_distance, path))
                continue

            if node not in visited:
                visited.add(node)
                for neighbor, weight in self.adjacent_list[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, total_distance + weight, path + [self.index_to_label[neighbor]]))

        return "No route available to the BLOOD BANK", 0
        
class GraphApp(tk.Frame):
    def __init__(self, root, graph):
        super().__init__(root)
        self.graph = graph
        self.root = root
        font = ("Helvetica", 10)
        

        # Labels and Entry fields for start and destination
        self.start_label = tk.Label(self, text="\nYour Location (BLOOD BANK):", font=("Helvetica", 12, "bold"))
        self.start_label.grid(row=0, column=0, padx=5, pady=(10, 5))

        self.start_entry = tk.Entry(self, font=("Helvetica", 10, "bold"), fg="#494949")
        self.start_entry.grid(row=0, column=1, padx=5, pady=(10, 5))

        self.start_info_label = tk.Label(
            self, 
            text="(FATMID BLOOD BANK, CIVIL BLOOD BANK,\nINDUS BLOOD BANK, ZAINABIA BLOOD BANK)", 
            font=("Helvetica", 8, "bold"), 
            fg="#c1c1c1"
        )
        self.start_info_label.grid(row=1, column=1, padx=5, pady=5)

        self.destination_label = tk.Label(self, text="\nHospital Name:", font=("Helvetica", 12, "bold"))
        self.destination_label.grid(row=2, column=0, padx=5, pady=5)

        self.destination_entry = tk.Entry(self, font=("Helvetica", 10, "bold"), fg="#494949")
        self.destination_entry.grid(row=2, column=1, padx=5, pady=5)

        self.destination_info_label = tk.Label(
            self, 
            text="(CIVIL, CMH, BONECARE, AGHAKHAN,\nHAJIANI, BINTAYAB, MAAJEE, RAJPUTANA)", 
            font=("Helvetica", 8, "bold"), 
            fg="#c1c1c1"
        )
        self.destination_info_label.grid(row=3, column=1, padx=5, pady=(5, 20))  # Adjusted pady for spacing

        # Button to find the route
        self.search_button = tk.Button(
            self, 
            text="Find Route", 
            command=self.find_route, 
            font=("Helvetica", 14), 
            bg="maroon", 
            fg="white"
        )
        self.search_button.grid(row=4, column=0, columnspan=2, padx=5, pady=15)

        # Frame to hold the Text widget and Scrollbar
        result_frame = tk.Frame(self)
        result_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Text widget for displaying results
        self.result_text = tk.Text(result_frame, height=10, width=70, font=font, wrap="word")
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for the Text widget
        scrollbar = tk.Scrollbar(result_frame, command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.configure(yscrollcommand=scrollbar.set)

        # Configure text tags for formatting
        self.result_text.tag_configure("highlight", foreground="blue", font=("Helvetica", 14, "bold"))
        self.result_text.tag_configure("delay", foreground="red", font=("Helvetica", 10, "bold"))
        self.result_text.tag_configure("route", foreground="black", font=("Helvetica", 12, "bold"))
        self.result_text.tag_configure("path", foreground="black", font=("Helvetica", 10, "bold"))
        self.result_text.tag_configure("prev", foreground="black", font=("Helvetica", 10, "bold"))

        # Set grid weights for resizing
        self.grid_rowconfigure(5, weight=1)  # Ensures result_frame row resizes with the window
        self.grid_columnconfigure(0, weight=1)

    def find_route(self):
        start = self.start_entry.get().strip().upper()
        destination = self.destination_entry.get().strip().upper()
        
        if not start or not destination:
            messagebox.showerror("Input Error", "Please enter both start and destination nodes.")
            return
        
        result, total_distance = self.graph.bfs_iterative(start, destination)
        self.result_text.delete(1.0, tk.END)
        
        for line in result.splitlines():
            if "Total distance covered" in line:
                self.result_text.insert(tk.END, line + "\n", "highlight")
            elif "ROUTE CHANGED" in line:
                self.result_text.insert(tk.END, line + "\n", "delay")
            elif "Best Route available to Hospital" in line:
                self.result_text.insert(tk.END, line + "\n", "route")
            elif "Previous Route Path" in line:
                self.result_text.insert(tk.END, line + "\n", "prev")
            elif "Path" in line:
                self.result_text.insert(tk.END, line + "\n", "path")
            else:
                self.result_text.insert(tk.END, line + "\n")


class WelcomePage(tk.Frame):
    def __init__(self, root, switch_to_main, bg_image):
        super().__init__(root)
        self.root = root
        self.switch_to_main = switch_to_main

        # Set the background image
        self.bg_image = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self, image=self.bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Add the welcome label
        welcome_label = tk.Label(
            self, text="Welcome to the Hospital Route Finder",
            font=("Helvetica", 24, "bold"), bg="#ffffff", fg="#333333"
        )
        welcome_label.place(relx=0.5, rely=0.3, anchor="center")

        # Add the proceed button
        proceed_button = tk.Button(
            self, text="Proceed to Route Map",
            font=("Helvetica", 16), bg="maroon", fg="white",
            command=self.show_loading_screen
        )
        proceed_button.place(relx=0.5, rely=0.5, anchor="center")


        
        # Loading animation (hidden initially)
        self.loading_label = tk.Label(self, text="Loading...", font=("Helvetica", 16, "bold"), bg="#cccccc", fg="maroon")
        self.loading_label.place(relx=0.5, rely=0.2, anchor="center")
        self.loading_label.place_forget()  

    def show_loading_screen(self):
        # Show the loading animation
        self.loading_label.place(relx=0.5, rely=0.7, anchor="center")

        # Add a delay of 2 seconds before switching
        self.root.after(3000, self.switch_to_main)


class App(tk.Tk):
    def __init__(self, graph, bg_image):
        super().__init__()
        self.graph = graph
        self.geometry("800x600")
        self.title("Hospital Route Finder")

        # Initialize the welcome and main pages
        self.welcome_page = WelcomePage(self, self.show_main_page, bg_image)
        self.welcome_page.pack(fill="both", expand=True)

        self.main_page = GraphApp(self, self.graph)

    def show_main_page(self):
        # Switch to the main page
        self.welcome_page.pack_forget()
        self.main_page.pack(fill="both", expand=True)



vertex_labels = [
    "CIVIL", "CENTRAL JAIL", "CANTT ROAD", "CMH", "BONE CARE", "AGHA KHAN", "HAJIANI", "BINTAYAB", "MAAJEE",
    "INDUS BLOOD BANK", "L8", "FATMID BLOOD BANK", "L7", "AUTOBHAN", "QASIMABAD", "RAJPUTANA", "GULCENTER", 
    "NASIM NAGAR", "THANDISADAK", "HAIDER CHOWK", "QASIM CHOWK", "SADDAR", "HIRABAD", "CITY GATE", "LIBERTY", 
    "PATHAN COLONY", "JAMSHORO ROAD", "CIVIL BLOOD BANK", "ZAINABIA BLOOD BANK", "DADAN SHAH", 
    "QOMI SHAHRAH ROAD", "CHANDNI", "RISALA ROAD", "ALRAHIM ROAD", "TILAK CHARI", "RANIBAGH", 
    "WADUWA ROAD", "GULISTAN E SAJJAD"]
graph = Graph(vertex_labels)
graph.add_edge("L8", "L7", weight=1)
graph.add_edge("L8", "AUTOBHAN", weight=3)
graph.add_edge("L7", "MAAJEE", weight=0.5)
graph.add_edge("AUTOBHAN", "MAAJEE", weight=0.5)
graph.add_edge("L8", "MAAJEE", weight=2)
graph.add_edge("L7", "GULCENTER", weight=1.4)
graph.add_edge("AUTOBHAN", "THANDISADAK", weight=3)
graph.add_edge("AUTOBHAN", "INDUS BLOOD BANK", weight=3)
graph.add_edge("THANDISADAK", "GULCENTER", weight=0.7)
graph.add_edge("THANDISADAK", "INDUS BLOOD BANK", weight=0.7)
graph.add_edge("RANIBAGH", "THANDISADAK", weight=0.7)
graph.add_edge("RANIBAGH", "WADUWA ROAD", weight=0.7)
graph.add_edge("WADUWA ROAD", "FATMID BLOOD BANK", weight=0.7)
graph.add_edge("WADUWA ROAD", "QASIMABAD", weight=0.7)
graph.add_edge("QASIMABAD", "NASIM NAGAR", weight=0.6)
graph.add_edge("QASIMABAD", "FATMID BLOOD BANK", weight=0.6)
graph.add_edge("NASIM NAGAR", "GULISTAN E SAJJAD", weight=0.6)
graph.add_edge("NASIM NAGAR", "AGHA KHAN", weight=0.6)
graph.add_edge("NASIM NAGAR", "QASIM CHOWK", weight=0.6)
graph.add_edge("GULISTAN E SAJJAD", "RAJPUTANA", weight=0.6)
graph.add_edge("JAMSHORO ROAD", "RAJPUTANA", weight=0.6)
graph.add_edge("JAMSHORO ROAD", "AGHA KHAN", weight=0.6)
graph.add_edge("JAMSHORO ROAD", "QASIM CHOWK", weight=0.6)
graph.add_edge("QASIM CHOWK", "QOMI SHAHRAH ROAD", weight=0.6)
graph.add_edge("QOMI SHAHRAH ROAD", "RANIBAGH", weight=0.6)
graph.add_edge("QOMI SHAHRAH ROAD", "THANDISADAK", weight=0.6)
graph.add_edge("GULCENTER", "HAIDER CHOWK", weight=1.3)
graph.add_edge("GULCENTER", "CHANDNI", weight=2.2)
graph.add_edge("CHANDNI", "SADDAR", weight=2.2)
graph.add_edge("NASIM NAGAR", "QASIM CHOWK", weight=0.6)
graph.add_edge("NASIM NAGAR", "AGHA KHAN", weight=0.4)
graph.add_edge("HAIDER CHOWK", "RISALA ROAD", weight=1.3)
graph.add_edge("RISALA ROAD", "SADDAR", weight=1.3)
graph.add_edge("QASIM CHOWK", "CANTT ROAD", weight=0.4)
graph.add_edge("CANTT ROAD", "CMH", weight=0.4)
graph.add_edge("CANTT ROAD", "SADDAR", weight=0.4)
graph.add_edge("QASIM CHOWK", "CENTRAL JAIL", weight=1.2)
graph.add_edge("QASIM CHOWK", "AGHA KHAN", weight=1.5)
graph.add_edge("SADDAR", "ALRAHIM ROAD", weight=1.2)
graph.add_edge("ALRAHIM ROAD", "LIBERTY", weight=1.2)
graph.add_edge("ALRAHIM ROAD", "HAJIANI", weight=1.2)
graph.add_edge("ALRAHIM ROAD", "ZAINABIA BLOOD BANK", weight=1.2)
graph.add_edge("ALRAHIM ROAD", "PATHAN COLONY", weight=1.2)
graph.add_edge("PATHAN COLONY", "LIBERTY", weight=1.2)
graph.add_edge("CENTRAL JAIL", "CITY GATE", weight=1.2)
graph.add_edge("HIRABAD", "LIBERTY", weight=2.2)
graph.add_edge("HIRABAD", "BONE CARE", weight=0.7)
graph.add_edge("CITY GATE", "HIRABAD", weight=1.1)
graph.add_edge("LIBERTY", "CIVIL", weight=0.3)
graph.add_edge("LIBERTY", "CIVIL BLOOD BANK", weight=0.3)
graph.add_edge("CIVIL", "CIVIL BLOOD BANK", weight=0.3)
graph.add_edge("CITY GATE", "PATHAN COLONY", weight=1.4)
graph.add_edge("PATHAN COLONY", "BINTAYAB", weight=1.5)
graph.add_edge("LIBERTY", "SARFARAZ CHARI", weight=1.5)
graph.add_edge("PATHAN COLONY", "SARFARAZ CHARI", weight=1.5)
graph.add_edge( "SARFARAZ CHARI","BINTAYAB", weight=1.5)
graph.add_edge("LIBERTY", "TILAK CHARI", weight=1.5)
graph.add_edge("TILAK CHARI", "DADAN SHAH", weight=1.5)
graph.add_edge("TILAK CHARI", "SADDAR", weight=1.5)
graph.add_edge("DADAN SHAH", "ZAINABIA BLOOD BANK", weight=1.5)
graph.add_edge("DADAN SHAH", "HAJIANI", weight=1.5)
graph.add_edge("DADAN SHAH", "ALRAHIM ROAD", weight=1.5)
graph.add_edge("GULISTAN E SAJJAD", "JAMSHORO ROAD", weight=1.5)

# Load and resize the background image
bg_image = Image.open("ambulance.jpg")
bg_image = bg_image.resize((800, 600), Image.LANCZOS)

app = App(graph, bg_image)
app.mainloop()
