# TODO: My solution for leetcode submission is running very slow, 
# 3000ms which beats 5.00% of users with Python3.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def get_attack_points(i: int, j: int) -> Set[Tuple[int]]:
            attack_points = set()
            for k in range(n):
                attack_points.add((k, j))
                attack_points.add((i, k))
            p, q = i, j
            while p >= 0 and q >= 0 and p < n and q < n:
                attack_points.add((p, q))
                p += 1
                q += 1
            p, q = i, j
            while p >= 0 and q >= 0 and p < n and q < n:
                attack_points.add((p, q))
                p += 1
                q -= 1
            p, q = i, j
            while p >= 0 and q >= 0 and p < n and q < n:
                attack_points.add((p, q))
                p -= 1
                q += 1
            p, q = i, j
            while p >= 0 and q >= 0 and p < n and q < n:
                attack_points.add((p, q))
                p -= 1
                q -= 1
            return attack_points

        point_to_attackpoints = {}
        for i in range(n):
            for j in range(n):
                point_to_attackpoints[(i, j)] = get_attack_points(i, j)

        res_locations = []
        def backtrack(index, attacked_points, remain_queens, assigned_points):
            if remain_queens == 0:
                res_locations.append(assigned_points)
                return 
            if len(attacked_points) == n ** 2:
                return
                
            for m in range(index, n ** 2):
                row = m // n
                col = m % n
                if (row, col) not in assigned_points and (row, col) not in attacked_points:
                    attack_points = point_to_attackpoints[(row, col)]
                    new_attacked_points = attacked_points.union(attack_points)
                    backtrack((row + 1) * n, new_attacked_points, remain_queens - 1, assigned_points + [(row, col)])

        backtrack(0, set(), n, [])
        def location_to_strboard(location):
            print(location)
            board = ['.' * n for i in range(n)]
            for i, j in location:
                board[i] = board[i][:j] + 'Q' + board[i][j + 1:]
            return board

        res = []
        for location in res_locations:
            res.append(location_to_strboard(location))
        return res 
