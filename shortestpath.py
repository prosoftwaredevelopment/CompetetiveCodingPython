import heapq
from collections import defaultdict


def shortestPath(graph,src,dest):
    h = []
    # keep a track record of vertices with the cost
    # heappop will return vertex with least cost
    # greedy SRC -> MIN - > MIN -> MIN -> DEST

    heapq.heappush(h,(0,src))
   
    while len(h)!=0:
        currcost,currvtx = heapq.heappop(h)
        if currvtx == dest:
            print("Path Exisits {} to {} with cost {}".format(src,dest,currcost))
            break
        for neigh,neighcost in graph[currvtx]:
            heapq.heappush(h,(currcost+neighcost,neigh))
            
        
    
    
graph = defaultdict(list)
v,e = map(int,input().split())
for i in range(e):
    u,v,w = map(str,input().split())
    graph[u].append((v,int(w)))
src,dest = map(str,input().split())
shortestPath(graph,src,dest)
