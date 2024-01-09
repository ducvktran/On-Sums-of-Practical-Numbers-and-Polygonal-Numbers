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

#generate list of Fibonacci numbers
n_1 = 0
n_2 = 1
count = 0
fib_list = []
while count < 50:  
        fib_list.append(n_1)  
        next_term = n_1 + n_2   
        n_1 = n_2  
        n_2 = next_term  
        count += 1

#generate set of numbers not expressible as a sum
non_sums = set()
for target in range(1,limit+1):
    not_sum = True
    for i, fib_num in enumerate(fib_list):
        if fib_num > target or not_sum == False:
            break
        else:
            len_l = len(fib_list)
            l2 = fib_list[i:len_l]
            if fib_num*2 > target:
                break
            for fib_num_2 in l2:
                if fib_num_2 > target - fib_num:
                    break
                if target - fib_num - fib_num_2 in practical_numbers_set:
                    not_sum = False
                    break
    if not_sum:
        non_sums.add(target)

print(sorted(non_sums))