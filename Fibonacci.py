class Solution:
    def fib(self, n: int) -> int:
        self.n = n
        if self.n <=1:
            return self.n
        return self.fib(n-1) + self.fib(n-2)
