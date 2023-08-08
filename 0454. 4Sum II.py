class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        :param nums1: the first integer arrays.
        :param nums2: the second inter arrays.
        :param nums3: the third inter arrays.
        :param nums4: the fourth inter arrays.
        :return: number of tuples (i, j, k, l) that satisify
                 nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0.
        """

        two_sum_to_freq1 = {}
        two_sum_to_freq2 = {}

        for num1 in nums1:
            for num2 in nums2:
                two_sum_to_freq1[num1 + num2] = two_sum_to_freq1.get(num1 + num2, 0) + 1

        for num3 in nums3:
            for num4 in nums4:
                two_sum_to_freq2[num3 + num4] = two_sum_to_freq2.get(num3 + num4, 0) + 1

        res = 0
        for x in two_sum_to_freq1:
            # frequency of 2sum x multipy frequency of 2sum y, where x + y = 0.
            # x is sum of two nums from nums1 and nums2,  y is sum of two nums from nums3 and nums4.
            res += two_sum_to_freq1[x] * two_sum_to_freq2.get(-x, 0)

        return res 
