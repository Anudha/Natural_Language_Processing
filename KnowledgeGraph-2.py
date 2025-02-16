import networkx as nx
import matplotlib.pyplot as plt

def create_sample_graph():
    """Creates a simple directed graph with labeled nodes and edges."""
    G = nx.DiGraph()
    edges = [
        ("AI", "Machine Learning"),
        ("Machine Learning", "Deep Learning"),
        ("Deep Learning", "Neural Networks"),
        ("AI", "Computer Vision"),
        ("AI", "Natural Language Processing"),
        ("Computer Vision", "Image Recognition"),
        ("Natural Language Processing", "Chatbots"),
        ("Neural Networks", "GPT-4"),
    ]
    G.add_edges_from(edges)
    return G

def visualize_graph(G):
    """Visualizes the graph using Matplotlib."""
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G, seed=42)  # Positions for nodes
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=3000, font_size=10, arrows=True)
    plt.title("Knowledge Graph")
    plt.show()

def graph_info(G):
    """Prints basic information about the graph."""
    print("Graph Info:")
    print(nx.info(G))
    print("\nNodes:", G.nodes)
    print("\nEdges:", G.edges)

def shortest_path(G, start, end):
    """Finds the shortest path between two nodes if possible."""
    if nx.has_path(G, start, end):
        path = nx.shortest_path(G, source=start, target=end)
        print(f"Shortest path from {start} to {end}: {path}")
    else:
        print(f"No path found between {start} and {end}")

def centrality_analysis(G):
    """Computes and prints centrality measures."""
    degree_centrality = nx.degree_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G)
    closeness_centrality = nx.closeness_centrality(G)

    print("\nCentrality Measures:")
    print("Degree Centrality:", degree_centrality)
    print("Betweenness Centrality:", betweenness_centrality)
    print("Closeness Centrality:", closeness_centrality)

def graph_traversal(G, start_node):
    """Performs BFS traversal from a given node."""
    if start_node in G:
        bfs_edges = list(nx.bfs_edges(G, source=start_node))
        bfs_nodes = [start_node] + [v for u, v in bfs_edges]
        print(f"BFS Traversal from {start_node}: {bfs_nodes}")
    else:
        print(f"Node {start_node} not found in graph.")

# Run the prototype functions
G = create_sample_graph()
visualize_graph(G)
graph_info(G)
shortest_path(G, "AI", "GPT-4")
centrality_analysis(G)
graph_traversal(G, "AI")
