from typing import Dict, Callable

operations: Dict[str, Callable[[int, int], any]] = {
    "multiply": lambda x, y: x * y ,
    "divide": lambda x, y: x / y ,
    "add": lambda x, y: x + y ,
    "subtract": lambda x, y: x - y ,
}

print(int(operations[input()](int(input()),int(input()))))
