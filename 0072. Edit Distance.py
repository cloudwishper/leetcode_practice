class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        :param word1: first string.
        :param word2: second string.
        :return:  the minimum number of operations required to convert word1 to word2.
        """
    
        m = len(word1)
        n = len(word2)
        if not word1 or not word2:
            return max(len(word1), len(word2))
        dps = [[0 for i in range(n + 1)] for j in range(m + 1)]

        for i in range(n + 1):
            dps[0][i] = i
        
        for j in range(m + 1):
            dps[j][0] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dps[i][j] = dps[i - 1][j - 1]
                else:
                    dps[i][j] = min(dps[i - 1][j - 1], dps[i - 1][j], dps[i][j - 1]) + 1

        return dps[-1][-1]
