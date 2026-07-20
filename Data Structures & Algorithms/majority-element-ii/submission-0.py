class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        mp = {}

        for i in nums:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        
        # iterate through map 

        result = []

        for num , count in mp.items():
                if count > n // 3:
                    result.append(num)
        return result