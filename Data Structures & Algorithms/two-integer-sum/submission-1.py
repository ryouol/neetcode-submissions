class Solution: 

    def twoSum(self, nums: List[int], target: int)-> List[int]: 
        seen = {} 
        for i in range(len(nums)): 
            num = nums[i]
            rem = target - num 
            if rem in seen: 
                return [seen[rem], i]
            seen[num] = i










#approach: 

#create a seen hashmap where key is the value and key is the index 

#loop throuhg nums get the remanider of target - nums[i] 
#check if the remainder exisits in hashmap if not add the nums[i] into the hashmap move onto the next value this should have a On run time and On space solution 
