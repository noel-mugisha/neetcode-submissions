class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        set_ = set(wordList)
        if endWord not in set_:
            return 0

        q = deque([beginWord])
        times = 1
        while q:
            size = len(q)

            for _ in range(size):
                word = q.popleft()
                for i in range(len(word)):
                    for j in range(26):
                        c = chr(ord("a") + j)
                        if c == word[i]:
                            continue
                        new_word = word[:i] + c + word[i + 1:]

                        if new_word == endWord:
                            return times + 1
                        
                        if new_word in set_:
                            q.append(new_word)
                            set_.remove(new_word)

            times += 1

        return 0
