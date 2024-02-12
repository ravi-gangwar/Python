# try:
#     inp = int(input ("Enter the Number: "))
#     inp2 = int(input ("Enter the Number: ")) #if num2 is zerp its gives error so we need error handling
#     print(inp/inp2)
# except Exception as e:
#     print("Error is:", e)
# finally: 
#     print("This is Finally")


# try:
#     dict = {'name': 'Ravi', 'age': 20, 'city': 'New Dehli'}
#     print(dict['gender'])
# except KeyError as e:
#     print("Error: ", e)
# finally: 
#     print("Finally Error")


class InvalidMarksError(Exception):
    def __init__(self, message="Invalid marks. Marks should be between 0 and 100."):
        self.message = message
        super().__init__(self.message)

def get_subject_marks():
    marks = []
    for i in range(5):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i + 1}: "))
                if mark < 0 or mark > 100:
                    raise InvalidMarksError()
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    return marks

try:
    subject_marks = get_subject_marks()
    print("Entered subject marks:", subject_marks)
except InvalidMarksError as e:
    print(f"Error: {e}")
finally:
    print("do you want to enter again")
    choice = input("Enter y/n: ")
    if choice.lower() == 'y':
        get_subject_marks()
