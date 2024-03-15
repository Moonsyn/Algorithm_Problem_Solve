from collections import deque

def solution(cards):
    answer = 0
    
    sets = []
    queue = deque()
    
    for i in range(len(cards)):
        card = cards[i]
        if card == 0:
            continue
        cards[i] = 0
        group = {i+1}
        queue.append(card)
        while queue:
            c = queue.popleft()
            if cards[c-1] == 0:
                continue
            group.add(c)
            queue.append(cards[c-1])
            cards[c-1] = 0
    
        sets.append(group)
    
    if len(sets) <= 1:
        return 0
    sets.sort(key=lambda x:len(x), reverse=True)
    
    return len(sets[0]) * len(sets[1])