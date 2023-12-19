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

#list of polygonal numbers
s=4 #change the value of s as desired
polygon_num_list = [(s-2)*x*(x-1)/2+x for x in range(0, round(limit**0.5)+2)]

#generate set of numbers not expressible as a sum
non_sums = set()
for target in range(1,limit+1):
    not_sum = True
    for polygon_num in polygon_num_list:
        if polygon_num > target:
            break
        if target - polygon_num in practical_numbers_set:
            not_sum = False
            break
    if not_sum:
        non_sums.add(target)

print(len(non_sums)) #n_s in the paper
print(max(non_sums)) #N_s in the paper