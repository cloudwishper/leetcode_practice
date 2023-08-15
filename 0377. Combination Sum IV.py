class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        :param nums: an array of distinct integers.
        :param target:  a target integer.
        :return:  the number of possible combinations that add up to target.
        """
        nums.sort()
        memo = {}

        def backtrack(nums, target_remain):
            if target_remain == 0:
                return 1
            if target_remain in memo:
                return memo[target_remain]
            
            res = 0
            for num in nums:
                if num <= target_remain:
                    res += backtrack(nums, target_remain - num)
            # we save the res for this target_remain in memo to prevent backtrack again.
            memo[target_remain] = res
            return res 
        
        return backtrack(nums, target)
