def rope(length , price):
      n = len(price)   
      dp = [0] * (n+1)
      for i in range(1,n+1):
            rope = -float('inf') #-float('inf') ทำให้ตัวแปรมีค่ามากที่สุด
            for j in range(i):
                  rope = max(rope, price[j] +dp[i-j-1])
                  dp[i] = rope
            return dp[n]

price= [2,5,6,9,11]
length = 5
maxResult = rope(length,price)
print(maxResult)