base = 0.0
height = 0.0

def read():
    global base , height
    base = float(input("enter base of triangel :"))
    height = float(input("enter height of triangel :"))

def findArea():
    A= (base*height)*0.5
    print(f'area of triangel is => {A}')

read()
findArea()
