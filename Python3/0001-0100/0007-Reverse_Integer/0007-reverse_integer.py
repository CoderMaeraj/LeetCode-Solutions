class Solution:
    def reverse(self, x: int) -> int:
        is_neg = False
        upper = (2**31)-1
        lower = -(2**31)
        if x<0:
            is_neg =True
        x = str(abs(x))
        new_x = x[::-1]
        new_x = int(new_x)
        if is_neg:
            new_x = -1*new_x
        if ((new_x > upper) or (new_x < lower)):
            return 0
        return new_x