#lex_auth_01269441913243238467

def create_largest_number(number_list):
    number = number_list.sort()
    highest_num = ""
    for num in number:
        highest_num = highest_num + str(num)
    return highest_num




number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)