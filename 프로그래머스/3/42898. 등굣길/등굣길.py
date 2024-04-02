def dp(d,m,n,puddles):
    if d[m][n] > 0:
        return d[m][n]
    if m == 1 and n == 1:
        return 1
    if [m,n] in puddles:
        return 0

    if m == 1:
        d[m][n] = dp(d,m,n-1,puddles)
    elif n == 1:
        d[m][n] = dp(d,m-1,n,puddles)
    else:
        d[m][n] = dp(d,m-1,n,puddles) + dp(d,m,n-1,puddles)

    return d[m][n]


def solution(m, n, puddles):
    answer = 0
    
    d = [[0 for _ in range(n+1)] for __ in range(m+1)]
    
    return dp(d,m,n,puddles) % 1000000007