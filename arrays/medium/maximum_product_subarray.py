'''
152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

'''

def maxProduct(nums: list) -> int:
    curMin, curMax = 1, 1
    result = max(nums)

    for n in nums:
        tmp_curMax =  n * curMax #needed for curMin because we changed curMax before using it for curMin
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp_curMax, n * curMin, n)
        result = max(result, curMax)
    return result
'''
time: O(n)
space: O(1)
'''

if __name__ == '__main__':
    nums = [-2,3,-4]
    print(maxProduct(nums))