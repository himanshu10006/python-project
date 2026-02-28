matrix=[]

print("enter the element of matrix:")

for i in range(2):
     row=[]
     for j in range(2):
         value = int(input("Enter the list value:"))
         row.append(value)

     matrix.append(row)

print(matrix)

for R in matrix:
    for C in R:
        print(C,end=' ')

    print()    
