#spiral matrix
def generate_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    top, bottom, left, right = 0, n - 1, 0, n - 1
    while num <= n * n:
        # Fill from left to right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Fill from top to bottom
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Fill from right to left
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # Fill from bottom to top
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix

# Example usage
n = 4
spiral_matrix = generate_spiral_matrix(n)
for row in spiral_matrix:
    print(*row)
