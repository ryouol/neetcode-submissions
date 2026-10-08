class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums: 
            count[n] += 1
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        res = [] 


        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res

        



"""
Brute force: 
- Count the frequency of each element in the array 
- Sort the array on each elements frequency 
- return top k elements 
- This would be nlogn solution 

Approach: 
- intiaizlie a default dict 
- loop through eachj eleme2nt in the array 
    - if the elemenet does not exisit in the frequency map insert it into the map 
    - find element i at key i and +=1 to its value 

- Create a freq array 
- insert number n into index frequency 
- couint backwards from end to k 


"""