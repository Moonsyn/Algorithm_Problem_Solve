from collections import Counter


def spin(arr, arr2):
    length = len(arr)
    temp = arr[-1]
    for i in reversed(range(1, len(arr))):
        arr[i] = arr[i-1]
    arr[0] = temp

    for j in range(len(arr2)):
        arr2[j] += 1
        if arr2[j] == length:
            arr2[j] = 0


def down_robot(arr, position):
    if position in arr:
        arr.remove(position)


def move_robots(arr, arr2):
    length = len(arr)
    for i in range(len(arr2)):
        new_robot = arr2[i]+1
        if new_robot == length:
            new_robot = 0

        if arr[new_robot] > 0 and new_robot not in arr2:
            arr2[i] = new_robot
            arr[new_robot] -= 1


n, k = map(int, input().split(" "))
belt = list(map(int, input().split(" ")))

counter = Counter(belt)
robots = []
stage = 1

while counter[0] < k:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    spin(belt, robots)
    # 내리는 위치의 로봇 내리기
    down_robot(robots, n-1)

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    # 만약 이동할 수 없다면 가만히 있는다.
    # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아있어야 한다.
    move_robots(belt, robots)
    # 내리는 위치의 로봇 내리기
    down_robot(robots, n-1)

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if belt[0] > 0:
        robots.append(0)
        belt[0] -= 1

    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료
    counter = Counter(belt)
    if counter[0] >= k:
        break
    stage += 1

print(stage)
