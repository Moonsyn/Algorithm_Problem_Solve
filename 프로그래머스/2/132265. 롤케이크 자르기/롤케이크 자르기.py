from collections import deque

def solution(topping):
    answer = 0
    
    a,b = [],[]
    category_a = {}
    category_b = {}
    
    topping = deque(topping)
    
    while topping:
        len_a = len(category_a.keys())
        len_b = len(category_b.keys())
        if len_a > len_b:
            element = topping.pop()
            b.append(element)
            if str(element) not in category_b.keys():
                category_b[str(element)] = 1
            else:
                category_b[str(element)] += 1
                
        else: 
            element = topping.popleft()
            a.append(element)
            if str(element) not in category_a.keys():
                category_a[str(element)] = 1
            else:
                category_a[str(element)] += 1
                
    while len(category_a.keys()) >= len(category_b.keys()) and a:
        if len(category_a) == len(category_b):
            answer += 1
            
        moved = a.pop()        
        category_a[str(moved)] -= 1
        if category_a[str(moved)] == 0:
            del category_a[str(moved)]
        
        b.append(moved)
        if str(moved) not in category_b.keys():
            category_b[str(moved)] = 1
        else:
            category_b[str(moved)] += 1
    
    return answer