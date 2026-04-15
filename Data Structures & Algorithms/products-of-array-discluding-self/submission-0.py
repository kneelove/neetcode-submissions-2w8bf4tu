class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        result=[]
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i==j:
                    continue
                product*=nums[j]
            result.append(product)
            product=1
        return result

        