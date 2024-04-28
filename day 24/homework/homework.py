#1
def litres(time):
    return int(time * 0.5)



#2
def blank_pages(a, b):
    if a < 0 or b < 0:
        return 0
    else:
        return a * b
    

#3
def multiply(values):
    result = 1
    for num in values:
        result *= num
    return result



#4
def replace_digits(string):
    result = ''
    for char in string:
        digit = int(char)
        if digit < 5:
            result += '0'
        else:
            result += '1'
    return result





#5
def count_by(x, n):
    return [x * i for i in range(1, n + 1)]




#6
def to_jaden_case(string):
    words = string.split()
    jaden_case_words = [word.capitalize() for word in words]
    return ' '.join(jaden_case_words)




#7
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))



#8
def remove_smallest(arr):
    if not arr:
        return arr
    else:
        min_val = min(arr)
        arr.remove(min_val)
        return arr
    


#9
def sum_of_multiples(n):
    if n < 0:
        return 0
    else:
        return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)
    



#10
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"




