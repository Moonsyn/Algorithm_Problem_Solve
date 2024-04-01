from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split(" ")))
d = [1]
x = [arr[0]]

for i in range(1, n):
    if arr[i] > x[-1]:
        x.append(arr[i])
        d.append(d[-1] + 1)
    else:
        index = bisect_left(x, arr[i])
        x[index] = arr[i]

print(d[-1])