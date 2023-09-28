def max_profit(n):
    prices = [0, 2, 5, 6, 9, 11]  # ราคาตามความยาวของเชือก
    dp = [0] * (n + 1)  # สร้างตารางเก็บผลลัพธ์
    
    for i in range(1, n + 1):
        max_val = -float('inf')
        for j in range(1, min(i, 5) + 1):
            max_val = max(max_val, prices[j] + dp[i - j])
        dp[i] = max_val
    
    return dp[n]

n = 7
# profit = max_profit(n)
# print(f"={profit} bath")
print(max_profit(n))