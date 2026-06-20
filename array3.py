import array as arr

a = arr.array("i",(1,2,3,4,5,6,7,8,9,10))

even = []
odd = []

for c in a:
    if c % 2 == 0:
        even.append(c)
    else:
        odd.append(c)
print('Even numbers in array are: ', even)
print('Odd numbers in array are: ', odd)

