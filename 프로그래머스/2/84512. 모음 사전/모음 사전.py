def solution(word):
    answer = 1
    search = "A"
    
    order = ['A', 'E', 'I', 'O', 'U']

    while search != word:
        if len(search) < 5:
            search += "A"
        else:
            for i in reversed(range(5)):
                if search[i] != 'U':
                    idx = order.index(search[i])
                    search = search[:i] + str(order[idx+1])
                    break
        answer += 1
    
    return answer