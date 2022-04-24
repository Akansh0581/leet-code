# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

import math

class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5=math.sqrt(5)
        return int((((1+sqrt5)/2)**(n+1) - ((1-sqrt5)/2)**(n+1))/sqrt5)
     