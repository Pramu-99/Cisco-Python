numbers=[6,7,3,1,2]
isSwapped=True

#printing unsorted list
print("Unsorted List:",numbers)
while isSwapped:
    isSwapped=False
    for i in range(len(numbers)-1):
        if numbers[i]>numbers[i+1]:
            isSwapped=True
            
            #swapping by easy approach
            numbers[i],numbers[i+1]=numbers[i+1],numbers[i]


print("Sorted List:",numbers)