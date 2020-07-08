# UNDIRECTED GRAPH

'''
ADJ MATRIX
ADJ LIST
'''

'''
V E
FOR EVERY EDGE
U V
7 9
A B
A C 
A F
C E
C F
C D
D E 
D G
G F

'''
from collections import defaultdict
graph = defaultdict(list)
v,e = map(int,input().split())
for i in range(e):
    u,v = map(str,input().split())
    graph[u].append(v)
    graph[v].append(u)
for v in graph:
    print(v,graph[v])

