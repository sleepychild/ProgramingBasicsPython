from typing import Callable, List

def make_filter_function(haystack: List[str]):
    def fltr_fnc(needle:str):
        for hay in haystack:
            if needle in hay:
                return True
        return False
    return fltr_fnc

subs_list: List[str] = input().split(', ')
filter_function: Callable[[str], bool] = make_filter_function(input().split(', '))
print(list(filter(filter_function, subs_list)))
