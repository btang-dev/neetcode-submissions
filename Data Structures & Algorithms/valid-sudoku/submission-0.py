class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        subbox = defaultdict(set) # key = (r / 3, c / 3) <--- this tells the current subbox we are in

        for r in range(9):
            for c in range(9):
                # empty position is represented by a dot. if it's empty, then skip it and continue
                if board[r][c] == ".":
                    continue
                # check for duplicates
                if (board[r][c] in rows[r]
                 or board[r][c] in cols[c]
                 or board[r][c] in subbox[(r // 3, c // 3)]):
                    return False
                
                # add the value that has not been added before in the row, col, and subbox
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                subbox[r // 3, c // 3].add(board[r][c])
        
        return True