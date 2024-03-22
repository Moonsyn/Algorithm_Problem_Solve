def solution(prices):
    answer = [0 for _ in range(len(prices))]
    
    stack = []  # (index, value)
    
    for i in range(len(prices)):
        price = prices[i]
        while stack:
            if stack[-1][1] > price:
                prev = stack.pop()
                index = prev[0]
                answer[index] = i - index
            else:
                break
        stack.append((i, price))
    
    length = len(prices)
    while stack:
        left = stack.pop()
        answer[left[0]] = length-left[0]-1

    return answer