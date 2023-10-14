# สร้างกราฟจากข้อมูล edges
edges = [['AB', 1], ['BA', 5], ['AC', 8], ['CA', 2], ['AD', 7], ['DA', 14], 
         ['AE', 14], ['EA', 7], ['BC', 3], ['CB', 7], ['BD', 3], ['DB', 15], 
         ['BE', 8], ['EB', 8], ['CD', 3], ['DC', 1], ['CE', 3], ['EC', 7], ['DE', 2], ['ED', 7]]
# หาจำนวนโหนดในกราฟ
num_nodes = 5  # เราสามารถคำนวณจากจำนวนอักษรที่ใช้ในชื่อโหนด (A, B, C, D, E)

# สร้างเมทริกซ์เตรียมสำหรับ Adjacency Matrix
matrix = [[0] * num_nodes for _ in range(num_nodes)]

# กำหนดค่าในเมทริกซ์โดยใช้ข้อมูล edges
for edge, weight in edges:
    i = ord(edge[0]) - ord('A')
    j = ord(edge[1]) - ord('A')
    matrix[i][j] = weight

# แสดง Adjacency Matrix
for row in matrix:
    print(row)
