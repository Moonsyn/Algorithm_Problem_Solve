t = int(input())


def find(v):
    if parent_ids[v] == v:
        return v
    else:
        # 경로 압축
        parent_ids[v] = find(parent_ids[v])
        # print(parent_ids)
        return parent_ids[v]


def union(v1, v2):
    if v1 != v2:
        friends[v1] = friends[v1] | friends[v2]
        del friends[v2]
        parent_ids[v2] = v1


for _ in range(t):
    f = int(input())
    friends = dict()
    parent_ids = dict()
    for network in range(f):  # 100,000
        a,b = input().split(" ")
        # print("input is {}, {}".format(a,b))
        if a not in parent_ids and b not in parent_ids:
            parent_ids[a] = a
            parent_ids[b] = a
            friends[a] = {a,b}
            print(len(friends[a]))

        elif a not in parent_ids:
            parent_ids[a] = a
            friends[a] = {a,b}
            union(a, find(b))
            print(len(friends[a]))

        elif b not in parent_ids:
            root_a = find(a)
            parent_ids[b] = root_a
            friends[b] = {a,b}
            union(root_a, b)
            print(len(friends[root_a]))

        else:
            root_a = find(a)
            root_b = find(b)
            union(root_a, root_b)
            print(len(friends[root_a]))

        # print(parent_ids)
        # print(friends)
