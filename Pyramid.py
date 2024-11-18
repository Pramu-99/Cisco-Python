blocks = int(input("Enter the number of blocks: "))

height=0
layer=1
while layer<=blocks:
    height+=1
    blocks-=layer
    layer+=1

print("The height of the pyramid:", height)