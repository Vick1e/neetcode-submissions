class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        path = []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def dfs(i):

            if not digits: 
                return []
            if i == len(digits):
                res.append("".join(path))
                return 

            letter = phone[digits[i]]

            for char in letter:
                path.append(char)
                dfs(i+1)
                path.pop()

        
        dfs(0)
        return res



