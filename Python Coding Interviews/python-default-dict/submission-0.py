from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:

    freq = defaultdict(int) 

    for c in s: 
        freq[c] += 1  
    return freq
    
    # takes in a string and returns a dict where the ketys are charcters in the string and the vlaues are the nuymber of times each charcter appears in the string 

    # approach: string can act like a list of cars  
    # create a freq default dict int 
    # loop through string if charcter appears more than once ++



def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    dict_list = defaultdict(list)

    for num in nums: 
        key = num[0]
        dict_list[key].extend(num[1:])
        
    return dict_list





# take a list of lists and return a dict where the keys are the first element of each list and the values are the rest of the elements. 

# create a defaultdict(list) 
# loop through list of listsmaking the first element a key and the rest appending to the value




# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
