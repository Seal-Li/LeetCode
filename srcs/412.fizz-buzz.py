#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def div3(self, n):
        if n % 3 == 0:
            return True
        else:
            return False

    def div5(self, n):
        if n % 5 == 0:
            return True
        else:
            return False

    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            if self.div3(i) and self.div5(i):
                result.append("FizzBuzz")
            elif self.div3(i):
                result.append("Fizz")
            elif self.div5(i):
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
# @lc code=end

