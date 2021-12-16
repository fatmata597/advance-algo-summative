import sys
import queue


# This class holds the structure of the vertex
class Vertex:
    #initializing the structure of the vertex has empty list of edges
    def __init__(self):
        self.edges = {}
    
    #Create a function that get gets edges stored in the class 
    def get_edges(self):
        return self.edges
    
    # this function add edges with the value and the distance between them
    def add_edge(self, val, dist):
        #an if statement to check if the current vertex is not already in the current edge
        # or if the distance is less than the distance currently in that edge location
        if val not in self.edges or dist < self.edges[val]:
            #add the edge to the vertex
            self.edges[val] = dist


# This class holds the structure of the graph 
class Graph:
    # initializing the graph by adding all initial number of 
    # vertices to the vertex structure initiated above
    def __init__(self, N):
        self.vertices = {}
        # A while to check that all the number of nodes are added in as vertices, 
        # this while loop will run until the vertices are 0
        while N > 0:
            self.vertices[N] = Vertex()
            N -= 1

    # function to get vertices in our graph
    def get_vertices(self):
        return self.vertices
        
    # Gets the vertex in a particular index location

    def get_vertex(self, value):
        return self.vertices[value]

    # add new in our graph at a particular index location

    def add_vertex(self, value, vertex):
        self.vertices[value] = vertex


# using Dijkstra algorithm to check and calculate the shortest distance 
# between all vertices that have been reach
class AllPaths:
    
    # initializing graph that would be used in functions
    def __init__(self, graph):
        self.graph = graph

    # this function calculate and update adjacent distances 
    # that are shortest from satrt vertex to a particular vertex
    def calculate_distance(self, begin):
        # this dictionary holds nodes and their shortest 
        # distances from the first node that have been reach
        reach = {begin : 0}
        adjacents = queue.PriorityQueue()
        # updating all adjacent points around the begining node
        self.update_adjacents(begin, reach, adjacents)
        # while loop that runs so long as the list of adjacents is not empty
        while not adjacents.empty():
            # get distance and value of the adjacent node
            (distance, value) = adjacents.get()
            # if the adjacent value already in reach then we continue
            if value in reach:
                continue
             # add node and distance to our dictionary of reach nodes
            reach[value] = distance
            # Update the adjacents nodes to the list of adjacents
            self.update_adjacents(value, reach, adjacents)
        return reach

    # function that updatess adjacent nodes
    def update_adjacents(self, parent, reach, adjacents):
        edges = self.graph.get_vertex(parent).get_edges()
        for value, distance in edges.items():
            adjacents.put((reach[parent] + distance, value))
#shortest reach algorithm
def shortestReach(n,edges,s):
    # initialize graph by passing in the number of nodes
    graph = Graph(n)
    
    # loop through from 0 to he number of nodes
    for i in range(n):
        begin,end,dist = edges[i][0], edges[i][1], edges[i][2]
        graph.get_vertex(begin).add_edge(end, dist)
        # on that same vertex, use the node to and add same 
        # edge now with the node from and the distance between them
        graph.get_vertex(end).add_edge(begin, dist)
    allpaths = AllPaths(graph)
    begin = s
    distances = allpaths.calculate_distance(begin)
    del distances[s]
    # sorting the dictionary by the keys
    distancess = sorted(distances)
    distance = []
    
    # loop through our sorted dictionary list
    for i in range(len(distancess)):
        distance.append(distances[distancess[i]])
    
    # display list as strings
    return ' '.join(map(str, distance))


n = 5

edges = [[1,2,5],[2,3,6],[3,4,2],[1,3,15],[1,5,-1],[2,5,-1],[3,5,-1],[4,5,-1]]
s = 1


print(shortestReach(n,edges,s))