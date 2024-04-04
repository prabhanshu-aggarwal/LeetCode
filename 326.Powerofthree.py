/* 326. Power of Three
Solved
Easy
Topics
Companies
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1). */


#using simple method.
class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0:
            return False
        if n==1:
            return True
        while n%3==0:
            n = n/3
            if n==1:
                return True
        return False



#using Math
import math

class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        # Calculate the logarithm of n with base 3 and check if it is an integer.
        log_val = math.log10(n) / math.log10(3)
        return log_val.is_integer()


#usin recursion

class Solution(object):
    def isPowerOfThree(self, n):
        if n < 1:
            return False
        if n == 1:
            return True
        if n % 3 == 0:
            return self.isPowerOfThree(n / 3)
        return False 
