class Solution:
    def trap(self, height: List[int]) -> int:
        maxVal = max(height)
        maxIndex = height.index(maxVal)

        def water(arr):
            curr = 0
            trapped_water = 0
            for i in arr:
                if i >= curr:
                    curr = i
                else:
                    trapped_water += curr - i
                    curr = max(curr, i)
            return trapped_water

        return water(height[maxIndex:len(height)][::-1]) + water(height[0:maxIndex])