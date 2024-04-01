def union_find(parents, a, b):
    root = min(parents[a], parents[b])
    unified = max(parents[a], parents[b])
    
    for idx in range(len(parents)):
        if parents[idx] == unified:
            parents[idx] = root
    
    return parents

def solution(n, costs):
    answer = 0
    
    parents = [i for i in range(n)]
    costs.sort(key=lambda x:x[-1])
    
    for c in costs:
        a = c[0]
        b = c[1]
        cost = c[2]
        
        if parents[a] == parents[b]:
            continue
        
        answer += cost
        
        parents = union_find(parents, a, b)
        
    return answer