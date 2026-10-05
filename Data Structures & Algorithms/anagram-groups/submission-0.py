class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 
        for s in strs: 
            count = [0] * 26 
            for c in s: 
                count[ord(c) - ord('a')] += 1 
            res[tuple(count)].append(s) 
        return list(res.values())
"""
Question: 
- Given a list of strings 
- Group anagrams togehter into sublists 
- return list of sublists

- Brute force: 
- Input string into hashmap and then compare if 5h3e string is same length with hash map 

- use an array of size 26 since theres only 26 letters ikn the alphamet to cound the frequency of each charcter in a string then we can use this array as the key in the hahsmap to group the strings. 
- 

Approach: 
- Create an array of 26 intizlied to 0 
- loop throuhg all strings 
- take one string and find its count 
- check if that key exisits in the array if true Append string to value. 
- insert that array as the key and string as value 


"""