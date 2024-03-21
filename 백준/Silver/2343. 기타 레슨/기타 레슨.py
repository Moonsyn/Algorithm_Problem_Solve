n, m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
left = max(arr)  # 9
right = sum(arr)  # 45
enables = []

while left <= right:
    mid = (left+right) // 2
    index = 0
    count = 0
    sub_sum = 0
    is_fit = False
    while count < m and index < n:
        sub_sum += arr[index]
        if sub_sum > mid:
            count += 1
            sub_sum = 0
        elif sub_sum == mid:
            is_fit = True
            index += 1
        else:
            index += 1

    if index < n:
        left = mid+1
    else:
        if is_fit:
            enables.append(mid)
        right = mid-1

print(min(enables))
