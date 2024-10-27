# step 1
#creating empty list
beatles=[]

print("Step 1:", beatles)

# step 2
#appending elements to the list
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("Harrison")

print("Step 2:", beatles)

# step 3
#taking user input
for i in range(3):
    beatles.append(input("Enter Singer Name:"))
   
print("Step 3:", beatles)

# step 4
#deleting specific elements
for i in range(2):
    del beatles[-1]

print("Step 4:", beatles)


# step 5
#inserting unique element
print("Step 5:", beatles)
beatles.insert(0,"Ringo Starr")

# testing list legth
#printong list length
print("The Fab", len(beatles))

