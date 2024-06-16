# CENG310 Programming Assignment 4: Graph Explorer Game

## Overview
This assignment focuses on implementing various graph algorithms to manage and navigate a simulated game world represented as a weighted graph. You will explore the practical applications of Depth-First Search (DFS), Breadth-First Search (BFS), and Dijkstra's algorithm in pathfinding and graph traversal tasks.

## Installation and Setup
- **Dependencies**: Python version is 3.10.5. 3.6+ python versions is enough. 
- **Execution**:  Python is enogh for that program. Nothing else is needed. I also imported heapq which is useful library in python. 

## Usage
Explain how to use the system after setting it up:
- **Starting the program**: Provide the command to start the `GameController`. In terminal by writing GameController.py the GameController.py file starts. it can be used for the other python files.
- **Input files**:  The graph input file shows nodes , label of nodes , edges and cost of these edges. We mpdify it with functions like add_node, add_edge in WeightedGraph.py and we can add also other functions like delete_node. 
- **Operations**: Detail how to initiate graph exploration, ally rallying, and treasure hunting.
  - Graph exploration uses DFS and starts from starting node given in the graph input file and exploes as much as before backracking. Uses the explore method in GameController.py . the alghoritm uses stacks to keep tracking. 
  - Ally rallying is used with BFS. It starts at the strating position and explores all neighbor nodes at the next level. 
  - Treasure hunting uses dijkstra alghoritm. That alghoritm uses queues and dictionaries to track and find minimum costs and finds the path which has lowest cost. 

## Implementation Details
- **Graph Representation**:
  - Describe the adjacency map used for the graph. The adjacency map uses dictionary for dictionaries like each node in the graph is a key in main dictionary and its value in anpther dictionary whic these values are edges and costs.

  - Explain the choice of using an adjacency map over other representations. It is more readable, flexible and has efficiency in accessing other nodes. It is better than adjaceny list and adjaceny matrix for our problem.

- **Graph Algorithms**:
  - **DFS**: 
      The alghoritm starts a while loop and goes as much as it goes until the stack gets empty. in each tour it pops a node and checks for visited or not. if it is visited adds to the visited list and track the same visited path for going back. the alghoritm continues until all nodes are visited. 
  - **BFS**:
      The alghoritm starts from a root node and explore all neighbor nodes. In that homework, BFS helps rally allies by finding the shortest paths from the start nodes to ally nodes. Also, ensure the all ally nodes are visited.

  - **Dijkstra**: Explain the implementation details of Dijkstra's algorithm and how paths are selected and prioritized.
      In this example, that alghoritm is used for finding the shortest path whch all nodes are labeled as 'treasure'. It uses priory queues and the alghorithm goes to closest nodes. After the function path is reconstructed according to total cost. 

## Graph Representations
- **Alternative Representations**:
  - Discuss at least two alternative graph representations.
    Adjacency list and adjacency matrix are two alternative for that graph representations. The list has advantages like space efficient and traversing easily but it is slightly worse according to Big O notation. ADjacency matrix has also some advantages like simplicity and its complexity is O(1). 
  - Compare and contrast these with the adjacency map used in the assignment.
    Adjaceny list's advantages are space efficiency and easy traversal. However, its updates are more complex. Adjacency matrix's advantages are low complexity (O(1)) and simple implementation but it is space inefficient. The map which is ued in that project has some advantages than these like efficient edge operation and space efficiency. the method's disadvantage is slightly complex implementations. 

  - Analyze advantages and disadvantages in terms of time and space complexity.
    Adjaceny list's space complexity = O(n) n is sum of edges and nodes     
    time complexity = O(n) n is number of nodes for traversal  O(1) = for insert and delete 
    Adjacency matrix's space complexity = O(n)
    time complexity = O(n) for traversal  O(1) = for insert/delete 
    Adjacency map's space complexity = O(n) n = sum of node and edges 
    time complexity = O(n)  O(1) = for insert/delete

- **Rationale for Using Adjacency Map**:
  - Justify why the adjacency map is particularly suitable for the tasks in this assignment, considering the specific operations required.
    The adjacency map's combination of efficient edge operations, space efficiency, and flexibility makes it  suitable for the tasks in this assignment. These properties ensure that the graph algorithms perform efficiently and effectively. 

## Testing
- **Unit Tests**: Outline how to run the unit tests provided in the `tester.ipynb` Jupyter Notebook.
    After copying all used python files to a folder icluding the tester.ipynb, in vs code open the folder. After opening all these files we can run the tester.ipynb file from the button on top of the page. And click to run all button. "# Graph-exploration-game" 
