
sort = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(sort)
for i in range(n-1): #Loop through sort
    swapped = False
    for x in range(n-i-1): #closing loop through sort
        if sort[x] > sort[x+1]:
            sort[x], sort[x+1] = sort[x+1], sort[x]
            swapped = True
            
    if not swapped:
        break

print("Sorted array:", sort)

# bubble sort works by repeatedly swapping adjacent elements if they are in the wrong order. This process is repeated until the entire array is sorted.