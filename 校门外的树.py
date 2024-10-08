L, M = map(int, input().split())
total = L + 1

remove = set()

def re(start, stop):
    for i in range(start, stop + 1):
        remove.add(i)

for _ in range(M):
    start, stop = map(int, input().split())
    re(start, stop)
remaining_trees = total - len(remove)

print(remaining_trees)