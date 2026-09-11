import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    reverse_sorted = [] 
    negated_nums = [-n for n in nums] 

    heapq.heapify(negated_nums) 

    while negated_nums: 
        reverse_sorted.append(-heapq.heappop(negated_nums)) 
    
    return reverse_sorted



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
