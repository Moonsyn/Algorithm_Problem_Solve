from collections import deque

def solution(maps):
    answer = -1
    visited = [[False for _ in range(len(maps[0]))] for __ in range(len(maps))]
    start = []
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    for i in range(len(maps)):
        if 'S' in maps[i]:
            start = [i, maps[i].index('S')]
            break
    
    queue = deque([[start, visited[::], 0, False]])
    while queue:
        node = queue.popleft()
        x, y = node[0][0], node[0][1]
        my_visit = node[1]
        if my_visit[x][y]:
            continue
        my_visit[x][y] = True
        
        if maps[x][y] == 'L' and not node[3]:
            # 레버 내리기 성공
            my_visit = [[False for _ in range(len(maps[0]))] for __ in range(len(maps))]
            node[3] = True
            
        if maps[x][y] == 'E' and node[3]:
            # 목적지 도착
            if answer == -1:
                answer = node[2]
            else:
                answer = min(answer, node[2])
            continue
            
        for direction in directions:
            new_x, new_y = x+direction[0], y+direction[1]
            if new_x < 0 or new_y < 0 or new_x >= len(maps) or new_y >= len(maps[0]):
                continue
            if my_visit[new_x][new_y] or maps[new_x][new_y] == 'X':
                continue
            queue.append([[new_x, new_y], my_visit[::], node[2]+1, node[3]])
    
    return answer