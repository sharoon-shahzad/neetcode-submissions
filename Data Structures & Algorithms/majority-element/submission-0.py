class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # getting the length of array/list

        n = len(nums)
        # hashmap to store the frequencies
        frequencyMap = {}

        for i in nums:
            # increase frquency if it exist in map
            # if not insert in map making count = 1
            # 
            if i in frequencyMap:
                frequencyMap[i]+=1
            else:
                frequencyMap[i] = 1

        # iterate through frequencyMap 
        for num , count in frequencyMap.items():
            if count > n // 2:
                return num

        return -1

        

            