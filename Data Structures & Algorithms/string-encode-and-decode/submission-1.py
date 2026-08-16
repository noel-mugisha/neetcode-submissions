class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            len_ = str(len(s))
            word = len_ + "#" + s
            res.append(word)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            num = []
            
            while s[i] != '#':
                num.append(s[i])
                i += 1
            
            len_ = int("".join(num))

            res.append("".join(s[i+1 : i+1+len_]))

            i += len_ + 1

        return res

