class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        all_letters = [
            "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz", ""
        ]
        res = []
        if not digits:
            return res
        curr = []

        def backtrack(digits, i):
            if i == len(digits):
                res.append("".join(curr))
                # res.append("".join(ch) for ch in curr)
                return
            
            index = int(digits[i])
            letter = all_letters[index]

            for ch in letter:
                curr.append(ch)
                backtrack(digits, i+1)
                curr.pop()

        backtrack(digits, 0)
        return res
        