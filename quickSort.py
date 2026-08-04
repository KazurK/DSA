def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivotIndex = partition(arr, low, high)
        quicksort(arr, low, pivotIndex-1)
        quicksort(arr, pivotIndex+1, high)


sort = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(sort)
print("Sorted array:", sort)


# choose a value in the array to be the pivot element
# order the rest of the array so that lower values then the pivot element are on the left and higher values are on the right
# swap the pivot element with the first element of higher values so that the pivot element lands between the lower and higher values
# do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element