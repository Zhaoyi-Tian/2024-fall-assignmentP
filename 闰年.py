n, k = map(int, input().split())

# 用列表来模拟多项式系数，coeffs[i]表示x^i的系数
coeffs = [1] + [0] * n
for _ in range(1, k):
    new_coeffs = [0] * (n + 1)
    for i in range(len(coeffs)):
        for j in range(i, n + 1):
            new_coeffs[j] += coeffs[i]
    coeffs = new_coeffs

ans = 0
for i in range(n // k, n + 1):
    ans += coeffs[i]
print(ans)