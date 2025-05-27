class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        x,y=1,1
        if dividend<0:
            x=-1
            dividend=abs(dividend)
        if divisor<0:
            y=-1
            divisor=abs(divisor)
        sign=x*y
        q=dividend//divisor
        max_value=2**31-1
        min_value=-2**31
        return max(min_value, min(max_value,sign*q))