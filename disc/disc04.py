"tmd是真的难啊,可恶的递归aaaa"




def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
   生而废物，我很抱歉 """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        i = 1
        while i <= k:
            total += count_k(n - i, k)
            i += 1
        return total
    """We need to include the while loop from the count_k solution and 
    keep track of a running total for the number of successful ways 
    because we can take up to k steps. The while loop will count how many successful ways 
    if we take 1, 2, 3, ... k steps. We also need to keep track of how many successful ways 
    there are for each value of k, so we use the total variable to remember
      how many successful ways there are so far.
      You can use recursion visualizer to step through the calls made to count_k(3, 3)."""


def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    else:
        return max(max_product(s[1:]), s[0] * max_product(s[2:]))