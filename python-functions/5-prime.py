def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False

    # We only need to check divisors up to the square root of the number
    # to determine if it's a prime number.
    # Any divisor larger than the square root would have a corresponding
    # divisor smaller than the square root.
    max_divisor = int(number ** 0.5) + 1
    for divisor in range(3, max_divisor, 2):
        if number % divisor == 0:
            return False

    return True

