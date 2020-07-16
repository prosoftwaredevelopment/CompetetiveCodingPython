from collections import defaultdict

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
# T.C = O(V+E)
# S.C = O(V)
def dfs(graph,start,visited,path):
    path.append(start)
    visited[start] = True
    for neighbour in graph[start]: # O(V+E)
        if visited[neighbour] == False: # O(1)
            dfs(graph,neighbour,visited,path)
    return path
            
    

v,e = map(int,input().split())
graph = defaultdict(list)
for i in range(e):
    u,v = map(str,input().split())
    graph[u].append(v)
    graph[v].append(u)

path = []
start = 'A'
visited = defaultdict(bool)
traversedpath = dfs(graph,start,visited,path)
print(traversedpath)
