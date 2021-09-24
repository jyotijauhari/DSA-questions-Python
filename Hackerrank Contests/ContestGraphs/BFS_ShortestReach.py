from collections import defaultdict

class Graph:

    def __init__(self):
        self.neighbours = defaultdict(list)

    def add_edge(self, u, v):
        self.neighbours[u].append(v)
        self.neighbours[v].append(u)

    def bfs(self, i, n):

        level = [-1] * (n + 1)
        queue = []
        level[i] = 0
        queue.append(i)

        while queue:
            head = queue.pop(0)
            for k in self.neighbours[head]:
                if level[k] == -1:
                    level[k] = 6 + level[head]
                    queue.append(k)

        return level

if __name__ == '__main__':
    q = int(input())
    for case in range(q):
        e = input().split()
        n = int(e[0])
        m = int(e[1])
        g = Graph()

        for edge in range(m):
            e = input().split()
            u = int(e[0])
            v = int(e[1])
            g.add_edge(u, v)

        s = int(input())
        distance = g.bfs(s, n)
        distance_temp = []
        for i in distance[1:]:
            if i > 0:
                distance_temp.append(str(i))
            if i < 0:
                distance_temp.append(str(-1))

        print(" ".join(distance_temp))


# def bfs(i, n, E):
#
# 	level = [-1] * (n+1)
# 	queue = []
# 	level[i] = 0
# 	queue.append(i)
#
# 	while len(queue) > 0:
# 		head = queue[0]
# 		queue = queue[1:]
# 		for j,k in E:
# 			if j == head:
# 				if level[k] == -1:
# 					level[k] = 1 + level[j]
# 					queue.append(k)
#
# 	return level
#
#
# q = int(input())
# for case in range(q):
# 	e = input().split(" ")
# 	n = int(e[0])
# 	m = int(e[1])
# 	E = []
#
# 	for edge in range(m):
# 		e = input().split(" ")
# 		u = int(e[0])
# 		v = int(e[1])
# 		E.append([u,v])
#
# 	s = int(input())
# 	distance = bfs(s, n, E)
# 	dist = []
# 	for i in distance[1:]:
# 		if i > 0:
# 			dist.append(str(i*6))
# 		if i < 0:
# 			dist.append(str(-1))
#
# 	print(" ".join(dist))
