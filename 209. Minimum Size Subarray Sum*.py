class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        :param target: a postive num 
        :param target: an array of positive integers
        :return: the minimal lenghth of a subarray whose sum is greater 
                 than or equal to target. Return 0 if there is no such subarray.
        """
        res = len(nums) + 1
        #use two pointer method to solve this quesion
        left, right = 0, 0
        sum_ = 0

        while right <= len(nums):
            if sum_ < target:
                if right == len(nums):
                    break
                sum_ += nums[right]
                right += 1  
            else:
                res = min(res, right - left)
                sum_ -= nums[left]
                left += 1

        return 0 if res == len(nums) + 1 else res
        
