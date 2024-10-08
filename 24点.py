from itertools import permutations

def can_make_24(nums):
    # 尝试所有的排列和操作符组合
    for perm in permutations(nums):
        if (perm[0] + perm[1] + perm[2] + perm[3] == 24 or
            perm[0] + perm[1] + perm[2] - perm[3] == 24 or
            perm[0] + perm[1] - perm[2] + perm[3] == 24 or
            perm[0] + perm[1] - perm[2] - perm[3] == 24 or
            perm[0] - perm[1] + perm[2] + perm[3] == 24 or
            perm[0] - perm[1] + perm[2] - perm[3] == 24 or
            perm[0] - perm[1] - perm[2] + perm[3] == 24 or
            perm[0] - perm[1] - perm[2] - perm[3] == 24):
            return True
    return False

# 读取输入
m = int(input())
results = []

for _ in range(m):
    nums = list(map(int, input().split()))
    if can_make_24(nums):
        results.append("YES")
    else:
        results.append("NO")

# 输出结果
for result in results:
    print(result)