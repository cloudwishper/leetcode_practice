class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :param nums: an integer array.
        :param k: an interger defines the top k 
        :return: k most frequent elements in nums
        """
        # use dict to count the frequency of each num
        num_to_frequency_map = {}
        for num in nums:
            num_to_frequency_map[num] = num_to_frequency_map.get(num, 0) + 1

        # heapq is min heap, so we save negative frequency in the tuple of the list.
        num_to_frequency = [(-num_to_frequency_map[k], k) for k in num_to_frequency_map]
        heapq.heapify(num_to_frequency)
        res = []

        for i in range(k):
            frequency, num = heapq.heappop(num_to_frequency)
            res.append(num)

        return res 
