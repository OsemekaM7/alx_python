def fibonacci_sequence(n):
    sequence = []
    if n <= 0:
        return([]) #For cases where n is 0, list must be empty
    elif n == 1:
        return([0]) #For cases where n is 1, list has one element such that len(sequence) == n
    else:
        (sequence.append(0))
        (sequence.append(1))
        while len(sequence) < n:
            (sequence.append(sequence[-1] + sequence[-2]))

    return sequence
