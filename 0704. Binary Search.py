class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        :param nums: an ascending sorted nums array
        :param target: a target num that try to search from nums
        :return: return index of target in nums if it exists, otherwise return -1
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1
