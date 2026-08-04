
sort = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(sort)
for i in range(n-1):
    minIndex = i
    for j in range(i+1, n):
        if sort[j] < sort[minIndex]:
            minIndex = j
        sort[i], sort[minIndex] = sort[minIndex], sort[i]


    print("Sorted array:", sort)

# go though the array and find the lowest value. 
# move the lowest value to the front of the array.
# loop though the array as many time as there are values