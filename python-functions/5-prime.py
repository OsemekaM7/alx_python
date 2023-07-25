def is_prime(number):
    n = (number - 1) % 6
    m = (number + 1) % 6
    if number == 2 or 3:
        return True
    elif n or m != 0:
        return False
    else:
        return True
