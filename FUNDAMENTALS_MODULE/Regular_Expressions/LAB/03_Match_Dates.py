import re
from typing import Dict

for r in re.finditer(r"\b(?P<day>\d{2})(?P<_sep>.)(?P<month>\w{3})(?P=_sep)(?P<year>\d{4})\b", input(), re.VERBOSE):
    rd: Dict[str, str] = r.groupdict()
    print(f"Day: {rd['day']}, Month: {rd['month']}, Year: {rd['year']}")
