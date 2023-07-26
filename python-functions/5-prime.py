def is_prime(number):
    n = (number - 1) % 6
    m = (number + 1) % 6
    if number == 2 or number == 3:
        return True
    elif n == 0 or m  == 0:
        return True
    else:
        return False
