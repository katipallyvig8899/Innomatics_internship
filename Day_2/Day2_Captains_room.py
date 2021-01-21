n=int(input())

set_a = set()
set_b = set()

for item in map(int, input().strip().split()):
    if item not in set_a:
        set_a.add(item)
    else:
        set_a.discard(item)
        set_b.add(item)

print(sum(set_a - set_b))
