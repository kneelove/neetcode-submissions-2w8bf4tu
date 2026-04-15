from collections import Counter
class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=[]
        used=set()
        for i in range(0,len(strs)):
            if strs[i] in used:
                continue
            temp=[strs[i]]
            used.add(strs[i])

            
            for j in range(i+1,len(strs)):
                if Counter(strs[i])==Counter(strs[j]):
                    temp.append(strs[j])
                    used.add(strs[j])

            result.append(temp)
            
        return result
            

        