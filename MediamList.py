list1 = [1,7,5,50]=,40,6,5]
a = len(list1)

if a%2!=0:
    mid = a//2
    print(f'Mediam is :{list1[mid]}')

else:
    mid = a//2
    print(f' mediam is: {(list1[mid] + list1[mid-1])//2}')
