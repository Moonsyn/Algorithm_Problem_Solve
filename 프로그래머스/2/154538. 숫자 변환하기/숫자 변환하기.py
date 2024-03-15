def solution(x, y, n):
    d = [float('inf') for _ in range(y+1)]
    d[x] = 0
    
    for i in range(x, y+1):
        if d[i] == float('inf'):
            continue
        a = i*3
        b = i*2
        c = i+n
        if a <= y:
            d[a] = min(d[a], d[i]+1)
            
        if b <= y:
            d[b] = min(d[b], d[i]+1)
        
        if c <= y:
            d[c] = min(d[c], d[i]+1)
    if d[y] == float('inf'):
        return -1
    return d[y]