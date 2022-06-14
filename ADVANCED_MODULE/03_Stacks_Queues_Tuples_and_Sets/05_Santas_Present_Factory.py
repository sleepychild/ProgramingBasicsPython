from collections import deque
from typing import Generator, Callable, Tuple, Deque, List

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "10 -5 20 15 -30 10",
        "40 60 10 4 10 0",
    ),
    (
        "30 5 15 60 0 30",
        "-15 10 5 -15 25",
    ),
    (
        "30 10",
        "15 10 5 0 10",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


present: Tuple[str] = (
    "Doll",
    "Wooden train",
    "Teddy bear",
    "Bicycle",
)
magic_needed: Tuple[int] = (150, 250, 300, 400)


def solution() -> None:
    materials: Deque[int] = deque(map(int, input().split()))
    magics: Deque[int] = deque(map(int, input().split()))

    crafted_presents: List[str] = list()

    while materials and magics:
        crafting_result: int = materials[-1] * magics[0]
        try:
            crafted_present: str = present[magic_needed.index(crafting_result)]
        except ValueError as e:
            if DEBUG:
                print(e)
            if materials[-1] == 0 or magics[0] == 0:
                if materials[-1] == 0:
                    materials.pop()
                if magics[0] == 0:
                    magics.popleft()
            elif crafting_result < 0:
                materials.append(materials.pop() + magics.popleft())
            else:
                magics.popleft()
                materials[-1] += 15
        else:
            materials.pop()
            magics.popleft()
            crafted_presents.append(crafted_present)

    print(
        "The presents are crafted! Merry Christmas!"
        if any(
            [
                "Doll" in crafted_presents and "Wooden train" in crafted_presents,
                "Teddy bear" in crafted_presents and "Bicycle" in crafted_presents,
            ]
        )
        else "No presents this Christmas!"
    )
    if materials:
        print("Materials left:", ", ".join(map(str, reversed(materials))))
    if magics:
        print("Magic left:", ", ".join(map(str, magics)))
    crafted_presents.sort()
    while crafted_presents:
        crafted_present: str = crafted_presents[0]
        crafted_present_count: int = crafted_presents.count(crafted_present)
        print(f"{crafted_present}: {crafted_present_count}")
        while crafted_present in crafted_presents:
            crafted_presents.remove(crafted_present)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
