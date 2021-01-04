def memoize(fun):
    """Memoizes a function of one argument."""
    the_dict = {}
    def wrapper_decorator(*args, **kwargs):
        assert len(args) == 1, "Only works with one argument"
        if args[0] not in the_dict:
            the_dict[args[0]] = fun(args[0])
        return the_dict[args[0]]
    return wrapper_decorator


@memoize
def fib(n):
    """Calculates the n'th fibonacci number (memo-ized version).

    Args:
        n: Which Fibonacci number to return

    Returns: the n'th Fibonacci number.
    """
    if n >= 2:
        return fib(n-2) + fib(n-1)
    else:
        return 1
