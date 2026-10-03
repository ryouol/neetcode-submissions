class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set() 

        for n in nums: 
            if n in seen: 
                return True
            else: 
                seen.add(n) 
        return False       




#Brute force Approach: 
# look at element  
# compare ever element in list to element 
# return true if another element equals that element 
# if not repeat until ever element has been compared  

# this is O(n*n) time 

#We can use a set since a set only allows unique values 
#thus we can interate throuhg the entire array and insert into set before we insert we check if this item is in the set if it is we return true else we insert this allows for us to interate through the array at O(n) time and insertiong is o(1) time thus O9n) tuime
