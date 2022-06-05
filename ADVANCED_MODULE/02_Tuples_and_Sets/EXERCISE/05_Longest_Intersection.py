from typing import Generator, Callable, Tuple, Set, Dict, List


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "3",
        "0,3-1,2",
        "2,10-3,5",
        "6,15-3,10",
    ),
    (
        "5",
        "0,10-2,5",
        "3,8-1,7",
        "1,8-2,4",
        "4,7-2,5",
        "1,10-2,11",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    intersections: List[Dict] = list()
    for _ in range(int(input())):
        line_in: str = input()
        str_a, str_b = line_in.split("-")
        a_start, a_end = str_a.split(",")
        set_a: Set[int] = set(range(int(a_start), int(a_end) + 1))
        b_start, b_end = str_b.split(",")
        set_b: Set[int] = set(range(int(b_start), int(b_end) + 1))
        intersection: Set = set_a.intersection(set_b)
        intersections.append(
            {"length": len(intersection), "intersection": intersection}
        )
    longest: Set = intersections[0]
    for intersection in intersections:
        if intersection["length"] > longest["length"]:
            longest = intersection
    if DEBUG:
        tuple(map(print, intersections))
    intersections.sort(key=lambda x: x["length"])
    if DEBUG:
        tuple(map(print, intersections))
    if DEBUG:
        print(longest)

    print(
        f"Longest intersection is {list(longest['intersection'])} with length {longest['length']}"
    )


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
