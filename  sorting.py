from typing import List
from typing import Union

#? We can also set empty lists, sets, tuples by set(), list()

def main():

    #* .append("value"), at the end
    #* .clear(), remove all
    #* count("value"), how many are in
    #* .index("value"), what index is the "value" in
    #* insert(index, "value") a value at that indexing, replacing the original element like an array
    #* .pop(), removes first/leftmost elemente
    #* .remove("value"), 
    #* .reverse(), 
    #* .sort()
    #! Ordered and mutable, Dupes ok
    list = [3, 4, 1, 3, 9, 10, 5, 2, -3]
    set = {i for i in list}
    print("List: ", list)
    print("Set: ", set)
    
    #* .add("value")
    #* .remove("value")
    #* .pop()
    #* .clear()
    #* .update() extends new set into existing set
    #! No Dupes, immutable, unordered, add/delete OK
    set = {1, 2, 3, 4, 5}
    set.update({6, 7, 8})
    set.add(9)
    print(set.pop())
    print("Set: ", set)

    #! Ordered and mutable, dupes OK
    tuple = {1: 'Cannot', 2: 'Change', 3: 'This', 4: "tuple"}

    #* dict.__init__(key: "value"), when we init an empty dict, dict(), we can start adding values to it with __init__
    #* .update: extending a list into an existing list
    dict = {1: 'Can', 2: 'Change', 3: 'This', 4: "Dict"}
    dict.update({5: 3.14})
    print("Dict: ", dict)

    #* element in collection = whether element is in the collection
    # print(quickSort(list, 0, len(list) - 1))
    # print(mergeSort(list, 0, len(list) - 1))
    # print(insertionSort(list))
    # print(selectionSort(list))
    # print(bubbleSort(list))

def mergeSort(list: List[int], l: int, r: int) -> Union[None, List[int]]:
    if list is None:
        return None
    if len(list) == 1:
        return list

    return list

def merge(list: List[int], l, m, r) -> Union[None, List[int]]:
    
    return list

def insertionSort(list: List[int]) -> Union[None, List[int]]:
    if list is None:
        return None
    if (len(list) == 1):
        return list
    
    for i in range(1, len(list) - 1):
        j = i - 1
        while (j >= 0 and list[j] > list[j + 1]):
            list[j], list[j + 1] = list[j + 1], list[j]
            j -= 1

    return list

def selectionSort(list: List[int]) -> Union[None, List[int]]:
    if list is None:
        return None
    if len(list) == 1:
        return list

    for i in range(len(list) - 1):
        minSoFar = i
        for j in range (i, len(list)):
            if list[j] < list[minSoFar]:
                minSoFar = j

        if minSoFar is not i:
            list[i], list[minSoFar] = list[minSoFar], list[i]

    return list

def bubbleSort(list: List[int]) -> Union[None, List[int]]:
    if list is None:
        return None
    if len(list) == 1:
        return list
    
    didSwap = True
    index = len(list) - 1

    while (index > 0 and didSwap):
        didSwap = False
        for j in range(index):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                didSwap = True
        index -= 1
    return list

def quickSort(list: List[int], l: int, r: int) -> Union[None, List[int]]:
    if list is None:
        return None
    if len(list) == 1:
        return list

    if (l < r):
        pivot = partition(list, l, r)
        quickSort(list, l, pivot - 1)
        quickSort(list, pivot + 1, r)
    return list

def partition(list: List[int], l: int, r: int) -> Union[None, List[int]]:
    if list is None:
        return None
    
    spot = l - 1
    pivot = list[r]
    for i in range(l, r):
        if (list[i] < pivot):
            spot += 1
            list[spot], list[i] = list[i], list[spot]

    spot += 1
    list[spot], list[r] = list[r], list[spot]

    return spot

main()

