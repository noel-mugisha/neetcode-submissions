class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_end = True
            curr.word = word

        ROWS, COLS = len(board), len(board[0])
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0)
        ]
        res = []

        def dfs(node, r, c):
            if node.is_end:
                res.append(node.word)
                node.is_end = False
                
            if not(0 <= r < ROWS and 0 <= c < COLS):
                return
            if board[r][c] == '#' or board[r][c] not in node.children:
                return

            ch = board[r][c]
            board[r][c] = '#'

            node = node.children[ch]

            for dr, dc in directions:
                dfs(node, r + dr, c + dc)

            board[r][c] = ch
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(root, r, c)

        return res