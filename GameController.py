from GraphParser import GraphParser


class GameController:
    """Controls the flow of the game, including setup and gameplay."""

    def __init__(self, filepath):
        """
        Initializes the game controller with the path to the graph file and parses the graph.

        Parameters:
            filepath (str): The path to the file containing the graph representation.
        """
        self.graph, self.start_location = GraphParser(filepath).parse()
        

    def explore(self):
        """
        Performs a Depth-First Search (DFS) starting from the starting location to explore the graph.
        Nodes are visited in lexicographical order when faced with multiple choices.

        Returns:
            List[str]: List of node identifiers in the order they were visited.
        """
        return self.graph.dfs(self.start_location)

    def rally_allies(self):
        """
        Uses Breadth-First Search (BFS) from the starting location to determine the shortest path to each ally,
        disregarding edge weights. Allies are sorted by distance, and ties are resolved lexicographically.

        Returns:
            List[str]: List of node ids representing allies in order of proximity.
        """
        return self.graph.bfs(self.start_location)

    def treasure_hunt(self):
        """
        Applies Dijkstra's algorithm to find the least-cost paths to treasures from the starting location.
        Paths are output as a list of tuples containing the path and its total cost, sorted by cost.

        Returns:
            List[Tuple[List[str], float]]: Sorted list of paths and costs to each treasure.
        """
        return self.graph.dijkstra(self.start_location)
