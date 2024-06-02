1.
def traffic_light_change(current_state):
    if current_state == "green":
        return "yellow"
    elif current_state == "yellow":
        return "red"
    elif current_state == "red":
        return "green"
    else:
        return "Invalid state"
    



2.
def find_difference(a, b):
    return abs((a[0] * a[1] * a[2]) - (b[0] * b[1] * b[2]))




3.
def triple_trouble(s1, s2, s3):
    return ''.join(a + b + c for a, b, c in zip(s1, s2, s3))



4.
def arithmetic_operation(a, b, operator):
    operations = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b
    }
    return operations[operator]


5.
def in_asc_order(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))



6.
def sequence_sum(n):
    if n < 0:
        return f"{n}<0"
    else:
        numbers = list(range(n + 1))
        sum_result = sum(numbers)
        sequence = '+'.join(map(str, numbers))
        return f"{sequence} = {sum_result}"
    


7.
def weird_case(string):
    def transform_word(word):
        transformed = ''.join(
            char.upper() if i % 2 == 0 else char.lower()
            for i, char in enumerate(word)
        )
        return transformed
    
    return ' '.join(transform_word(word) for word in string.split())




8.
def reverse_bits(data):
    num_bytes = len(data) // 8
    chunks = [data[i*8:(i+1)*8] for i in range(num_bytes)]
    reversed_chunks = chunks[::-1]
    reversed_data = [bit for chunk in reversed_chunks for bit in chunk]
    return reversed_data








