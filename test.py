def find_adjacent_around(matrix, target):
    adjacent = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Find the position of the target value in the matrix
    target_position = None
    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == target:
                target_position = (row, col)
                break
        if target_position:
            break
    
    if not target_position:
        return None  # Target value not found in the matrix

    # Check adjacent elements to the left, right, up, down, and diagonals
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dr, dc in directions:
        new_row, new_col = target_position[0] + dr, target_position[1] + dc
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
            adjacent.append(matrix[new_row][new_col])
    
    return adjacent

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target_value = 1
adjacent_numbers = find_adjacent_around(matrix, target_value)
if adjacent_numbers:
    print("Adjacent numbers around {}: {}".format(target_value, adjacent_numbers))
else:
    print("Target value {} not found in the matrix.".format(target_value))
