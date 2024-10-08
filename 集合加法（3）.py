def find():
    n = 0
    s = int(input())
    a = int(input())
    A = list(map(int, input().split()))
    b = int(input())
    B = list(map(int, input().split()))
    b_counts={}
    for q in B:
        if q in b_counts:
            b_counts[q] += 1
        else:
            b_counts[q] = 1
    for p in A:
        if s-p in b_counts:
            n+=b_counts[s-p]
    print(n)
n=int(input())
for i in range(n):
    find()