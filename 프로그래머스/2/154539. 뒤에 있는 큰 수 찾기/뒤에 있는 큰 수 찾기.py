def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    
    not_pulled = []
    
    for i in range(len(numbers)):
        num = numbers[i]
        for j in reversed(range(len(not_pulled))):
            if num > not_pulled[j][0]:
                answer[not_pulled[j][1]] = num
                not_pulled.pop(j)
            else:
                break
        not_pulled.append((num, i))
            
    
    return answer