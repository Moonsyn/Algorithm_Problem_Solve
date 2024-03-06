def solution(park, routes):
    x,y = 0,0
    
    for i in range(len(park)):
        row = park[i]
        for j in range(len(row)):
            if row[j] == 'S':
                x,y = i,j
                break
    
    for route in routes:
        direction = None
        distance = int(route[2:])
        
        if route[0] == 'W':
            direction = (0,-1)
        elif route[0] == 'E':
            direction = (0,1)
        elif route[0] == 'N':
            direction = (-1,0)
        elif route[0] == 'S':
            direction = (1,0)
            
        if x+direction[0]*distance not in range(len(park)) or y+direction[1]*distance not in range(len(park[0])):
            continue
        
        new_x, new_y = x,y
        blocked = False
        for i in range(1, distance+1):
            new_x += direction[0]
            new_y += direction[1]
            if park[new_x][new_y] == 'X':
                blocked = True
                break
        if blocked:
            continue
        x,y = new_x, new_y
    
    return [x,y]