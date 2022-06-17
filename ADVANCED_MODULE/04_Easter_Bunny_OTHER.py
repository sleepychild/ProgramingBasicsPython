from typing import List, Tuple, Generator, Callable


DEBUG: bool = True

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '5',
        '1 3 7 9 11',
        'X 5 4 X 63',
        '7 3 21 95 1',
        'B 1 73 4 9',
        '9 2 33 2 0',
    ), (
        '8',
        '4 18 9 7 24 41 52 11',
        '54 21 19 X 6 34 75 57',
        '76 67 7 44 76 27 56 37',
        '92 35 25 37 52 34 56 72',
        '35 X 1 45 4 X 37 63',
        '105 X B 2 12 43 5 19',
        '48 19 35 20 32 27 42 4',
        '73 88 78 32 37 52 X 22',
    ), (
        '5',
        '1 1 X 1 1',
        '1 1 2 1 1',
        '1 1 B 1 1',
        '1 1 1 1 1',
        '1 1 1 1 1',
    ), (
        '3',
        '1 2 1',
        '1 B 1',
        '1 1 1',
    ), (
        '5',
        '0 0 0 0 0',
        '0 0 0 0 0',
        '0 0 B 0 0',
        '0 0 0 0 0',
        '0 0 0 0 0',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


def solution():

    def direction_valid(row, col):
        return all([
            row in range(n),
            col in range(n)
        ])

    def get_bunnie_row_col(direction, bunnie_row, bunnie_col):
        if direction == "up":
            bunnie_row, bunnie_col = bunnie_row - 1, bunnie_col
        elif direction == "down":
            bunnie_row, bunnie_col = bunnie_row + 1, bunnie_col
        elif direction == "left":
            bunnie_row, bunnie_col = bunnie_row, bunnie_col - 1
        elif direction == "right":
            bunnie_row, bunnie_col = bunnie_row, bunnie_col + 1

        return bunnie_row, bunnie_col

    def play(bunnie_row, bunnie_col, best_direction, best_score, best_path):
        directions = ["up", "down", "left", "right"]
        for direction in directions:
            # Initial default values for every step
            current_row, current_col = bunnie_row, bunnie_col
            current_score = 0
            current_path = []

            while True:
                current_row, current_col = get_bunnie_row_col(
                    direction, current_row, current_col)

                is_directions_valid = direction_valid(current_row, current_col)
                if not is_directions_valid or matrix[current_row][current_col] == 'X':
                    break
                else:
                    current_path.append([current_row, current_col])
                    current_score += int(matrix[current_row][current_col])
                    if current_score > best_score:
                        best_direction = direction
                        best_score = current_score
                        best_path = current_path

        return best_score, best_direction, best_path

    n = int(input())
    matrix = []

    bunnie_row = 0
    bunnie_col = 0

    best_score = 0
    best_direction = ""
    best_path = list()

    # Create matrix:
    for row in range(n):
        line = input().split()
        matrix.append(line)
        for col in range(n):
            if line[col] == "B":
                bunnie_row = row
                bunnie_col = col

    best_score, best_direction, best_path = play(
        bunnie_row, bunnie_col, best_direction, best_score, best_path)

    # Prints results
    # if best_score > 0:
    print(best_direction)
    for path in best_path:
        print(path)
    print(best_score)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
