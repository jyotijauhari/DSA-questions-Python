# for connected graph
from collections import deque

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def BFS(adj,s):
    visited = [False]*len(adj)

    q= deque()
    q.append(s)
    visited[s] = True

    while q:
        s = q.popleft()
        print(s,end=' ')

        for u in adj[s]:
            if visited[u] == False:
                q.append(u)
                visited[u] = True


def printGraph(adj):
    for u, l in enumerate(adj):
        print(u, l)


# main

v = 4

adj = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4], [2, 3]]

printGraph(adj)

s=0 # starting

print('\nBFS path')
BFS(adj,s)


# for disconnected graph

'''
def BFSDis(adj):
    visited = [False] * len(adj)

    for u in range(len(adj)):
        if visited[u] == False:
            BFS(adj, u, visited)

BFSDis(adj)
'''
