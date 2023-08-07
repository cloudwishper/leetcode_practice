class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        :param n: a positive integer.
        :return: a n x n matrix filled with elements from 1 to n**2 in spiral order.
        """

        left = 0
        right = n - 1
        up = 0
        bottom = n - 1
        num = 1
        res = [[0 for i in range(n)] for j in range(n)]

        # fill the matrix in spiral order which means in the loop: 
        # left to right, up to bottom, right to left, bottom to up.
        while num <= n**2:
            for i in range(left, right + 1):
                res[up][i] = num
                num += 1
            up += 1

            for i in range(up, bottom + 1):
                res[i][right] = num
                num += 1
            right -= 1

            for i in range(right, left - 1, -1):
                res[bottom][i] = num
                num += 1
            bottom -= 1

            for i in range(bottom, up - 1, -1):
                res[i][left] = num
                num += 1
            left += 1

        return res 
