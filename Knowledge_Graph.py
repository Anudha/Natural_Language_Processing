import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def create_knowledge_graph(csv_file):
    """
    Reads a CSV file with 'question' and 'answer' columns and generates a knowledge graph.
    """
    # Load CSV data
    df = pd.read_csv(csv_file)

    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes and edges
    for _, row in df.iterrows():
        question = row['question']
        answer = row['answer']
        G.add_edge(question, answer)  # Question -> Answer relationship

    return G

def visualize_knowledge_graph(G):
    """
    Visualizes the knowledge graph using Matplotlib.
    """
    plt.figure(figsize=(12, 6))
    pos = nx.spring_layout(G, seed=42)  # Node positioning
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=3000, font_size=9)
    plt.title("Knowledge Graph from Q&A CSV")
    plt.show()

# Example: Convert CSV to Knowledge Graph
csv_file = "AI_Performance_Metrics-2.csv"  # Replace with your CSV file path
G = create_knowledge_graph(csv_file)
visualize_knowledge_graph(G)
