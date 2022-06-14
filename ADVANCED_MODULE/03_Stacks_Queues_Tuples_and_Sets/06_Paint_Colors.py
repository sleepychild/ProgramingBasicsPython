from collections import deque
from typing import Generator, Callable, Tuple, Deque, List

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    ("d yel blu e low redd",),
    ("r ue nge ora bl ed",),
    ("re ple blu pop e pur d",),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


primary_colors: Tuple[str] = (
    "red",
    "yellow",
    "blue",
)

secondary_colors: Tuple[str] = (
    "orange",  # 0 = 0 + 1
    "purple",  # 1 = 0 + 2
    "green",  # 2 = 1 + 2
)

color_requirements: Tuple[Tuple[str, str]] = (
    ("red", "yellow"),
    ("red", "blue"),
    ("yellow", "blue"),
)


def solution() -> None:
    colors: Deque[str] = deque(input().split())
    colors_found: List[str] = list()

    while colors:
        color_a: str = colors.popleft()
        try:
            color_b: str = colors.pop()
        except IndexError as e:
            if color_a in primary_colors or color_a in secondary_colors:
                colors_found.append(color_a)
            else:
                color_a = color_a[:-1]
                if color_a:
                    colors.append(color_a)
        else:
            if any(
                (
                    f"{color_a}{color_b}" in primary_colors,
                    f"{color_a}{color_b}" in secondary_colors,
                )
            ):
                colors_found.append(f"{color_a}{color_b}")
            elif any(
                (
                    f"{color_b}{color_a}" in primary_colors,
                    f"{color_b}{color_a}" in secondary_colors,
                )
            ):
                colors_found.append(f"{color_b}{color_a}")
            else:
                insert_position: int = len(colors) // 2
                color_a = color_a[:-1]
                if color_a:
                    colors.insert(insert_position, color_a)
                color_b = color_b[:-1]
                if color_b:
                    colors.insert(insert_position, color_b)

    for color in colors_found:
        if color in secondary_colors:
            if not all(
                [
                    (col in colors_found)
                    for col in color_requirements[secondary_colors.index(color)]
                ]
            ):
                while color in colors_found:
                    colors_found.remove(color)

    print(colors_found)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
