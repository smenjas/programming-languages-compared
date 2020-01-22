def euclid(x, y):
    """ Return the greatest common divisor of two integers. """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("arguments must be integers")
    if (x < 1) or (y < 1):
        raise ValueError("arguments must be natural numbers")

    # Make sure x is the largest.
    if x < y:
        x, y = y, x

    while True:
        # If y is a factor of x, return y.
        if x % y == 0:
            return y
        x, y = y, x % y
        if y < 1:
            return 0
