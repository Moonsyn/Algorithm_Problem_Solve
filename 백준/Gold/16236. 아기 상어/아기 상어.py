from collections import deque

n = int(input())
graph = []
shark = [0,0]  # [행,열]
size = 2
eaten = 0
for i in range(n):
    row = list(map(int, input().split(" ")))
    if 9 in row:
        shark[0] = i
        shark[1] = row.index(9)
        row[shark[1]] = 0
    graph.append(row)

directions = [(1,0), (-1,0), (0,1), (0,-1)]
time = 0
while True:
    can_eats = []

    node = [shark[0], shark[1], 0]
    queue = deque([node])
    visited = [[False for _ in range(n)] for __ in range(n)]
    while queue:
        current = queue.popleft()
        r,c,d = current[0],current[1],current[2]

        if visited[r][c]:
            continue
        visited[r][c] = True

        fish = graph[r][c]
        if 0 < fish < size:
            can_eats.append(current)
            continue

        for di in directions:  # [5,0], [4,1], [5,2]
            new_r = r + di[0]
            new_c = c + di[1]
            if new_r < 0 or new_r >= n or new_c < 0 or new_c >= n:
                continue
            if visited[new_r][new_c]:
                continue
            if graph[new_r][new_c] > size:
                continue

            queue.append([new_r,new_c,d+1])

    if len(can_eats) == 0:
        break

    position = [n,n]
    distance = n*n
    for fish in can_eats:
        d = fish[2]
        if d < distance:
            distance = d
            position = fish
        elif d == distance:
            if fish[0] < position[0]:
                position = fish
            elif fish[0] == position[0]:
                if fish[1] < position[1]:
                    position = fish

    shark = position
    time += distance
    graph[shark[0]][shark[1]] = 0

    eaten += 1
    if eaten == size:
        size += 1
        eaten = 0

print(time)
