def match_k(k):
    def check(x):
        i = 0
        while 10 ** (i + k) < x:
            if (x // 10**i) % 10 != (x // 10 ** (i + k)) % 10:
                return False
            i = i + 1
        return True
    return check

# BEGIN SOLUTION NO PROMPT
# Alternate solution
def match_k_alt(k):
    """ Return a function that checks if digits k apart match

    >>> match_k_alt(2)(1010)
    True
    >>> match_k_alt(2)(2010)
    False
    >>> match_k_alt(1)(1010)
    False
    >>> match_k_alt(1)(1)
    True
    >>> match_k_alt(1)(2111111111111111)
    False
    >>> match_k_alt(3)(123123)
    True
    >>> match_k_alt(2)(123123)
    False
    """
    def check(x):
        while x // (10 ** k):
            if (x % 10) != (x // (10 ** k)) % 10:
                return False
            x //= 10
        return True
    return check
# END SOLUTION