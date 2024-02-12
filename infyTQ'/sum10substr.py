def find_ten_substring(num_str):
    try:
        if not num_str.isdigit():
            raise ValueError("Input must be a string containing only digits.")
    except ValueError as e:
        return str(e)

    def find_substrings(s):
        substrings = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if sum(map(int, substring)) == 10:
                    substrings.append(substring)
        return substrings
    
    result = find_substrings(num_str)
    return result

try:
    input_str = input("Enter a string of digits: ")
    result = find_ten_substring(input_str)
    print(f"The 10-substrings of {input_str} are: {result}")
except ValueError as e:
    print(str(e))
