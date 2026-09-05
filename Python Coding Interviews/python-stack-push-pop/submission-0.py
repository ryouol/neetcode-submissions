from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    temp = 0  
    new_arr = []
    for i in range(len(arr)): 
        temp = arr.pop() 
        new_arr.append(temp)
    return new_arr
        



#Takes in arr and returns a new list in reverse order 
# we can approach this by arr.pop() and new_arr.insert() 

# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
