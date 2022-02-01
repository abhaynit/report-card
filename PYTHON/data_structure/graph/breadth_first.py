from create_graph import make_graph
from blue_print_graph import graph

ky = make_graph()
ky.print_the_graph()
ky.find_shortest_path(0,8)








"""
# code to find the least step to reach the final position
ky.print_the_graph()
print()
t = graph.final_position

count = 1
star = 0 
abc = set()
visited_node = [False]*12
visited_node[0]=True
for i in t[star]:
    abc.add(i)
    visited_node[i]=True

while(True):
    tk = set()
    if 4 in abc:
        break
    print(count,abc)
    for j in abc:
        for k in t[j]:
            if visited_node[k]==False:
                tk.add(k)
                visited_node[k] = True
    abc = tk
    count+=1

"""







