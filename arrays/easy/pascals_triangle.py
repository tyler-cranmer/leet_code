''' 
118. Pascal's Triangle EASY

https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30

'''

def generate(numRows: int):
    
    triangle = [[1]]
    for r in range(1,numRows):
        prev_row = [0] + triangle[-1] + [0]
        next_row = []
        for c in range(len(prev_row)-1):
            next_row.append(prev_row[c] + prev_row[c+1])
        triangle.append(next_row)
    return triangle

'''
time: O(n^2), n = num of rows
space: O(1)
'''


if __name__ == '__main__':
    print(generate(5))
    print(generate(1))
    print(generate(4))