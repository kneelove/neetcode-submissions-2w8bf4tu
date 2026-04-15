from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        max_freq=-1
        freq_map=Counter(sorted(nums))
        result=[]
        
        while k>0:
            max_key = max(freq_map, key=freq_map.get)
            result.append(max_key)
            freq_map.pop(max_key)
            k-=1
    


                    


            
        return result
            

        