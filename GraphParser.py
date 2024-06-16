from WeightedGraph import WeightedGraph

class GraphParser:
    def __init__(self, filepath):
        """
        Initializes the parser with a path to the file containing the graph representation.
        """
        self.filepath = filepath
        self.start_location = None

    def parse(self):
        """
        Parses the file and returns a WeightedGraph object.
        """
        graph = WeightedGraph()
        section = None

        with open(self.filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith("#"):
                    section = line[1:].lower()
                elif line and section == "nodes":
                    self._parse_node(line, graph)
                elif line and section == "edges":
                    self._parse_edge(line, graph)

        return graph, self.start_location

    def _parse_node(self, line, graph):
        """
        Parses a node line and adds it to the graph.
        """
        parts = line.split(',')
        node_id = parts[0].split()[1].strip()
        label = parts[1].split('=')[1].strip()
        graph.add_node(node_id,label)
        if label == "start":
            self.start_location = node_id

    def _parse_edge(self, line, graph):
        """
        Parses an edge line and adds it to the graph.
        """
        parts = line.split(',')
        nodes = parts[0].split()[1:]
        cost = int(parts[1].split('=')[1].strip())
        graph.add_edge(nodes[0].strip(), nodes[1].strip(), cost)
