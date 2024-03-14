n, m = map(int, input().split(" "))
set_a = set(input().split(" "))
set_b = set(input().split(" "))

print(len(set_a - set_b) + len(set_b - set_a))