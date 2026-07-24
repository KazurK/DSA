
sort = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(sort)
for i in range(n-1):
    minIndex = i
    for j in range(i+1, n):
        if sort[j] < sort[minIndex]:
            minIndex = j
        sort[i], sort[minIndex] = sort[minIndex], sort[i]


    print("Sorted array:", sort)

# Selection sort works by going through the array and finding the minimum element in the unsorted part of the array and swapping it with the first unsorted element. This process is repeated for all elements until the entire array is sorted.

