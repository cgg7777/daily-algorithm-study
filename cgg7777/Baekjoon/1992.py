import sys

N = int(sys.stdin.readline().rstrip())
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, sys.stdin.readline().rstrip()))

def quadTree(x_start, x_end, y_start, y_end):
    global arr
    if x_start == x_end:
        return str(arr[x_start][y_start])

    x_gap = x_end - x_start
    y_gap = y_end - y_start

    first = str(quadTree(x_start, x_start + x_gap//2, y_start, y_start + y_gap//2))
    second = str(quadTree(x_start, x_start + x_gap//2, y_start + y_gap//2+1, y_end))
    third = str(quadTree(x_start + x_gap // 2 +1, x_end, y_start, y_start + y_gap // 2))
    firth = str(quadTree(x_start + x_gap // 2 +1, x_end, y_start + y_gap//2+1, y_end))

    if len(first) == 1:
        if first == second == third == firth:
            return first

    return "(" + first + second + third + firth + ")"


print(quadTree(0, N-1, 0, N-1))

