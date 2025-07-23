class Solution(object):
    def plusOne(self, digits):
        #digits[-1]=digits[-1]+1
        #if digits[-1]>9:
        num = int(''.join(str(d) for d in digits))
        num += 1
        digits = [int(d) for d in str(num)]
        return digits

sol = Solution()
sol.plusOne([1,2,3])
        