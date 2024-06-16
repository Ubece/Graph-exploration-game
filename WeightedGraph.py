import heapq

class WeightedGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node_id, label=None):
        if node_id not in self.nodes:
            self.nodes[node_id] = {'label': label, 'edges': {}}

    def add_edge(self, node1, node2, cost):
        if node1 in self.nodes and node2 in self.nodes:
            if node2 not in self.nodes[node1]['edges']:
                self.nodes[node1]['edges'][node2] = cost
            if node1 not in self.nodes[node2]['edges']:
                self.nodes[node2]['edges'][node1] = cost

    def dfs(self, start):
        visited = []
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                neighbors = sorted(self.nodes[node]['edges'].keys(), reverse=True)
                stack.extend(neighbors)

        return visited

    def bfs(self, start):
        visited = []
        queue = [start]
        level = {start: 0}
        allies = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                if self.nodes[node]['label'] == 'ally':
                    allies.append((level[node], node))
                neighbors = sorted(self.nodes[node]['edges'].keys())
                for neighbor in neighbors:
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
                        level[neighbor] = level[node] + 1

        allies.sort()
        return [ally for _, ally in allies]

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.nodes}
        previous_nodes = {node: None for node in self.nodes}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.nodes[current_node]['edges'].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        paths = []
        for node, distance in distances.items():
            if self.nodes[node]['label'] == 'treasure':
                path = []
                while node is not None:
                    path.append(node)
                    node = previous_nodes[node]
                paths.append((path[::-1], distance))

        return paths