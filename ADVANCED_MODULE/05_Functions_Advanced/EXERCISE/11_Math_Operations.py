def math_operations(*args, **kwargs):
    float_list = list(args)
    while float_list:
        for k, v in kwargs.items():
            try:
                kwargs[k] = {
                    "a": lambda x, y: x + y,
                    "s": lambda x, y: x - y,
                    "d": lambda x, y: x / y,
                    "m": lambda x, y: x * y,
                }[k](v, float_list.pop(0))
            except ZeroDivisionError as _:
                pass
            except IndexError as _:
                break
    return "\n".join(
        [
            f"{k}: {v:.1f}"
            for k, v in sorted(
                dict(sorted(kwargs.items())).items(), key=lambda x: x[1], reverse=True
            )
        ]
    )


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
