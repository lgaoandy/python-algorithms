class StockSpanner:
    def __init__(self):
        self.prices = []
        self.span = []


    def next(self, price: int) -> int:
        span = self.span.copy()
        i = len(span) - 1
        cur = 1

        while i >= 0 and self.prices[i] <= price:
            cur += span[i]
            i -= span[i]

        self.prices.append(price)
        self.span.append(cur)

        return cur
    

class StockSpannerOptimized:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price, 1))
            return 1

        count = 1
        while self.stack and self.stack[-1][0] <= price:
            count += self.stack[-1][1]
            self.stack.pop()
        
        self.stack.append((price, count))
        return count


if __name__ == "__main__":
    s = StockSpannerOptimized()
    print(s.next(100))
    print(s.next(80))
    print(s.next(60))
    print(s.next(70))
    print(s.next(60))
    print(s.next(75))
    print(s.next(85))