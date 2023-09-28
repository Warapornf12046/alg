def optimal_bst(keys, freq):
    n = len(keys)
    
    # สร้างตาราง dp สำหรับเก็บค่าต้นไม้ทวิภาคที่ดีที่สุด
    dp = [[0] * n for _ in range(n)]
    
    # สร้างตารางเพิ่มเติมสำหรับเก็บเวลาค้นหา
    search_time = [[0] * n for _ in range(n)]
    
    # กรณีพิเศษเมื่อมีโหนดเดียว
    for i in range(n):
        dp[i][i] = freq[i]
        search_time[i][i] = freq[i]
    
    # สำหรับต้นไม้ทวิภาคขนาดเพิ่มขึ้น
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            dp[i][j] = float('inf')
            
            # คำนวณค่าค้นหาต้นไม้ทวิภาคที่ดีที่สุดสำหรับระหว่าง i และ j
            for k in range(i, j + 1):
                c = sum(freq[i:j+1])  # ความน่าจะเป็นรวมของโหนดในช่วงนี้
                left = dp[i][k - 1] if k > i else 0
                right = dp[k + 1][j] if k < j else 0
                total = left + right + c
                if total < dp[i][j]:
                    dp[i][j] = total
                    search_time[i][j] = total * (j - i + 1)  # คำนวณเวลาค้นหา
    
    return dp[0][n - 1], search_time[0][n - 1]

# ตัวอย่างการใช้งาน
keys = ["A", "B", "C", "D"]
freq = [0.2, 0.1, 0.6, 0.3]  #freq = [4, 2, 6, 3]
min_cost, search_time = optimal_bst(keys, freq)
print("ค่าค้นหาต้นไม้ทวิภาคที่ดีที่สุดคือ:", min_cost)
print("เวลาค้นหาต้นไม้ทวิภาคที่ดีที่สุดคือ:", search_time)






