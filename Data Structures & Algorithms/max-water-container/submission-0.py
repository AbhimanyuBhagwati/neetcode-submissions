class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        for left_index in range(len(heights)):
            for right_index in range(left_index + 1, len(heights)):
                left_height = heights[left_index]
                right_heigth = heights[right_index]


                cnt_height =min(left_height, right_heigth)

                cnt_wdth = right_index - left_index

                water_hold = cnt_height * cnt_wdth

                if water_hold > max_water:
                    max_water = water_hold
        
        return max_water