def fibonacci_sequence(n):
    sequence = []
    if n == 0:
        return([])
    elif n < 2:
        return([])
    else:
        (sequence.append(0))
        (sequence.append(1))
        while len(sequence) < n:
            (sequence.append(sequence[-1] + sequence[-2]))

    return sequence
