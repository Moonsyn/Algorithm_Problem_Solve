def solution(wallpaper):
    min_x = 50
    min_y = 50
    max_x = -1
    max_y = -1

    for x in range(len(wallpaper)):
        files = wallpaper[x]
        for y in range(len(files)):
            file = files[y]
            if file == '#':
                print(x, y)
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)
    
    return [min_x, min_y, max_x+1, max_y+1]