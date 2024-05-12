# from sys import maxsize
# from itertools import permutations

# v=4
# def tr_S(graph,s):
#     vertex=[]
#     for i in range(4):
#         if i!=s:
#             vertex.append(i)

#     min_path=maxsize    
#     new_path=permutations(vertex)
#     for j in new_path:
#         currentpath_size=0
#         k=s
#         for l in j:
#             currentpath_size+=graph[k][l]
#             k=l
#         currentpath_size+=graph[k][s]
#         min_path=min(min_path,currentpath_size)
#     return min_path

# graph=[[0,10,15,20],[10,0,35,25],[15,25,0,30],[20,25,30,0]]
# s=int(input("Enter starting point"))
# print(tr_S(graph,s))

# import heapq
# a=[]

# def ucs(graph,start,goal):
#     visited=set()
#     queue=[(0,start)]
#     while queue:
#         cost, node =heapq.heappop(queue)
#         if node not in visited:
#             visited.add(node)
#             a.append(node)
#             if (node==goal):
#                 return cost
#             for edge_cost,node in graph.get(node):
#                 heapq.heappush(queue,(cost+edge_cost,node))    

# graph = {'S': [(1, 'A'), (4, 'B')],
#          'A': [(1, 'S'), (2, 'B'), (5, 'C'), (12,  'D')],
#          'B': [(2, 'A'), (2, 'C'), (4, 'S')],
#          'C': [(2, 'B'), (3, 'D'), (5, 'A')],
#          'D': [(12, 'A'), (3, 'C')]}

# ucs(graph,'S','D')
# print(a)

# 8 puzzle 

# def print_in_format(state):
#     for i in range(9):
#         if((i%3==0) and (i>0)):
#             print()
#         print(state[i],end=" ")

# def move(arr,p,st):
#     store_st=st.copy()
#     rh=99999
#     for i in range(len(arr)):
#         dupl_st=st.copy()

#         temp=dupl_st[p]
#         dupl_st[p]=dupl_st[arr[i]]
#         dupl_st[arr[i]]=temp

#         t=count(dupl_st)
#         if t<rh:
#             rh=t
#             store_st=dupl_st.copy()
#     return store_st,rh


# def count(state):
#     c=0
#     ideal=[1,2,3,
#            4,5,6,
#            7,8,9
#         ]
#     for i in range(9):
#         if ((state[i]!=ideal[i]) and (state[i]!=0)):
#             c+=1
#     return c


# state=[1,2,3,
#        0,5,6,
#        4,7,8
#       ]

# h=count(state)
# print(h)

# print_in_format(state)

# while(h>0):
#     p=state.index(0)
#     if p==0:
#         arr=[1,3]
#         state,h=move(arr,p,state)
#     elif(p==1):
#         arr=[0,2,4]
#         state,h=move(arr,p,state)
#     elif p==2:
#         arr=[1,5]
#         state,h=move(arr,p,state)
#     elif p==3:
#        arr=[0,4,6]
#        state,h=move(arr,p,state)
#     elif p==4:
#        arr=[1,3,5,7]
#        state,h=move(arr,p,state)
#     elif p==5:
#        arr=[2,4,8]
#        state,h=move(arr,p,state)
#     elif p==6:
#        arr=[3,7]
#        state,h=move(arr,p,state)
#     elif p==7:
#        arr=[4,6,8]
#        state,h=move(arr,p,state)
#     elif p==8:
#         arr=[5,7]
#         state,h=move(arr,p,state)


# print('\n')
# print_in_format(state)

a=[1,2,3]
b=a 
a.append(4)
print(b)