# สร้างกราฟจากข้อมูล edges
edges = [['AB', 1], ['BA', 5], ['AC', 8], ['CA', 2], ['AD', 7], ['DA', 14], 
         ['AE', 14], ['EA', 7], ['BC', 3], ['CB', 7], ['BD', 3], ['DB', 15], 
         ['BE', 8], ['EB', 8], ['CD', 3], ['DC', 1], ['CE', 3], ['EC', 7], ['DE', 2], ['ED', 7]]

# สร้างเมทริกซ์เตรียมสำหรับ Floyd-Warshall algorithm
inf = float('inf')
num_nodes = 5  # จำนวนโหนด (A, B, C, D, E)
matrix = [[inf] * num_nodes for _ in range(num_nodes)]

# กำหนดค่าเริ่มต้นในเมทริกซ์โดยใช้ข้อมูล edges
for edge, weight in edges:
    i = ord(edge[0]) - ord('A')
    j = ord(edge[1]) - ord('A')
    matrix[i][j] = weight

# กำหนดค่าเริ่มต้นให้เส้นทางจากโหนด i ไปยัง i เป็น 0
for i in range(num_nodes):
    matrix[i][i] = 0

# Floyd-Warshall algorithm
for k in range(num_nodes):
    print(f'รอบที่ {k + 1}:')
    for i in range(num_nodes):
        for j in range(num_nodes):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    # แสดงเมทริกซ์หลังจากรอบที่ k
    for row in matrix:
        print(row)

# แสดงผลลัพธ์ระยะทางที่สั้นที่สุดระหว่างโหนดทุกโหนด
for i in range(num_nodes):
    for j in range(num_nodes):
        if matrix[i][j] != inf:
            print(f'ระยะทางที่สั้นที่สุดจาก {chr(i + ord("A"))} ไปยัง {chr(j + ord("A"))} คือ {matrix[i][j]}')

# หาเส้นทางที่สั้นที่สุดจาก A ไปยัง C
start_node = 0  # A
end_node = 2    # C
if matrix[start_node][end_node] != inf:
    print(f'เส้นทางที่สั้นที่สุดจาก A ไปยัง C คือ {matrix[start_node][end_node]}')
else:
    print('ไม่มีเส้นทางจาก A ไปยัง C')

# หาเส้นทางที่สั้นที่สุดจาก C ไปยัง A
start_node = 2  # C
end_node = 0    # A
if matrix[start_node][end_node] != inf:
    print(f'เส้นทางที่สั้นที่สุดจาก C ไปยัง A คือ {matrix[start_node][end_node]}')
else:
    print('ไม่มีเส้นทางจาก C ไปยัง A')
