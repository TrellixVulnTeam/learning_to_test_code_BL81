from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = -1
        for l in range(len(height)):
            for r in range(l+1, len(height)):
                minBar = min(height[l], height[r])
                width = r - l
                area = width * minBar
                maxArea = max(maxArea, area)
                print(f'area: {area} maxArea: {maxArea}')
            print("-")
        return maxArea


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    solution.maxArea(height)
    
    
    