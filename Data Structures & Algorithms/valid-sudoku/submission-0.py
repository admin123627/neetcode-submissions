class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = {}
        columns_map = {}
        box_map = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                square_num = (i // 3, j // 3)
                if num != '.':
                    if i not in row_map:
                        row_map[i] = set()
                        row_map[i].add(num)
                    else:
                        if num in row_map[i]:
                            return False
                        row_map[i].add(num)
                    if j not in columns_map:
                        columns_map[j] = set()
                        columns_map[j].add(num)
                    else:
                        if num in columns_map[j]:
                            return False
                        columns_map[j].add(num)
                    if square_num not in box_map:
                        box_map[square_num] = set()
                        box_map[square_num].add(num)
                    else:
                        if num in box_map[square_num]:
                            return False
                        box_map[square_num].add(num)
        return True


        