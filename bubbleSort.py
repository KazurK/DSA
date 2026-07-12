def bubbleSort():
    sort = [1, 3,45,422121212121212,66,0,0.0001]
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

if __name__ == "__main__":
    bubbleSort()