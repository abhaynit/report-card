from blue_print_graph import graph

class make_graph:
    def __init__(self):


        self.Graph = graph(10)
        self.Graph.add_unidirectional_node(0,9)
        self.Graph.add_node(0,1)
        self.Graph.add_node(0,2)
        self.Graph.add_node(1,3)
        self.Graph.add_node(2,3)
        self.Graph.add_node(2,4)
        self.Graph.add_node(3,8)
        self.Graph.add_node(4,5)
        self.Graph.add_node(5,6)
        self.Graph.add_node(6,7)
        self.Graph.add_node(7,8)
        #self.Graph.add_node(9,8)

        """
        self.Graph = graph(12)
        self.Graph.add_node(0,1)
        self.Graph.add_node(0,9)
        self.Graph.add_node(1,8)
        self.Graph.add_node(3,2)
        self.Graph.add_node(3,4)
        self.Graph.add_node(3,5)
        self.Graph.add_node(6,5)
        self.Graph.add_node(7,10)
        self.Graph.add_node(7,11)
        self.Graph.add_node(7,6)
        self.Graph.add_node(7,3)
        self.Graph.add_node(8,7)
        self.Graph.add_node(9,8)
        self.Graph.add_node(10,11)
        """
    def print_the_graph(self):
        self.Graph.print1()

    def breadth_first_traversal(self):
        self.Graph.bfs()

    def find_shortest_path(self,starting_point,dest):
        self.Graph.shortest_path(starting_point,dest)