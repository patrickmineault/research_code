def fib(n):
    if n >= 2:
        return fib(n-1) + fib(n-2)
    else:
        assert n != 2
        return 1

if __name__ == '__main__':
    print("Tests running")
    assert fib(0) == 1  # expect 1
    assert fib(2) == 2  # 2
    assert fib(4) == 5  # 5
    print("Tests passed")