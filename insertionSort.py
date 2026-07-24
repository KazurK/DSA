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

# Insertion sort works by dividing the array into a sorted and an unsorted part. It takes one element from the unsorted part and finds its correct position in the sorted part by comparing it with the elements in the sorted part. This process is repeated until all elements are sorted.