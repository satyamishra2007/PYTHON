class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            i = 0
            j = len(s) - 1
            while (i < j):
                if s[i] == s[j]:
                    i = i + 1
                    j = j - 1
                    continue
                else:
                    p = s[:j] + s[j + 1:]
                    q = s[:i] + s[i + 1:]
                    break
            if p == p[::-1] or q == q[::-1]:
                return True
            else:
                return False


s = "abca"
print("validPalindrome_II : ", Solution().validPalindrome(s))