import sys

def find(a):
    global parent
    if a == parent[a]:
        return a

    return find(parent[a])

def union(a,b):
    global parent
    global size

    a = find(a)
    b = find(b)
    if a == b:
        return None
    if size[a] >= size[b]:
        size[a] += size[b]
        parent[b] = a
        return a
    else:
        size[b] += size[a]
        parent[a] = b
        return b


T = int(sys.stdin.readline())

for case in range(T):
    N, M = map(int, sys.stdin.readline().split())

    parent = [i for i in range(N+1)]
    size = [1 for i in range(N+1)]

    edges = [[] for _ in range(N+1)]
    edgeList = []

    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        edgeList.append([a,b])

    count = 0
    maxCount = 0
    for edge in edgeList:
        result = union(edge[0], edge[1])
        if result is not None:
            count +=1
            if maxCount < size[result]:
                maxCount = size[result]
        if maxCount == N:
            print(count)
            break