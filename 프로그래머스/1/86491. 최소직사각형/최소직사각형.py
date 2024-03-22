def solution(sizes):
    answer = 0
    
    new_sizes = []
    for size in sizes:
        large = max(size[0], size[1])
        small = min(size[0], size[1])
        new_sizes.append([large,small])
    
    max_width = 0
    max_height = 0
    for size in new_sizes:
        max_width = max(max_width, size[0])
        max_height = max(max_height, size[1])
    
    return max_width * max_height