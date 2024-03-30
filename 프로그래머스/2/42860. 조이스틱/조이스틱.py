def solution(name):
    answer = 0
    
    length = len(name)
    word = ["A" for _ in range(len(name))]
    alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
                 "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    visited_cursors = [0]
    
    for cursor in range(length):
        target = name[cursor]
        letter = 'A'
        
        index = alphabets.index(target)
        word[cursor] = target
        
        move = min(index, 26-index)
        answer += move
        
        if move > 0 and cursor > 0:
            visited_cursors.append(cursor)
    
    min_count = length
    
    for right in range(len(visited_cursors)):
        move = 0
        now_cursor = 0
        left = len(visited_cursors) - right - 1
    
        for i in range(right):
            move += visited_cursors[i+1] - now_cursor
            now_cursor = visited_cursors[i+1]
            
        for j in range(left):
            plus = now_cursor - visited_cursors[-(j+1)]
            if plus < 0:
                plus += length
            move += plus
            now_cursor = visited_cursors[-(j+1)]
        
        min_count = min(move, min_count)
        
        
    for right in range(len(visited_cursors)):
        move = 0
        now_cursor = 0
        left = len(visited_cursors) - right - 1
            
        for j in range(left):
            plus = now_cursor - visited_cursors[-(j+1)]
            if plus < 0:
                plus += length
            move += plus
            now_cursor = visited_cursors[-(j+1)]
            
        for i in range(right):
            plus = visited_cursors[i+1] - now_cursor
            if plus < 0:
                plus += length
            move += plus
            now_cursor = visited_cursors[i+1]
        
        min_count = min(move, min_count)
    
    return answer + min_count