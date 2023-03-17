def countElems(list):
    if list == []:
        return 0
    return 1 + countElems(list[1:])


print(countElems([1,2,3]))

# print([1,2,3][1:])