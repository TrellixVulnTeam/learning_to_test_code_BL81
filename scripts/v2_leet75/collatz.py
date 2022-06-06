# just practice from "autOmate the boring stuff: collataz sequence. ch3."
# 6-5-22 KZ


# standalone function
# def collatz(n):
#     if n == 1:
#         print(f"COLLATZ == {n}")
#         return n
#     else:
#         guess = int(input("enter number: "))
#         print(f"current: {guess}")

#         if guess % 2 == 0:
#             print("value (even)")
#             operation = guess // 2
#             return collatz(operation)
#         else:
#             print("value (odd)")
#             operation = 3 * guess + 1
#             return collatz(operation)

# as class
class Collatz:
    def __init__(self, number: int, current: int=0) -> str:
        self.number = number
        self.current = current

        print(f"[INFO] starting with {self.current}")
        self.run()

    @property
    def current(self):
        """
        must use underscore or get recursion error
        """
        return self._current
    
    @current.setter
    def current(self, value):
        """
        must use underscore or get recursion error
        """
        self._current = value
        
    def run(self):  # sourcery skip: assign-if-exp, hoist-statement-from-if
        print(f"[INFO] current: {self.current}")

        if self.current == 1:
            print(f"[INFO] number equals {self.current}")
            # return self.current
            return 1
        else:
            new_value = int(input("new number: "))
            if new_value % 2 == 0:
                operation = new_value // 2
                self.current = operation
                return self.run()
            else:
                operation = new_value * 3 + 1
                self.current = operation
                return self.run()
    
    def __str__(self):
        return str(self.current)

if __name__ == '__main__':
    # print(collatz(7))
    print(Collatz(7))
    # collatz = Collatz(7)
    # print(collatz.run())