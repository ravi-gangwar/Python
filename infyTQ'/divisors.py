def find_smallest_number(n):
    try:
        n = int(n)
        if n <= 0:
            raise ValueError("Input must be a positive integer.")
    except ValueError as e:
        return str(e)
    
    def count_divisors(num):
        divisors = 0
        for i in range(1, num + 1):
            if num % i == 0:
                divisors += 1
        return divisors

    
    number = 1
    while True:
        if count_divisors(number) == n:
            return number
        number += 1

try:
    n = int(input("Enter a positive integer: "))
    result = find_smallest_number(n)
    print(f"The smallest number with {n} divisors is: {result}")
except ValueError as e:
    print(str(e))

