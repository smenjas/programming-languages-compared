def factorial(n):
    """ Returns n times each consecutive smaller natural number. """
    if not isinstance(n, int):
        raise TypeError("argument must be an integer")
    if n < 1:
        raise ValueError("argument must not be negative")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
