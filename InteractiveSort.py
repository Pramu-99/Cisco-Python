#defining an empty list
numbers=[]

#defining flag variable
isSwapped=True
num=int(input("Enter Length of the List:"))

#iteration through for loop
for i in range(num):
    val=float(input(f"Enter List Element {i+1}:"))
    numbers.append(val)

#printing unsorted list
print("Unsorted List:",numbers)
while isSwapped:
    isSwapped=False
    for i in range(len(numbers)-1):
        if numbers[i]>numbers[i+1]:
            isSwapped=True
            numbers[i],numbers[i+1]=numbers[i+1],numbers[i]

print("Sorted List:",numbers)