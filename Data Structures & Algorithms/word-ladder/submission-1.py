from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        min_steps = 1
        q = deque([beginWord])

        while q:
            q_len = len(q)

            for _ in range(q_len):
                word = q.popleft()
                
                for i in range(len(word)):
                    for n in range(26):
                        letter = chr(ord('a') + n)
                        new_word = word[ :i] + letter + word[i + 1: ]

                        if new_word == endWord:
                            return min_steps + 1
                        
                        if new_word in words:
                            q.append(new_word)
                            words.remove(new_word)

            min_steps += 1
        
        return 0