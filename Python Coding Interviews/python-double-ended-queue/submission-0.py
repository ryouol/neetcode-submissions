from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    queue = deque(arr)

    for i in range(k) : 
        x = queue[-1] 
        queue.pop() 
        queue.appendleft(x) 
    return queue


# the
# convert list into a deque and then rotate the vlaues in the list to the right bt k steps and return the deque 

# Thus first queue = deque(arr)

# Loop through queue and save item we are going pop at the right end of the qyeye and then append to the end thu
# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
