class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.is_end = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        return self.dfs(curr, 0, word)
        
    def dfs(self, node, i, word):
        if i == len(word):
            return node.is_end
        
        if word[i] == '.':
            for child in node.children:
                if (self.dfs(node.children[child], i + 1, word)):
                    return True

        else:
            c = word[i]
            if c not in node.children:
                return False
            if self.dfs(node.children[c], i + 1, word):
                return True

        return False