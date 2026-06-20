import array as arr

# Create an array
a = arr.array("i",(1,3,5,3,7,9,3))
print("Original array: "+str(a))

print("Number of occurrences of 3 in the array: "+str(a.count(3)))

#array reverse

a.reverse()
print("reverse the order of items")
print(str(a))
