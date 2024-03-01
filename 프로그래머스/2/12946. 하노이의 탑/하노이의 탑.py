def hanoi(num, start, target, spare):
    if num == 1:
        return [[start, target]]
    else:
        return hanoi(num-1, start, spare, target) + [[start, target]] + hanoi(num-1, spare, target, start)
    
    
def solution(n):
    return hanoi(n, 1, 3, 2)