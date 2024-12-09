import networkx as nx
import matplotlib.pyplot as plt


# Initialize graph
G = nx.Graph()

# Define vertices
vertex_labels = [
    "CIVIL", "CENTRAL JAIL", "CANTT ROAD", "CMH", "BONE CARE", "AGHA KHAN", "HAJIANI", "BINTAYAB", "MAAJEE",
    "INDUS BLOOD BANK", "L8", "FATMID BLOOD BANK", "L7", "AUTOBHAN", "QASIMABAD", "RAJPUTANA", "GULCENTER", 
    "NASIM NAGAR", "THANDISADAK", "HAIDER CHOWK", "QASIM CHOWK", "SADDAR", "HIRABAD", "CITY GATE", "LIBERTY", 
    "PATHAN COLONY", "JAMSHORO ROAD", "CIVIL BLOOD BANK", "ZAINABIA BLOOD BANK", "DADAN SHAH", 
    "QOMI SHAHRAH ROAD", "CHANDNI", "RISALA ROAD", "ALRAHIM ROAD", "TILAK CHARI", "RANIBAGH", 
    "WADUWA ROAD", "GULISTAN E SAJJAD"
]

# Add vertices to the graph
G.add_nodes_from(vertex_labels)

# Define edges with weights
edges = [
    ("L8", "L7", 1), ("L8", "AUTOBHAN", 3), ("L7", "MAAJEE", 0.5), ("AUTOBHAN", "MAAJEE", 0.5),
    ("L8", "MAAJEE", 2), ("L7", "GULCENTER", 1.4), ("AUTOBHAN", "THANDISADAK", 3), 
    ("AUTOBHAN", "INDUS BLOOD BANK", 3), ("THANDISADAK", "GULCENTER", 0.7),
    ("THANDISADAK", "INDUS BLOOD BANK", 0.7), ("RANIBAGH", "THANDISADAK", 0.7), 
    ("RANIBAGH", "WADUWA ROAD", 0.7), ("WADUWA ROAD", "FATMID BLOOD BANK", 0.7),
    ("WADUWA ROAD", "QASIMABAD", 0.7), ("QASIMABAD", "NASIM NAGAR", 0.6), 
    ("QASIMABAD", "FATMID BLOOD BANK", 0.6), ("NASIM NAGAR", "GULISTAN E SAJJAD", 0.6),
    ("NASIM NAGAR", "AGHA KHAN", 0.6), ("NASIM NAGAR", "QASIM CHOWK", 0.6),
    ("GULISTAN E SAJJAD", "RAJPUTANA", 0.6), ("JAMSHORO ROAD", "RAJPUTANA", 0.6),
    ("JAMSHORO ROAD", "AGHA KHAN", 0.6), ("JAMSHORO ROAD", "QASIM CHOWK", 0.6),
    ("QASIM CHOWK", "QOMI SHAHRAH ROAD", 0.6), ("QOMI SHAHRAH ROAD", "RANIBAGH", 0.6),
    ("QOMI SHAHRAH ROAD", "THANDISADAK", 0.6), ("GULCENTER", "HAIDER CHOWK", 1.3),
    ("GULCENTER", "CHANDNI", 2.2), ("CHANDNI", "SADDAR", 2.2), 
    ("NASIM NAGAR", "QASIM CHOWK", 0.6), ("NASIM NAGAR", "AGHA KHAN", 0.4),
    ("HAIDER CHOWK", "RISALA ROAD", 1.3), ("RISALA ROAD", "SADDAR", 1.3),
    ("QASIM CHOWK", "CANTT ROAD", 0.4), ("CANTT ROAD", "CMH", 0.4),
    ("CANTT ROAD", "SADDAR", 0.4), ("QASIM CHOWK", "CENTRAL JAIL", 1.2),
    ("QASIM CHOWK", "AGHA KHAN", 1.5), ("SADDAR", "ALRAHIM ROAD", 1.2),
    ("ALRAHIM ROAD", "LIBERTY", 1.2), ("ALRAHIM ROAD", "HAJIANI", 1.2),
    ("ALRAHIM ROAD", "ZAINABIA BLOOD BANK", 1.2), ("ALRAHIM ROAD", "PATHAN COLONY", 1.2),
    ("PATHAN COLONY", "LIBERTY", 1.2), ("CENTRAL JAIL", "CITY GATE", 1.2),
    ("HIRABAD", "LIBERTY", 2.2), ("HIRABAD", "BONE CARE", 0.7),
    ("CITY GATE", "HIRABAD", 1.1), ("LIBERTY", "CIVIL", 0.3),
    ("LIBERTY", "CIVIL BLOOD BANK", 0.3), ("CIVIL", "CIVIL BLOOD BANK", 0.3),
    ("CITY GATE", "PATHAN COLONY", 1.4), ("PATHAN COLONY", "BINTAYAB", 1.5),
    ("LIBERTY", "SARFARAZ CHARI", 1.5), ("PATHAN COLONY", "SARFARAZ CHARI", 1.5),
    ("SARFARAZ CHARI", "BINTAYAB", 1.5), ("LIBERTY", "TILAK CHARI", 1.5),
    ("TILAK CHARI", "DADAN SHAH", 1.5), ("TILAK CHARI", "SADDAR", 1.5),
    ("DADAN SHAH", "ZAINABIA BLOOD BANK", 1.5), ("DADAN SHAH", "HAJIANI", 1.5),
    ("DADAN SHAH", "ALRAHIM ROAD", 1.5), ("GULISTAN E SAJJAD", "JAMSHORO ROAD", 1.5)
]

# Add edges to the graph
for v1, v2, weight in edges:
    G.add_edge(v1, v2, weight=weight)

# Draw the graph
plt.figure(figsize=(20, 15))
pos = nx.spring_layout(G, seed=42)  # Layout with consistent positioning
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='skyblue')
nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.9, edge_color="black")
nx.draw_networkx_labels(G, pos, font_size=9, font_family="sans-serif")

# Draw edge labels with weights
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7, font_color="red")

plt.title("Graph Visualization of Blood Bank Routing System")
plt.axis("off")  # Hide axes for clarity
plt.show()
