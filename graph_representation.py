import sys

# Class to represent a node in the graph
class Node:
    def __init__(self, identifier):
        # Unique identifier for the node
        self.id = identifier
        # Adjacent nodes and their edge weights
        self.neighbors = {}
        # Initialize distance to maximum possible
        self.distance = sys.maxsize
        # Flag for visited nodes
        self.visited = False
        # Previous node in the path
        self.previous = None

    def add_edge(self, adjacent_node, weight=0):
        # Connect a node to its neighbor
        self.neighbors[adjacent_node] = weight

    def get_adjacent_nodes(self):
        # Retrieve adjacent nodes
        return self.neighbors.keys()

    def get_node_id(self):
        # Get the node's unique identifier
        return self.id

    def get_edge_weight(self, neighbor):
        # Get weight of edge to a neighbor
        return self.neighbors[neighbor]

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.neighbors])

# Class for the entire graph
class GraphStructure:
    def __init__(self):
        # Store nodes in the graph
        self.node_dict = {}
        # Number of nodes in the graph
        self.node_count = 0

    def __iter__(self):
        return iter(self.node_dict.values())

    def add_node(self, node_id):
        # Add a new node to the graph
        self.node_count += 1
        new_node = Node(node_id)
        self.node_dict[node_id] = new_node
        return new_node

    def get_node(self, node_id):
        # Retrieve a node by its identifier
        return self.node_dict.get(node_id, None)

    def create_edge(self, from_node, to_node, weight=0):
        # Create an edge between two nodes
        if from_node not in self.node_dict:
            self.add_node(from_node)
        if to_node not in self.node_dict:
            self.add_node(to_node)

        # Since it's an undirected graph, add edges in both directions
        self.node_dict[from_node].add_edge(self.node_dict[to_node], weight)
        self.node_dict[to_node].add_edge(self.node_dict[from_node], weight)

    def get_node_ids(self):
        # Get identifiers of all nodes in the graph
        return self.node_dict.keys()


# Main execution starts here
if __name__ == '__main__':
    # Create a graph instance
    graph = GraphStructure()

    # Adding nodes to the graph
    for node in ['a', 'b', 'c', 'd', 'e', 'f']:
        graph.add_node(node)

    # Adding edges and their weights
    edges = [
        ('a', 'b', 7), ('a', 'c', 9), ('a', 'f', 14),
        ('b', 'c', 10), ('b', 'd', 15),
        ('c', 'd', 11), ('c', 'f', 2),
        ('d', 'e', 6), ('e', 'f', 9)
    ]
    for frm, to, cost in edges:
        graph.create_edge(frm, to, cost)

    # Display the graph
    print('Graph Data:')
    for node in graph:
        for neighbor in node.get_adjacent_nodes():
            node_id = node.get_node_id()
            neighbor_id = neighbor.get_node_id()
            print(f'({node_id}, {neighbor_id}, {node.get_edge_weight(neighbor)})')