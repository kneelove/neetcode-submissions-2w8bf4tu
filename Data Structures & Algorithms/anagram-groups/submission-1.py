from collections import Counter
class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary={}
        for i in range(0,len(strs)):
            key="".join(sorted(strs[i]))
            if key not in dictionary:
                dictionary[key]=[]
            dictionary[key].append(strs[i])
        return list(dictionary.values())



            
            

            

        