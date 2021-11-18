from typing import Dict, List

class Solution:
    
    def final_value_after_operations(self, operations: List[int]) -> int:
        # initialize multipliers dict
        multipliers = {
            "++X" : 1,
            "X++" : 1,
            "X--" : -1,
            "--X" : -1
        }
        
        # initialize "X" counter
        X = 0
        
        for operation in operations:
            X += multipliers[operation]
        
        return X