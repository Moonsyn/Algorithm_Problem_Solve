import heapq

def solution(operations):
    answer = []
    
    max_heap = []
    min_heap = []
    
    for op in operations:
        splited = op.split(" ")
        operation = splited[0]
        num = int(splited[1])
        
        if operation == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif len(max_heap) == 0 or len(min_heap) == 0:
            continue
        elif num == -1:
            minimum = heapq.heappop(min_heap)
            max_heap.remove(-minimum)
        elif num == 1:
            maximum = heapq.heappop(max_heap)
            min_heap.remove(-maximum)
    
    if len(max_heap) > 0 and len(min_heap) > 0:
        answer.append(-max_heap[0])
        answer.append(min_heap[0])
    else:
        answer = [0,0]
    
    return answer