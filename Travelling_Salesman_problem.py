from sys import maxsize
from itertools import permutations

v=4;

def TSP(graph,s):
    vertex=[]
    for i in range(v):
        if i!=s:
            vertex.append(i)

    min_path=maxsize
    new_path=permutations(vertex)
    for j in new_path:
        currentpath_size=0
        k=s
        for l in j:
            currentpath_size+=graph[k][l]
            k=l
        currentpath_size+=graph[k][s]

        min_path=min(min_path,currentpath_size)
    return min_path

graph=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
s=int(input("Enter the starting point(0-3)"))
print(TSP(graph,s))
