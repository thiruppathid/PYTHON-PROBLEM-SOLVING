
from collections import defaultdict
d={}
v=3
#V = 4, edges[][] = {{0, 1}, {1, 2}, {1, 3}, {2, 3}, {3, 0}}
def addedge(vertex,edge):
    if vertex in d:
        d[vertex].append(edge)
    else:
        d[vertex]=[edge]
    
    #d[edge]=(vertex)
for _ in range(v+2):
    addedge(int(input()),int(input()))
#print(d)
for key,ele in d.items():
    print(key,"->",*ele)
    