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

#generate list of Lucas numbers
n_1 = 2
n_2 = 1
count = 0
lucas_list = []
while count < 50:  
        lucas_list.append(n_1)  
        next_term = n_1 + n_2   
        n_1 = n_2  
        n_2 = next_term  
        count += 1

#generate set of numbers not expressible as a sum
non_sums = set()
for target in range(1,limit+1):
    not_sum = True
    for lucas_num in lucas_list:
        if lucas_num > target or not_sum == False:
            break
        else:
            for lucas_num_2 in lucas_list:
                if lucas_num_2 > target - lucas_num:
                    break
                if target - lucas_num - lucas_num_2 in practical_numbers_set:
                    not_sum = False
                    break
    if not_sum:
        non_sums.add(target)

print(sorted(non_sums))