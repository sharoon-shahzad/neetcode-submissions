class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hashmap
        seen ={}
        # traverse array
        for i in range(len(nums)):
            more = target - nums[i]
            # check if number exist in Hashmap
            # if yes retrieve it otherwise insert in hashmap
            if more in seen:
                return [seen[more] , i]
            seen[nums[i]] = i
            
        return[]
