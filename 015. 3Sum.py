class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        :param nums: an integer array.
        :return: all unqiue the triplets [nums[i], nums[j], nums[k]] such that 
                 i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 1):
            # choose a num as pivot number.
            num = nums[i]

            # if same num has been choosen as pivot number, skip it to prevent duplicate tuple result.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # use two pointers to find two nums that sum of them equals 0 - pivot num.
            left, right = i + 1, len(nums) - 1
            while left < right:
                # if same left num has been seen, skip it to prevent duplicate tuple result.
                if left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                if nums[left] + nums[right] == -num:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > -num:
                    right -= 1
                else:
                    left += 1

        return res
