def prime_factors(n):
    def smallest_prime_factor(n):
        k=2
        while n % k != 0:
            k=k+1
        return k
    while n>1:
        k=smallest_prime_factor(n)
        n=n//k
        print(k)
def sum_nature(n):
    sum=0
    while n>0:
        sum+=n
        n=n-1
    print(sum)
    return sum

def adder(n):
    def adder1(k):
        print(n,k)      #内部可以找到全局，全局不可找到内部
        return n+k
    return adder1


def just_in_case():
    x = 10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x

