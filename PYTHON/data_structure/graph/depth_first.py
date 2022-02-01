from collections import defaultdict

class Graph:
    def __init__ (self):
        self.graph = defaultdict(list)

    def add_node(self,src,dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def prin_graph(self):
        print(self.graph)

    def dfsutil(self,visited,start):
        visited.add(start)
        print(start,end= " ")
        for i in self.graph[start]:
            if i not in visited:
                self.dfsutil(visited,i)  
                
    # shortest path traversal in bfs
    def shortest_path_treaversal(self,start,end):
        queue = [[start]]
        visited = set()
        while (queue):
            path = queue.pop(0)
            if path[-1]==end :
                return path 
            elif path[-1] not in visited:
                for current_neighbours in self.graph[path[-1]]:
                    new_path = list(path)
                    new_path.append(current_neighbours)
                    queue.append(new_path)
                visited.add(path[-1])

ab = Graph()
visited = set()
ab.add_node('chennai','mumbai')
ab.add_node('chennai','bangalore')
ab.add_node('chennai','vishakhapatnam')

ab.add_node('mumbai','ahmedabad')
ab.add_node('mumbail','jalandhar')

ab.add_node('bangalore','bhopal')
ab.add_node('bangalore','patna')
ab.add_node('bangalore','vishakhapatnam')

ab.add_node('vishakhapatnam','kolkata')

ab.add_node('ahmedabad','delhi')
ab.add_node('ahmedabad','kashmir')
ab.add_node('ahmedabad','bhopal')

ab.add_node('bhopal','delhi')
ab.add_node('bhopal','lucknow')
ab.add_node('bhopal','patna')

ab.add_node('delhi','jalandhar')
ab.add_node('delhi','lucknow')

ab.add_node('lucknow','patna')

ab.add_node('patna','kolkata')

ab.add_node('kolkata','guwahati')

ab.add_node('guwahati','dimapur')

ab.add_node('jalandhar','kashmir')

#ab.dfsutil(visited,'patna')
print()
print(ab.shortest_path_treaversal('jalandhar','dimapur'))
print(ab.shortest_path_treaversal('dimapur','jalandhar'))


