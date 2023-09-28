def RobotCoinCollection(C):
    n = len(C)
    m = len(C[0])
    
    F = [[0 for _ in range(m)] for _ in range(n)]
    
    F[0][0] = C[0][0]
    
    # Initialize the first row
    for j in range(1, m):
        F[0][j] = F[0][j - 1] + C[0][j]
    
    # Initialize the first column
    for i in range(1, n):
        F[i][0] = F[i - 1][0] + C[i][0]
    
    # Fill in the rest of the table using dynamic programming
    for i in range(1, n):
        for j in range(1, m):
            F[i][j] = max(F[i - 1][j], F[i][j - 1]) + C[i][j]
    
    # The largest number of coins the robot can collect is in F[n-1][m-1]
    return F[n - 1][m - 1]

# Example usage:
C = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
]

result = RobotCoinCollection(C)
print("Largest number of coins collected:", result)