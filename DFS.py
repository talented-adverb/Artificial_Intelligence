#Explore the depth untill the end and then backtrack
#using recursive function 

visited=set()
graph={'a':['b','c','d'],'b':['e'],'c':['d','e'],'d':[],'e':[]} #connection of b to a already listed therefore not listed again and so on

def dfs(visited,graph,root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited,graph,neighbour)


dfs(visited,graph,'a')
 