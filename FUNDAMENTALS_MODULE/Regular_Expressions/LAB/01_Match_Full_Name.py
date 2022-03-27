import re

print(' '.join(re.findall(
    r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b",
    input()
)))
