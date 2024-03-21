n, m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

time = max(max(arr), sum(arr) // m)
indexes = []
index = 0

for i in range(m-1):
    sub_list = arr[index:index+1]
    sub_time_sum = sum(sub_list)

    while sub_time_sum <= time and index < n:
        index += 1
        if index == n:
            break
        sub_time_sum += arr[index]

    indexes.append(index)

indexes.append(n)

# print(time, indexes)

while True:
    sub_list = []
    # print(time, indexes)  # arr = [9,8,7,6,5,4,3,2,1]
    for i in range(len(indexes)):  # indexes = [1,3,9]
        index = indexes[i]
        if i == 0:
            sub_list = arr[:index]
        else:
            sub_list = arr[indexes[i-1]:index]

        sub_time_sum = sum(sub_list)

        while index < n:
            if sub_time_sum + arr[index] <= time:
                sub_time_sum += arr[index]
                index += 1
            else:
                break

        indexes[i] = index

    if sum(sub_list) <= time:
        # print(sub_list)
        print(time)
        break
    time += 1
