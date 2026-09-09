from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    queue = deque(arr)
    
    for i in range(k): 
        k = queue[0] 
        queue.popleft()
        queue.append(k)
    
    return queue



# convert arr to a deque then rotate the vlaues in the list to the left by k steps and return the deque 


# Thus we need to pop the first k elements off and appened


# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
