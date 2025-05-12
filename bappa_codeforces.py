t = int(input())
results = []

for _ in range(t):
    n = int(input())
    total = n * n

    # Prepare all numbers from 0 to n^2 - 1
    numbers = list(range(total))

    # Matrix initialized with dummy values
    matrix = [[-1 for _ in range(n)] for _ in range(n)]

    # Determine center positions
    if n % 2 == 0:
        # Even n
        m1, m2 = n // 2 - 1, n // 2
        center_positions = [(m1, m1), (m1, m2), (m2, m1), (m2, m2)]
    else:
        # Odd n
        m = n // 2
        center_positions = [(m, m), (m, m + 1), (m + 1, m), (m + 1, m + 1)]
    
    # Assign 0 to 3 to center positions
    used = set()
    for val, (i, j) in enumerate(center_positions):
        matrix[i][j] = val
        used.add(val)

    # Fill the rest of the matrix with remaining values
    idx = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == -1:
                while idx in used:
                    idx += 1
                matrix[i][j] = idx
                idx += 1

    results.append(matrix)

# Print all matrices
for matrix in results:
    for row in matrix:
        print(" ".join(map(str, row)))
