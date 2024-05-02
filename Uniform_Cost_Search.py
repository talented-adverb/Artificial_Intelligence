import heapq
A=[]

def UCS(graph, start, goal):
    visited = set()
    queue = [(0, start)] #cost,node

    while queue:
        cost, node = heapq.heappop(queue) #root node is removed
        if node not in visited:
            visited.add(node)
            A.append(node)
            if node == goal:
                return cost
            for edge_cost, i in graph.get(node):# heappush adds item to heap while maintaining the heap property 
                heapq.heappush(queue, (cost + edge_cost, i))


graph = {'S': [(1, 'A'), (4, 'B')],
         'A': [(1, 'S'), (2, 'B'), (5, 'C'), (12,  'D')],
         'B': [(2, 'A'), (2, 'C'), (4, 'S')],
         'C': [(2, 'B'), (3, 'D'), (5, 'A')],
         'D': [(12, 'A'), (3, 'C')]}

UCS(graph,'S','D')
print(A)
