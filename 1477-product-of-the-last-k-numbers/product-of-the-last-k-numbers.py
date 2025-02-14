class ProductOfNumbers:

    def __init__(self):
        self.prefix_product = [1]
        self.size = 0
    def add(self, num: int) -> None:
        if num == 0:
            # If num is 0, reset the cumulative products since multiplication
            # with 0 invalidates previous products
            self.prefix_product = [1]
            self.size = 0
        else:
            # Append the cumulative product of the current number with the last
            # product
            self.prefix_product.append(self.prefix_product[self.size] * num)
            self.size += 1
    def getProduct(self, k: int) -> int:
        # Check if the requested product length exceeds the size of the valid
        # product list
        if k > self.size:
            return 0
        # Compute the product of the last k elements using division
        return (
            self.prefix_product[self.size] // self.prefix_product[self.size - k]
        )
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)