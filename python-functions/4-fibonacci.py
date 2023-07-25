def fibonacci_sequence(n):
    sequence = []
    if n == 0 or None:
        return([])
    else:
        while len(sequence) < n:
            (sequence.append(0))
            (sequence.append(1))
            (sequence.append(sequence[-1] + sequence[-2]))

    return sequence
# print(fibonacci_sequence())
