def topsort(g,vtx):
    degree = [0]*vtx
    for node in g:
        for adjnode in g[node]:
            degree[adjnode]+=1

            
    bfs = [i for i in range(vtx) if degree[i] == 0]
    for node in bfs:
        for adjnode in g[node]:
            degree[adjnode]-=1
            if degree[adjnode] == 0:
                bfs.append(adjnode)
    return bfs
    

from collections import defaultdict
g = defaultdict(list)
vtx,e = map(int,input().split())
for i in range(e):
    u,v = map(str,input().split())
    u = ord(u) - ord('A')
    v = ord(v) - ord('A')
    g[u].append(v)
topSort = topsort(g,vtx)
topSort = [chr(i+65) for i in topSort]
print(topSort)
