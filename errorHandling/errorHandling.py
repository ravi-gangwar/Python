# try:
#     inp = int(input ("Enter the Number: "))
#     inp2 = int(input ("Enter the Number: ")) #if num2 is zerp its gives error so we need error handling
#     print(inp/inp2)
# except Exception as e:
#     print("Error is:", e)
# finally: 
#     print("This is Finally")


try:
    dict = {'name': 'Ravi', 'age': 20, 'city': 'New Dehli'}
    print(dict['gender'])
except KeyError as e:
    print("Error: ", e)
finally: 
    print("Finally Error")


