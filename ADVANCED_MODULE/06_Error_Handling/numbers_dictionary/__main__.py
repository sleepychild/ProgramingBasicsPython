import importlib
from typing import Callable, Tuple
from helpers import get_run_generator
from os import path
from json import load
from argparse import ArgumentParser

if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser(description="Numbers Dictionary Solver")
    parser.add_argument(
        "--inputs",
        required=False,
        dest="inputs",
        default="",
        type=str,
        help="Path to a json file holding test run inputs",
        action="store",
    )
    parser.add_argument(
        "--solution",
        required=False,
        dest="solution",
        default="first",
        type=str,
        help='The solution to test. Available options are "first" and "second".',
    )
    args = parser.parse_args()
    solution: Callable[[None], None] = importlib.import_module(args.solution).solution

    if path.exists(args.inputs):
        print(f"Loading inputs file: {args.inputs}")
        with open(args.inputs, "r") as jf:
            test_runs: Tuple[Tuple[str]] = tuple(map(tuple, load(jf)))
        for test_run in test_runs:
            input: Callable[[], str] = get_run_generator(test_run)
            __builtins__.input = input
            solution()
    else:
        solution()
