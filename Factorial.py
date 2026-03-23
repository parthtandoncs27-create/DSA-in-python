class Solution:
    def factorial(self, n: int) -> int:
        self.n = n
        if self.n == 0 or self.n == 1:
            return 1
        return self.n * self.factorial(n-1)
