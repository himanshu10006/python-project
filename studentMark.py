student=[]

print("print student number:")

for i in range(3):
    marks=[]
    for j in range(3):
        m= int(input("Enter student marks:"))
        marks.append(m)

    student.append(marks)

print(student)    
