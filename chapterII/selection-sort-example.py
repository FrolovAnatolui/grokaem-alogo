def findSmallest(arr):
    smallest = arr[0] # - To store the smallest value
    smallest_index = 0 # - To store the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

print(findSmallest([1,2,3,0,-1,4,5]))

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5,2,3,4,56,7]))