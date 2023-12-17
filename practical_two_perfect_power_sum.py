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
    not_sum = True
    for perf_power in perfect_power_list:
        if perf_power > target or not_sum == False:
            break
        else:
            for perf_power_2 in perfect_power_list:
                if perf_power_2 > target - perf_power:
                    break
                if target - perf_power - perf_power_2 in practical_numbers_set:
                    not_sum = False
                    break
    if not_sum:
        non_sums.add(target)

print(sorted(non_sums))