class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        :param nums: an integers array.
        :param k: the sliding window size.
        :return: max num of each step sliding window moving left to right in nums
        """
        res = []
        right = 0
        queue = collections.deque()

        for i in range(len(nums) - k + 1):
            # queue is monotoic decreasing
            while right < i + k:
                while queue and queue[-1][1] < nums[right]:
                    queue.pop()
                queue.append((right, nums[right]))
                right += 1
            # i is left boundary of the window
            if queue[0][0] < i:
                queue.popleft()
            res.append(queue[0][1])

        return res 
