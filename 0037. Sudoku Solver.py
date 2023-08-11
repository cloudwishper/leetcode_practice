class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        :param board: a 2D list represent a  Sudoku puzzle
        :return: None
        Do not return anything, modify board in-place instead.
        """
        # for each row, col, and 3 x 3 subbox, remember already exist numbers
        find_solution = False
        row_num_set = [set() for i in range(9)]
        col_num_set = [set() for i in range(9)]
        subbox_set =  [[set(), set(), set()] for i in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row_num_set[i].add(board[i][j])
                    col_num_set[j].add(board[i][j])
                    subbox_set[i//3][j//3].add(board[i][j])

        def backtrack(board):
            nonlocal find_solution
            if find_solution:
                return
            count = 0
            possible_nums_location = []
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        count += 1
                        possible_nums = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
                        # find all exist nums from this row, col and located subbox
                        exist_nums = row_num_set[i].union(col_num_set[j]).union(subbox_set[i//3][j//3])
                        possible_nums = possible_nums - exist_nums
                        # if can't find a num for '.', it is impossible to find a solution, just return.
                        if not possible_nums:
                            return
                        possible_nums_location.append([possible_nums, (i, j)])
            if count == 0:
                find_solution = True
                return
            # find a location with least number of possible numbers to assgin,
            # this operation can speed up to 60 ms from 120 ms in leetcode submission.
            possible_nums_location.sort(key = lambda x: len(x[0]))
            
            possible_nums = possible_nums_location[0][0]
            i, j = possible_nums_location[0][1]
            for num in possible_nums:
                board[i][j] = num
                row_num_set[i].add(board[i][j])
                col_num_set[j].add(board[i][j])
                subbox_set[i // 3][j // 3].add(board[i][j])
                backtrack(board)
                if find_solution:
                    break
                row_num_set[i].remove(board[i][j])
                col_num_set[j].remove(board[i][j])
                subbox_set[i // 3][j // 3].remove(board[i][j])
                board[i][j] = '.'

        backtrack(board)
