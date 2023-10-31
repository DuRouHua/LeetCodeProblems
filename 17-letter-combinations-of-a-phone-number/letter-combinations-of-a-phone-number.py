class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        d = [" ", "","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        ans = [""]

        for digit in digits:
            tmp = []
            for s in ans:
                for c in d[ord(digit)-ord('0')]:
                    tmp.append(s+c)
            ans = tmp

        return ans
        