class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)


#Using Memoization
class Solution(object):
    def __init__(self):
        self.memo={}
    def fib(self, n):
        if n<=1:
            return n
        if n not in self.memo:
            self.memo[n] = self.fib(n-1)+self.fib(n-2)
        return self.memo[n]
      
sol = Solution()
print(sol.fib(4))
