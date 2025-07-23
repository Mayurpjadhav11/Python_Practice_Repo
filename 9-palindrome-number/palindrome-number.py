class Solution(object):
    def isPalindrome(self, x):
        r_x = str(x)[::-1]
        if r_x ==str(x):
            return True
        else:
            return False
        
sol = Solution()
sol.isPalindrome(121)        