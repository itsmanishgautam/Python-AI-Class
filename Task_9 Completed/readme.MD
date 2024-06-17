# Bot for Finding Path in a Matrix

This bot is designed to find a path from a starting number to a destination number in a given matrix. It uses a greedy algorithm to select the bot's starting position and then attempts to find the shortest path to the destination number.


## Usage
# AI Engineer's Matrix Navigation Bot

This Python script demonstrates a matrix navigation bot capable of finding a path from a randomly selected starting position to a randomly chosen destination number within the matrix.

## Overview

The script consists of several functions:

1. **bot_select_from_outer_layer(matrix)**: Selects a random number from the outer layer of the matrix.

2. **choose_random_number_in_matrix(matrix)**: Chooses a random number from within the matrix.

3. **find_path(matrix, bot_number, number_to_find)**: Finds a path from the starting position (bot_number) to the destination number (number_to_find) using a modified breadth-first search algorithm.

## Example Usage

1. The user inputs a number which determines the size of the matrix.
2. The script generates a matrix of random numbers.
3. The bot selects a number from the outer layer of the matrix.
4. The script finds a path from the bot's starting position to a randomly chosen destination number within the matrix.

## Dependencies

- `math`: For mathematical operations.
- `random`: For generating random numbers.
- `collections.deque` (currently commented out): Could be used for deque operations, but not utilized in the current implementation.

## Usage

1. Run the script.
2. Input a number to determine the size of the matrix.
3. View the generated matrix and the selected numbers.
4. If a path is found, it will be displayed; otherwise, a message indicating no path is found will be shown.



## Functionality

- The bot generates a random matrix with dimensions based on the input number.
- It selects a starting number from the outer layer of the matrix and a destination number from within the matrix.
- It then attempts to find a path from the starting number to the destination number.
- If a path is found, it prints the path. Otherwise, it indicates that no path was found.

## Programmer
Manish Gautam

## Mentor, Brain
Dixanta Bahadur Shrestha