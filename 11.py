class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start_cursor = 0
        end_cursor = len(height) - 1
        area = 0
        while True:
            vertical = min(height[start_cursor], height[end_cursor])
            area = max(area, vertical * (end_cursor - start_cursor))
            if abs(start_cursor - end_cursor) == 0:
                return area
            if height[start_cursor] < height[end_cursor]:
                start_cursor += 1
            else:
                end_cursor -= 1
