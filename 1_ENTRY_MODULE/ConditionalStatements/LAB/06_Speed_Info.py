a: float = float(input())
print(
    "slow" if a <= 10 else
    "average" if a <= 50 else
    "fast" if a <= 150 else
    "ultra fast" if a <= 1000 else
    "extremely fast"
)
