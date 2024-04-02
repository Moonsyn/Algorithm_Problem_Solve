def solution(N, number):
    if N == number:
        return 1
    sN = str(N)
    d = [[], set([N]), set([int(sN+sN)]), set([int(sN+sN+sN)]), set([int(sN+sN+sN+sN)]), 
         set([int(sN+sN+sN+sN+sN)]), set([int(sN+sN+sN+sN+sN+sN)]), set([int(sN+sN+sN+sN+sN+sN+sN)]), 
         set([int(sN+sN+sN+sN+sN+sN+sN+sN)])]

    for i in range(2,9):
        for j in range(i):
            for left in list(d[j]):
                for right in list(d[i-j]):
                    if right == 0:
                        continue
                    d[i].add(left+right)
                    d[i].add(left-right)
                    d[i].add(left*right)
                    d[i].add(left//right)
                    
        # print(d[i])
        if number in d[i]:
            return i
    
    return -1