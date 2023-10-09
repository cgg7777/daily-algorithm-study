import sys

sys.setrecursionlimit(10**6)
def dfs(x,start,end):
    global count
    count += 1
    start[x] = count
    for target in edges[x]:
        dfs(target, start, end)
    end[x] = count

def updateLazy(node, start, end):
    global segTree
    global lazy

    if lazy[node] != 0:
        segTree[node] += (end-start +1) * lazy[node]
        if(start != end):
            lazy[node*2] += lazy[node]
            lazy[node*2 +1] += lazy[node]
        lazy[node] = 0

def updateSegmentTree(node, start, end, left, right, value):
    global segTree
    global lazy
    updateLazy(node, start, end)
    if left > end or  right < start:
        return

    if left <= start and end <= right:
        segTree[node] += (end - start + 1) * value
        if start != end:
            lazy[node*2] += value
            lazy[node*2+1] += value
        return

    mid = (start + end) // 2
    updateSegmentTree(node*2, start ,mid, left ,right, value)
    updateSegmentTree(node*2+1, mid+1 ,end, left ,right, value)
    segTree[node] = segTree[node*2] + segTree[node*2+1]

def getValue(node, start, end, left, right):
    global segTree

    updateLazy(node,start,end)
    if left > end or right < start:
        return 0

    if left<=start and end <=right:
        return segTree[node]

    mid = (start + end) // 2
    return getValue(node*2, start, mid, left, right) + getValue(node*2+1, mid+1, end, left, right)

global count
count = 0

N, M = map(int, sys.stdin.readline().split(' '))

start = [0] * 1000000
end = [0] * 1000000

parent = list(map(int, sys.stdin.readline().split(' ')))
edges = [[] for _ in range(N+1)]

for j, entry in enumerate(parent):
    if entry != -1:
        edges[entry].append(j + 1)

dfs(1, start, end)

global segTree
segTree = [0] * 1000000

global lazy
lazy = [0] * 1000000

values = [0] * 1000000

for i in range(M):
    command = list(map(int, sys.stdin.readline().split(' ')))
    if command[0] == 1:
        updateSegmentTree(1, 1, N+1, start[command[1]], end[command[1]], command[2])
    if command[0] == 2:
        print(getValue(1, 1, N+1, start[command[1]], start[command[1]]))