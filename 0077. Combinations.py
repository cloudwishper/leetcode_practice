class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        :param n: an integer define the nums range is [1  n].
        :param k: an integer that means seleck k numbers from nums with range [1, n].
        :return: return all possible combinations of k numbers chosen from the range [1, n].
        """
        def backtrack(nums: List[int], combination: List[int], 
                      res: List[List[int]]) -> None:
            if len(combination) == k:
                res.append(combination)
                return
            for i in range(len(nums)):
            # make sure remain nums' len is larger than remain k, 
            # next line comment code make it slightly faster.
            # for i in range(len(nums) - (k - len(combination)) + 1):
                backtrack(nums[i + 1:], combination + [nums[i]], res)
        res = []
        nums = range(1, n + 1)
        backtrack(nums, [], res)
        return res 
