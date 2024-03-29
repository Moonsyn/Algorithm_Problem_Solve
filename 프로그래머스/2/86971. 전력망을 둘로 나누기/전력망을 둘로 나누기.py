from collections import deque

def bfs(node_list, graph, q, visited, n, numbering):
    while q:
        node = q.popleft()
        visited[node] = True
        numbering += 1
            
        for next_node in range(1, n+1):
            if graph[node][next_node] == 1 and not visited[next_node]:
                q.append(next_node)
                node_list.remove(next_node)

    return numbering

def solution(n, wires):
    answer = -1
    n = len(wires) + 1
    graph = [[0 for _ in range(n+1)] for __ in range(n+1)]
    nodes = set([])
    
    for wire in wires:
        a,b = wire[0], wire[1]
        graph[a][b] = 1
        graph[b][a] = 1
        nodes.update(wire)
        
    min_diff = n+1
    
    for wire in wires:
        a,b = wire[0], wire[1]
        graph[a][b] = 0
        graph[b][a] = 0
        
        node_list = list(nodes)
        queue = deque()
        queue.append(node_list.pop(0))
        
        visited = [False for _ in range(n+1)]
        
        one = bfs(node_list, graph, queue, visited, n, 0)
    
        queue.append(node_list.pop(0))
    
        two = bfs(node_list, graph, queue, visited, n, 0)
        
        min_diff = min(min_diff, abs(one-two))
        
        graph[a][b] = 1
        graph[b][a] = 1
        
    
    return min_diff