'''

https://leetcode.com/problems/valid-parentheses/ EASY
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

'''
from collections import deque

def isValid(s: str) -> bool:
    stack = []
    dic = {'(':')', '{':'}','[':']'}

    for ch in s:
        if ch in dic:
            stack.append(ch)
        elif len(stack) == 0 or dic[stack.pop()] != ch:
            return False
    return len(stack) == 0
# 1. if it's the left bracket then we append it to the stack
# 2. else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
# 3. finally check if the stack still contains unmatched left bracket

if __name__ == '__main__':
    s = '()[]{}'
    s2 = "(]"
    s3= '[{}]{{)'
    s4=']'
    print(isValid(s))
    print(isValid(s2))
    print(isValid(s3))
    print(isValid(s4))

