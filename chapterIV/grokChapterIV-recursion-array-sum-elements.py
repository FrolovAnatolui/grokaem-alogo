def arrSum(arr):
    sum = 0
    count = 0
    length = len(arr)
    next = count + 1
    if (len(arr) == 1):
        sum = +arr[0]
        return sum
    else:
        sum = sum + arr[count]
        return sum + arrSum(arr[next:length])

def recursion_sum(arr):
    if not arr:
        return 0
    return arr[0] + recursion_sum(arr[1:])

print(arrSum([123,7,12,3,4,5,7]))

#my_list = [1,2,3,4,5]
# my_list[1:3] # Outputs [2,3]
# my_list[::2] # Outputs [1,3,5]