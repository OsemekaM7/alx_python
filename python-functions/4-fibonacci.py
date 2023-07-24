def fibonacci_sequence(n):
    sequence = [0,1]
    if n == 0 or None:
        return([])
    else:
        while len(sequence) < n:
            (sequence.append(sequence[-1] + sequence[-2]))
        return sequence
