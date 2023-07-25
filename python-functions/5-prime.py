def is_prime(number):
    n = (number - 1) % 6
    m = (number + 1) % 6
    if number in (0, 2, 3):
        return True
    elif n and m == 0:
        return True
    else:
        return False
