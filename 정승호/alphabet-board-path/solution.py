class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst",
                 "uvwxy", "z"]
        position = {}
        for r in range(6):
            for c in range(len(board[r])):
                position[board[r][c]] = (r,c)
        
        answer = ''
        
        x,y = 0,0
        
        for ch in target:
            dx, dy = position[ch]
            ups = max(0, x - dx)
            rights = max(0, dy - y)
            lefts = max(0, y - dy)
            downs = max(0, dx - x)
            answer += 'U' * ups + 'L' * lefts + 'R' * rights + 'D' * downs + '!'
            x, y = dx, dy
            
        return answer
