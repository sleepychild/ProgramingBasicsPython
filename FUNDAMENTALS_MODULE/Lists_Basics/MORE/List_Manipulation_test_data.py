from typing import Tuple

input_data: Tuple[str] = (
    '1 3 5 7 9',
    '1 10 100 1000',
    '1 10 100 1000',
    '1 8 2 3',
    '1 1 2 2 3 3 6 6',
    '1 2 3 6',
)

results_data: Tuple[str] = (
    '[3, 5, 7, 9, 1]',
    '[10, 100, 1000, 1]',
    '[1, 10, 100, 1000]',
    '[]',
    '[]',
    '[]',
)

input_data_cmd: Tuple[Tuple[str]] = (
    (
        'exchange 1',
        'max odd',
        'min even',
        'first 2 odd',
        'last 2 even',
        'exchange 3',
        'end',
    ),(
        'max even',
        'first 5 even',
        'exchange 10',
        'min odd',
        'exchange 0',
        'max even',
        'min even',
        'end',
    ),(
        'exchange 3',
        'first 2 odd',
        'last 4 odd',
        'end',
    ),(
        'first 2 odd',
        'first 2 even',
        'last 2 odd',
        'last 2 even',
        'end',
    ),(
        'last -10 even',
        'last -1 even',
        'last 0 even',
        'last 1 even',
        'last 10 even',
        'end',
    ),(
        'first 2 odd',
        'first 2 even',
        'last 2 odd',
        'last 2 even',
        'end',
    ),
)