class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        :param nums: an integer array.
        :return: all unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
                 nums[a] + nums[b] + nums[c] + nums[d] == target.
        """
        nums.sort()
        res = []

        for i in range(len(nums) - 3):
            # choose num1 as first pivot number.
            num1 = nums[i]
            # if same num has been choosen as first pivot number, skip it to prevent duplicate tuple result.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                # choose num2 as first pivot number.
                num2 = nums[j]
                # if same num has been choosen as second pivot number, skip it to prevent duplicate tuple result.
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # use two pointers to find two nums that sum of them equals target - num1 - num2.
                left, right = j + 1, len(nums) - 1
                while left < right:
                    # if same left num has been seen, skip it to prevent duplicate tuple result.
                    if left > j + 1 and nums[left] == nums[left - 1]:
                        left += 1
                        continue
                    if nums[left] + nums[right] == target - num1 - num2:
                        res.append([num1, num2, nums[left], nums[right]])
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] > target - num1 - num2:
                        right -= 1
                    else:
                        left += 1

        return res 
