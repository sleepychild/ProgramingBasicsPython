grade: float = float(input())
print(
    'Excellent' if grade >= 5.5 else
    'Very Good' if grade >= 4.5 else
    'Good' if grade >= 3.5 else
    'Poor' if grade >= 3 else
    'Fail'
)
