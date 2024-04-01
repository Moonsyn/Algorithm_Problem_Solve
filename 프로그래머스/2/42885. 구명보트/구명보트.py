def solution(people, limit):
    answer = 0
    
    people.sort()
    left = 0
    right = len(people)-1
    
    while left <= right:
        if left == right:
            answer += 1
            break
            
        if people[right] + people[left] > limit:
            right -= 1
            answer += 1
        else:
            right -= 1
            left += 1
            answer += 1
    
    return answer