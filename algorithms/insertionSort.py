sort = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(sort)
for i in range(1, n):
    insertIndex = i
    currentValue = sort[i]
    for j in range(i-1, -1, -1):
        if sort[j] > currentValue:
            sort[j+1] = sort[j]
            insertIndex = j
        else:
            break
    sort[insertIndex] = currentValue


print ("Sorted array:", sort)

# take the first value from the unsorted part of the array
# move the value into the correct place in the sorted part of the array
# go through the unsorted part of the array as many times as there are values