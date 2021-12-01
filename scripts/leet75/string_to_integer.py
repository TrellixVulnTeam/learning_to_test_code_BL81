from typing import Dict, List


class Solution:
    
    
    def clip(self, val):
        min_ = -1*(2**31)
        max_ =  2**31 - 1
        return min_ if val < min_ else max_ if val > max_ else val
    
    def myAtoi(self, s: str) -> int:
        # remove whitespace
        s = s.strip()
        start = s[0]
        if "." in s:
            index = s.find(".")
            s = s[:index]
        print(s)
        if start.isalpha():
            return 0
        else:
            if start == "-":
                value =  "-" + "".join([i for i in s[1:] if i.isdigit()])
                return self.clip(int(value))
            elif start == "+":
                value = "".join([i for i in s[1:] if i.isdigit()])
                return self.clip(int(value))
            else:
                value = "".join([i for i in s if i.isdigit()])
                print(value)
                return self.clip(int(value))
        
        
if __name__ == "__main__":
    s = "   +32"
    s = " 3.14159"
    s = ".1"
    solution = Solution()
    print(solution.myAtoi(s))