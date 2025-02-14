class ProductOfNumbers:
    def __init__(self):
        self.stream = []
        
    
    def add(self, num: int) -> None:
        for i in range(len(self.stream)):
            self.stream[i] *= num
        self.stream.append(num)
    
    
    def getProduct(self, k: int) -> int:
        n = len(self.stream)
        return self.stream[n-k]
    
    
if __name__ == "__main__":
    p = ProductOfNumbers()
    print(p.add(3))
    print(p.add(0))
    print(p.add(2))
    print(p.add(5))
    print(p.add(4))
    print(p.getProduct(2))
    print(p.getProduct(3))
    print(p.getProduct(4))
    print(p.add(8))
    print(p.getProduct(2))
    