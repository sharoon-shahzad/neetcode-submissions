class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """

        low = 0
        
        mid = 0 

        high = len(nums)-1

        while mid <= high:

            if nums[mid] == 0:

                nums[low] , nums[mid] = nums[mid] , nums[low]

                low+=1

                mid+=1

            elif nums[mid] == 1:
                mid+=1
            
            elif nums[mid] == 2:
                nums[mid] , nums[high] = nums[high] , nums[mid]
                high-=1

        # if nums is None:
        #     raise ValueError("nums cannot be None")

        # count0 = count1 = count2 = 0

        # # PASS 1: Count frequencies, validate input explicitly
        # for num in nums:
        #     if num == 0:
        #         count0 += 1
        #     elif num == 1:
        #         count1 += 1
        #     elif num == 2:
        #         count2 += 1
        #     else:
        #         raise ValueError(f"Invalid value {num!r}: expected only 0, 1, or 2")

        # # PASS 2: Overwrite array in place
        # for i in range(count0):
        #     nums[i] = 0
        # for i in range(count0, count0 + count1):
        #     nums[i] = 1
        # for i in range(count0 + count1, len(nums)):
        #     nums[i] = 2