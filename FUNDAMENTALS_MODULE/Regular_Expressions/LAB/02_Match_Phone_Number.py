import re
from typing import List

rep = re.compile(r"(?P<Phone>\+359(?P<d>[\s|-])2(?P=d)\d{3}(?P=d)\d{4}\b)", re.VERBOSE)
results: List[str] = list()

for r in rep.finditer(input()):
    results.append(r.groupdict()["Phone"])

print(', '.join(results))
