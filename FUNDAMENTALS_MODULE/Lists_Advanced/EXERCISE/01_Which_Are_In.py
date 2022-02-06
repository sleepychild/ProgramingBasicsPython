from typing import List, Tuple

subs: Tuple[str] = (
    'arp, live, strong',
    'tarp, mice, bull',
)

strs: Tuple[str] = (
    'lively, alive, harp, sharp, armstrong',
    'lively, alive, harp, sharp, armstrong',
)

for i in range(len(subs)):
    print(subs[i], ' in ', strs[i])
    subs_list: List[str] = subs[i].split(', ')
    strs_list: List[str] = strs[i].split(', ')
