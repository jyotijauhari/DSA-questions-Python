def addEdge(listt, u, v):
    listt[u].append(v)
    listt[v].append(u)


def printGraph(listt):
    for u, l in enumerate(listt):
        print(u, l)


# main

v = 4

listt = [[] for i in range(v)]
addEdge(listt, 0, 1)
addEdge(listt, 0, 2)
addEdge(listt, 1, 2)
addEdge(listt, 1, 3)

printGraph(listt)
