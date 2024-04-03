from collections import deque

def solution(begin, target, words):
    answer = len(words) + 1
    length = len(begin)
    
    visited = {}
    for key in words:
        visited[key] = False
    
    node = [begin, 0]
    queue = deque([node])
    
    while queue:
        node = queue.popleft()
        visited[node[0]] = True
        
        if node[0] == target:
            answer = min(answer, node[1])
            continue
            
        for word in words:
            if visited[word]:
                continue
            diff = 0
            for i in range(length):
                if word[i] != node[0][i]:
                    diff += 1
                if diff > 1:
                    break
            
            if diff > 1:
                continue
                
            queue.append([word, node[1]+1])
    
    if answer == len(words)+1:
        answer = 0
    
    return answer