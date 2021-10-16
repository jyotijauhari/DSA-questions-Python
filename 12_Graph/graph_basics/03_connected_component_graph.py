from collections import deque


def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


def BFS(adj, s, visited):
    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        s = q.popleft()
        print(s, end=' ')

        for u in adj[s]:
            if visited[u] == False:
                q.append(u)
                visited[u] = True

    print()


def BFSDis(adj):
    visited = [False] * len(adj)

    res = 0

    for u in range(len(adj)):
        if visited[u] == False:
            res+=1
            BFS(adj, u, visited)

    return res


def printGraph(adj):
    for u, l in enumerate(adj):
        print(u, l)


# main

v = 8

adj = [[1, 2], [0, 2], [0, 1], [4], [3], [6,7], [5],[5]]

printGraph(adj)

print('\nconnected component')
print('no of connected component',BFSDis(adj))
