from collections import defaultdict

class Graph:
    def __init__ (self):   
        self.graph = defaultdict(list)

    def add_node(self,src,dest):
        self.graph[src].append(dest)


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
###############################################################################################
###############################################################################################
ab = Graph()
visited = set()

point_break = []

#ladder
ladder = [[4,14],[9,31],[20,38],[29,84],[40,59],[63,81],[71,91]]
for i in ladder:
    ab.add_node(i[0],i[1])
#snake
snake = [[17,6],[42,18],[60,42],[68,49],[87,24],[93,73],[99,46]]
for i in snake:
    ab.add_node(i[0],i[1])
    ab.add_node(i[0]-1,i[0]+1)
    point_break.append(i[0])

sta = 1
while(sta<100):
    if (sta+1) in point_break:
        sta+=2
    else:
        ab.add_node(sta,sta+1)
        sta+=1

#######################################################################################
#######################################################################################
res = ab.shortest_path_treaversal(1,100)
print("the path of the snake be like : \n" ,res)

#*****************************************************************************
# the outcome is    not 100% correct upto the day i have coded
#*****************************************************************************
counting = 0
i=0
total_step_with_value = []
while(res[i]<100):
    if res[i] +1 in res:
        print(res[i],end=" ")
        counting+=1
    elif res[i] in res:
        print(res[i])
        # lets assume there is only one value
        if counting==0:
            counting+=1

        if counting%6>0:
            final_step = counting//6 +1
        else:
            final_step = counting//6

        #print("the no of step : ",final_step,counting)
        for q in range(final_step):
            total_step_with_value.append(counting)
        counting=0
    i+=1

print(total_step_with_value)
