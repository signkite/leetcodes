class MyStack:

    def __init__(self):
        self.values = []

    def push(self, x: int) -> None:
        self.values.append(x)
        
    def pop(self) -> int:
        if self.values:
            return self.values.pop()
        else:
            return None

    def top(self) -> int:
        if self.values:
            return self.values[-1]
        else:
            return None

    def empty(self) -> bool:
        if self.values:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()