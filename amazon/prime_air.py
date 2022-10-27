'''
Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id and the second integer represents a value. 
Your task is to find an element from a and an element form b such that the sum of their values is less or equal to target and as close to target as possible. 
Return a list of ids of selected elements. If no pair is possible, return an empty list.

Input:
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

Output: [[2, 1]]

Explanation:
There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.

Input:
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10

Output: [[2, 4], [3, 2]]

Explanation:
There are two pairs possible. Element with id = 2 from the list `a` has a value 5, and element with id = 4 from the list `b` also has a value 5.
Combined, they add up to 10. Similarily, element with id = 3 from `a` has a value 7, and element with id = 2 from `b` has a value 3.
These also add up to 10. Therefore, the optimal pairs are [2, 4] and [3, 2].

Input:
a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20

Output: [[3, 1]]

Input:
a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20

Output: [[1, 3], [3, 2]]
'''
import math
def OptimalUtilization(l1, l2, target):
    N = len(l1) 
    M = len(l2) 
    l1.sort(key = lambda x: x[1])
    l2.sort(reverse=True, key = lambda x: x[1])
    top,bottom = 0,0
    result = []
    min_distance = math.inf
    while top < N and bottom < M:
        sum_value = l1[top][1] + l2[bottom][1]
        if sum_value > target:
            bottom += 1
        else:
            curr_distance = target - sum_value
            if curr_distance == min_distance:
                result.append([l1[top][0], l2[bottom][0]])
                min_distance = curr_distance
                bottom += 1
                top +=1
            elif curr_distance < min_distance:
                result.clear()
                result.append([l1[top][0], l2[bottom][0]])
                min_distance = curr_distance
                top +=1
    return result

if __name__ =='__main__':
    a1 = [[1, 2], [2, 4], [3, 6]]
    b1 = [[1, 2]]
    target1 = 7

    print(OptimalUtilization(a1,b1, target1))

    a2 = [[1, 3], [2, 5], [3, 7], [4, 10]]
    b2 = [[1, 2], [2, 3], [3, 4], [4, 5]]
    target2 = 10

    print(OptimalUtilization(a2,b2, target2))
    
    a3 = [[1, 8], [2, 7], [3, 14]]
    b3 = [[1, 5], [2, 10], [3, 14]]
    target3 = 20
    print(OptimalUtilization(a3,b3, target3))
    
    a4 = [[1, 8], [2, 15], [3, 9]]
    b4 = [[1, 8], [2, 11], [3, 12]]
    target4 = 20
    print(OptimalUtilization(a4,b4, target4))