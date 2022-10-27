''' 
https://leetcode.com/problems/container-with-most-water/submissions/ MEDIUM

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

'''
import math
def maxArea_brute_force(height):
    left = 0
    N = len(height)
    max_area = -math.inf

    for left in range(N):
        for right in range(left+1, N):
            w = min(height[left], height[right])
            l = right - left
            current_area = l * w
            max_area = max(current_area, max_area)
    return max_area

def maxArea(height):
    N = len(height) 
    left = 0
    right = N - 1
    max_area = -math.inf
    while left < right:
        w = min(height[left], height[right])
        l = right - left
        current_area = l * w
        max_area = max(current_area, max_area)
        if height[left] > height[right]:
            right -=1
        else:
            left += 1
    return max_area


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))
