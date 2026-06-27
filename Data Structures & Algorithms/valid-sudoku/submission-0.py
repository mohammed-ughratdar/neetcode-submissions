class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for x in range(0, len(board)):
            sudoku_map_horizontal = {}
            sudoku_map_verticle = {}
            for y in range(0, len(board[0])):
                if board[x][y] != '.' and sudoku_map_horizontal.get(board[x][y]):
                    return False
                if board[y][x] != '.' and sudoku_map_verticle.get(board[y][x]):
                    return False

                if board[x][y] != '.':
                    sudoku_map_horizontal[board[x][y]] = True
                if board[y][x] != '.':
                    sudoku_map_verticle[board[y][x]] = True

        sub_boxes = {}
        for x in range(0, len(board)):
            for y in range(0, len(board[0])):
                if board[x][y] != '.':
                    if board[x][y] in sub_boxes.get((x//3,y//3), ()):
                        return False
                    indices_list = sub_boxes.get((x//3,y//3), [])
                    indices_list.append(board[x][y])
                    sub_boxes[(x//3,y//3)] = indices_list

        return True

            
                