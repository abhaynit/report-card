class node:
    def __init__(self,data):
        self.data = data 
        self.next = None


class graph:
    def __init__(self,v):
        self.vertices = v
        self.graph = [None]*self.vertices

    def add_node(self,src,dest):
        ab = node(dest)
        ab.next = self.graph[src]
        self.graph[src] = ab 
        
        ab = node(src)
        ab.next = self.graph[dest]
        self.graph[dest] = ab 

    def add_unidirectional_node(self,src,dest):
        ab = node(dest)
        ab.next = self.graph[src]
        self.graph[src] = ab 

    
    final_position = {}
    def print1(self):
        for i in range(self.vertices):
            bc = []
            print(i , ' -> ',end=" ")
            temp = self.graph[i]
            while (temp):
                print("-> ",temp.data,end = " ")
                bc.append(temp.data)
                temp = temp.next
            self.final_position[i] = bc
            print('\n')
        print(self.final_position)


    def bfs(self):
        s = 0
        visited = [False]*self.vertices
        queue = []
        queue.append(s)
        visited[s]=True

        while queue:
            q = queue.pop(0)
            print(q,end = " ")
            temp = self.graph[q]
            while (temp):
                if visited[temp.data]==False:
                    queue.append(temp.data)
                    visited[temp.data] = True
                temp = temp.next

    def shortest_path(self,src,dest):
        count = 1
        abc = set()
        visited_node = [False]*self.vertices
        visited_node[src]=True
        temp = self.graph[src]
        while temp:
            abc.add(temp.data)
            visited_node[temp.data]=True
            temp = temp.next

        while(True):
            tk = set()
            if dest in abc:
                break
            print(count,abc)
            for j in abc:
                temp = self.graph[j]
                while temp :
                    if visited_node[temp.data]==False:
                        tk.add(temp.data)
                        visited_node[temp.data] = True
                    temp = temp.next
            abc = tk
            if len(abc)==0:
                print("there is no path possible ")
                break
            count+=1
       

    
Graph = graph(12)
Graph.add_node(0,1)
Graph.add_node(0,9)
Graph.add_node(1,8)
Graph.add_node(3,2)
Graph.add_node(3,4)
Graph.add_node(3,5)
Graph.add_node(6,5)
Graph.add_node(7,10)
Graph.add_node(7,11)
Graph.add_node(7,6)
Graph.add_node(7,3)
Graph.add_node(8,7)
Graph.add_node(9,8)
Graph.add_node(10,11)
#Graph.shortest_path()
#Graph.print1()
#Graph.bfs()

#Graph.shortest_path_treaversal(0,11)
