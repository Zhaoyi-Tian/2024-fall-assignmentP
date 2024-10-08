n = int(input())
li = list(map(int, input().split()))
li1 = sorted(li)

# 计算前缀和
prefix_sum_li = [0]
for num in li:
    prefix_sum_li.append(prefix_sum_li[-1] + num)

prefix_sum_li1 = [0]
for num in li1:
    prefix_sum_li1.append(prefix_sum_li1[-1] + num)

q = int(input())
for i in range(q):
    type, l, r = map(int, input().split())
    if type == 1:
        # 使用前缀和计算区间和
        print(prefix_sum_li[r] - prefix_sum_li[l-1])
    elif type == 2:
        # 使用前缀和计算区间和
        print(prefix_sum_li1[r] - prefix_sum_li1[l-1])