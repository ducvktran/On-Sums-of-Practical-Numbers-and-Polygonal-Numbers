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

practical_numbers_list = [n for n in range(1, 10**5+1) if is_practical(n)]

#list of polygonal numbers
s=4 #change the value of s as desired
polygon_num_list = [(s-2)*x*(x-1)/2+x for x in range(0, 318)]
polygon_num_set = set(polygon_num_list)

#check possible sums
possible_sums = set()
for target in range(1,10**5+1):
    for prac_num in practical_numbers_list:
        if prac_num > target:
            break
        else: 
            for polygon_num in polygon_num_list:
                if polygon_num > target - prac_num:
                    break
                if target - prac_num - polygon_num in polygon_num_set:
                    possible_sums.add(target)
                    break

#list of non sums
non_sums = [num for num in range(1, 10**5+1) if num not in possible_sums]
print(non_sums)