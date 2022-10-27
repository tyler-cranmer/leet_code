import math
import numpy as np

# https://leetcode.com/discuss/interview-question/2732206/Amazon-OA

def max_gray(arr):
    row = []
    col = np.zeros((len(arr[0]), 2))
    max_gray = -math.inf
    for r in range(len(arr)):
        b=0
        w=0
        for c in range(len(arr[r])):
            if arr[r][c] == '1':
                col[c][0] += 1
                b+=1
            elif arr[r][c] == '0':
                col[c][1] += 1
                w+=1
        row.append([b,w])
    for i in range(len(row)):
        for j in range(len(col)):
            curr_gray = (row[i][0] + col[j][0] ) - (row[i][1] + col[j][1])
            max_gray = max(curr_gray, max_gray)
    return int(max_gray)


if __name__ == '__main__':
    a = ["101", "001", "110"]
    b = ["1010", "0101", "1010"]
    c = ["001","101","001"]
    print(max_gray(a))
    print(max_gray(b))
    print(max_gray(c))