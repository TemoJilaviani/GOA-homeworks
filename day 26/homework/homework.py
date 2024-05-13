1.
def twice_as_old(dad_years_old, son_years_old):
    age_difference = dad_years_old - 2 * son_years_old

    return abs(age_difference)



2.
def sum_str(a, b):
    a = int(a) if a else 0
    b = int(b) if b else 0
    
    return str(a + b)


3. 
def reverse_seq(n):
    return list(range(n, 0, -1))



4.
def no_space(x):
    return x.replace(" ", "")



5.
def abbrev_name(name):
    first_name, last_name = name.split()

    initials = first_name[0].upper() + "." + last_name[0].upper()

    return initials



6. 
import math

def divisors(n):
    if n <= 1:
        return []

    divisors_list = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors_list.append(i)
            if n // i != i:
                divisors_list.append(n // i)

    if divisors_list:
        return sorted(divisors_list)
    else:
        return f"{n} is prime"

print(divisors(12)) 
print(divisors(25)) 
print(divisors(13)) 



7.
def divisors_count(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

print(divisors_count(4)) 
print(divisors_count(5))  
print(divisors_count(12)) 
print(divisors_count(30)) 



8.
def capitals_indices(word):
    indices = []
    for i, char in enumerate(word):
        if char.isupper():
            indices.append(i)
    return indices

print(capitals_indices("CodEWaRs")) 


