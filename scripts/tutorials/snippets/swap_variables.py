# Program to swap numbers *WITH* a temporary 3rd variable

class SwapNos:
    def __init__(self, x: int = 0, y: int = 1) -> None:
        self.x = x
        self.y = y
    
    def swap_third_temp(self) -> None:
        print(f"before: x={self.x}, y={self.y}")
        tmp = self.x
        self.x = self.y
        self.y = tmp
        print(f"after: x={self.x}, y={self.y}")
        self.reset()
        
    def reset(self) -> None:
        print("[x] resetting...")
        self.x = 0
        self.y = 1
        
    def swap_no_third_variable(self) -> None:
        print(f"before: x={self.x}, y={self.y}")
        self.x = self.x + self.y
        self.y = self.x - self.y
        self.x = self.x - self.y
        print(f"after: x={self.x}, y={self.y}")
        self.reset()
