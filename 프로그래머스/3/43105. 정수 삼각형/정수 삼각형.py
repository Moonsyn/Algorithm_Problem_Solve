def dp(triangle, graph, n, m):
    if graph[n][m] >= 0:
        return graph[n][m]
    
    if m == 0:
        graph[n][m] = dp(triangle, graph, n-1, m) + triangle[n][m]
    elif m == n:
        graph[n][m] = dp(triangle, graph, n-1, m-1) + triangle[n][m]
    else:
        graph[n][m] = max(dp(triangle, graph, n-1, m-1), dp(triangle, graph, n-1, m)) + triangle[n][m]
    
    return graph[n][m]


def solution(triangle):    
    n = len(triangle)
    graph = [[-1 for _ in range(n)] for __ in range(n)]
    graph[0][0] = triangle[0][0]
    
    max_value = 0
    for i in range(n):
        max_value = max(max_value, dp(triangle, graph, n-1, i))
    
    return max_value