from sys import maxsize
from itertools import permutations

v=4;

def TSP(graph){
    s=int(input("Enter the node where you want to start"))
    vertex=[]
    for i in range(v):
        if i!=s:
            vertex.append()

    min_path=maxsize
    new_path=permutations(vertex)
    for j in new_path:
        currentpath_size=0

}