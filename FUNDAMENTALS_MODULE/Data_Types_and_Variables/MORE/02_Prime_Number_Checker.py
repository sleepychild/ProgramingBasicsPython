def is_prime(num: int) -> bool:
    prime_nums_list: list = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    ]
    if num in prime_nums_list:
        return True
    elif list(str(num))[-1] in ["2", "5"]:
        return False
    else:
        for n in range(2, num):
            if (num % n) == 0:
                return False
        return True


print(is_prime(int(input())))
