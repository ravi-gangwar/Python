studentOfName = input("Give Student name: ")
rollNo = int(input("Give Roll No: "))

f = open("marksheet.txt", "w")

f.write("Student Name: " + studentOfName + "\n")    
f.write("Roll No: " + str(rollNo) + "\n")

howManySubject = int(input("How many subjects: "))
totalMarksAllsub = 0
totalMarksObtained = 0

f.write("-------------------------------------------------------------------------" + "\n")

f.write("Subjects Name" + "\t\t\t\t\t\t\t\t\t\t\t\t" + "Total of Subject" + "\t\t\t\t\t\t\t\t\t\t\t\t" + "Obtained Marks" + "\n")
for i in range(howManySubject):
    subject = input("Give subject name: ")
    totalMarks = int(input("Give total marks: "))
    totalMarksAllsub += totalMarks
    marks = int(input("Give marks: "))
    totalMarksObtained += marks
    f.write(subject + "\t\t\t\t\t\t\t\t\t\t\t\t" + str(totalMarks) + "\t\t\t\t\t\t\t\t\t\t\t\t" + str(marks) + "\n")

f.write("-------------------------------------------------------------------------" + "\n")

percentage = (totalMarksObtained * 100) / totalMarksAllsub
if percentage >= 33:
    f.write("\t\t\t\t\t\t\tResult: Pass" + "\n")
else:
    f.write("\t\t\t\t\t\t\tResult: Fail" + "\n")

print("Thanks for giving information")
f.close()
