from sympy import perfect_power
from sympy import factorint

#definition of practical numbers (modified from OEIS A005153)
def is_practical(n):
    if n & 1:
        return n == 1
    if n%4 != 0 and n%3!=0:
        return n==2
    f = factorint(n)
    P = (2 << f.pop(2)) - 1
    for p in f:
        if p > 1 + P:
            return False
        P *= p**(f[p] + 1) // (p - 1)
    return True

limit = 10**8

practical_numbers_list = [n for n in range(1, limit+1) if is_practical(n)]
practical_numbers_set = set(practical_numbers_list)

#list of perfect powers
perfect_power_list = [m for m in range(0, limit+1) if m==0 or m==1 or perfect_power(m)]

#generate set of numbers not expressible as a sum
non_sums = set()
for target in range(1,limit + 1):
    if target%8 == 1:
        continue    #It's proven that all natural numbers of the form 8k+1 can be written as a sum of a practical number and a square, so we skip them here.
    not_sum = True
    for perf_power in perfect_power_list:
        if perf_power > target:
            break
        if target - perf_power in practical_numbers_set:
            not_sum = False
            break
    if not_sum:
        non_sums.add(target)

#lists of even and odd non sums
even_non_sums = [num for num in range(1, limit+1) if not num % 2 and num in non_sums]
odd_non_sums = [num for num in range(1, limit+1) if num % 2 and num in non_sums]
print(max(even_non_sums))
print(len(even_non_sums))
print(max(odd_non_sums))
print(len(odd_non_sums))