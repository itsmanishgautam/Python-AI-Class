def find_path(matrix, bot_number, number_to_find):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    visited = [[False] * num_cols for _ in range(num_rows)]
    visited_count = 0

    # Find the starting position of the bot_number
    start_row, start_col = None, None
    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == bot_number:
                start_row, start_col = row, col
                break
        if start_row is not None:
            break

    if start_row is None:
        print("Bot number not found in the matrix.")
        return None
    
    current_row, current_col = start_row, start_col
    path = [matrix[current_row][current_col]]

    while matrix[current_row][current_col] != number_to_find:
        visited[current_row][current_col] = True
        visited_count += 1

        adjacent = find_adjacent(matrix, current_row, current_col)
        min_distance = float('inf')
        next_row, next_col = None, None

        for r, c in adjacent:
            if not visited[r][c]:
                distance = abs(matrix[r][c] - number_to_find)
                if distance < min_distance:
                    min_distance = distance
                    next_row, next_col = r, c
        
        if next_row is None or next_col is None:
            print("Number {} not found in the matrix reachable from bot number {}.".format(number_to_find, bot_number))
            return None
        
        current_row, current_col = next_row, next_col
        path.append(matrix[current_row][current_col])

    return path

def find_adjacent(matrix, row, col):
    adjacent = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Check adjacent elements to the left, right, up, down, and diagonals
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
            adjacent.append((new_row, new_col))
    
    return adjacent

# Generate a 10x10 matrix
import random
matrix = [[random.randint(1, 100) for _ in range(4)] for _ in range(4)]
print(matrix)

bot_number = 1
number_to_find = 90

path = find_path(matrix, bot_number, number_to_find)
if path:
    print("Path from bot number {} to number {}: {}".format(bot_number, number_to_find, path))
