a=100 #globel

def fun1():
    print(a)

def fun2():
    global a # global is update
    a=500
    print(a)


fun1()#100
fun2()#500
fun1()#500


#now without using global keyword

print("without using globel keyword")
x=100

def fun3():
    print(x)
def fun4():
    x=500
    print(x)

fun3()#100
fun4()#500
fun3()#100
    
