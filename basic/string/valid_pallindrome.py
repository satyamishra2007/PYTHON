def isPalindrome(s: str):
        res = ''
        for i in s:
            if i.isalnum():
                res += i.lower()
            else:
                continue
        if not res:
            return True
        return res == res[::-1]



# Optimised T: O(N)  and S(1)
def isPalindromeOpt(s):
    l, r = 0, len(s) - 1
    while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
    return True

s = "A man, a plan, a canal: Panama"
print("isPalindrome:" , isPalindrome(s))

print("isPalindromeOpt: ",isPalindromeOpt(s))