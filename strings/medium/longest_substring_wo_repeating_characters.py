'''
3. Longest Substring Without Repeating Characters MEDIUM

https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''
from collections import Counter
def lengthOfLongestSubstring(s: str):
    charSet = set()
    left = 0
    result = 0
    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        result = max(result, right - left + 1)
    return result
'''
time: O(n)
space: O(n)
'''
if __name__ == "__main__": 
    s = "abcbacbb"
    # s = "bbbbb"
    # s = " "
    print(lengthOfLongestSubstring(s))
