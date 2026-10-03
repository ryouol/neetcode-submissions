class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {} 
        if len(s) != len(t): 
            return False

        for c in s: 
            if c in count: 
                count[c] += 1 
            else: 
                count[c] = 1
            
        for f in t: 
            if f not in count: 
                return False 
            count[f] -= 1 
            if count[f] == 0: 
                del count[f]
            
        if len(count) == 0: 
            return True 




#Brute force: 
#We can sort each string with ''.join(sorted(s))
#if sorted1 = sorted 2 than we have an valid anagram and return true 
#if else we return false. but this is nlogn * nlogn

#HAshmap soln (since we dont care about order but only count)
#$if the len of str 1 and str 2 are not == we reutrn false 

#: we insert Str 1 into a Hashmap char by char 
#: as we loop throuhg str 1 if char already exsitis in hahsmap 
#: we key + 1 
#: if not we just insert into hashmap 

#then move onto str 2 we would iterate throuhg the str char by char 
#if that char is in the hashmap we would fo key - 1 
#if it is not in the map we return false 

#if hashmap emprt we return true  

#now in a hash map we hash to key to see sotrage bucket value 
#Thus the key is char and the vlaue is the count 
