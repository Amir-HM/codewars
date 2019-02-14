def BFS():
    level = {s:0}
    parent = {s:None}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            for v in Adj[u]:
                level[v] = i
                parent[v] = u
                next.append(v)
        frontier = next
        i += 1
