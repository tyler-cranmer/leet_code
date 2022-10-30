"""
26. Remove Duplicate from orted Array - EAY 

http://leetcode.com/problem/remove-duplicate-from-orted-array/

Given an integer array num orted in non-decreaing order, remove the duplicate in-place uch that each unique element appear only once. The relative order of the element hould be kept the ame.

ince it i impoible to change the length of the array in ome language, you mut intead have the reult be placed in the firt part of the array num. More formally, if there are k element after removing the duplicate, then the firt k element of num hould hold the final reult. It doe not matter what you leave beyond the firt k element.

Return k after placing the final reult in the firt k lot of num.

Do not allocate extra pace for another array. You mut do thi by modifying the input array in-place with O(1) extra memory.

Cutom Judge:

The judge will tet your olution with the following code:

int[] num = [...]; // Input array
int[] expectedNum = [...]; // The expected anwer with correct length

int k = removeDuplicate(num); // Call your implementation

aert k == expectedNum.length;
for (int i = 0; i < k; i++) {
    aert num[i] == expectedNum[i];
}
If all aertion pa, then your olution will be accepted.

 

Example 1:

Input: num = [1,1,2]
Output: 2, num = [1,2,_]
Explanation: Your function hould return k = 2, with the firt two element of num being 1 and 2 repectively.
It doe not matter what you leave beyond the returned k (hence they are undercore).
Example 2:

Input: num = [0,0,1,1,1,2,2,3,3,4]
Output: 5, num = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function hould return k = 5, with the firt five element of num being 0, 1, 2, 3, and 4 repectively.
It doe not matter what you leave beyond the returned k (hence they are undercore).
 

Contraint:

1 <= num.length <= 3 * 104
-100 <= num[i] <= 100
num i orted in non-decreaing order.

"""

def removeDuplicate(nums):
    left = 0
    for right in range(1,len(nums)):
        if nums[right] != nums[left]:
            nums[left + 1 ] = nums[right]
            left += 1
        else:
            continue
    return left+1 , nums

"""
time: O(n)
space: O(1)

"""

if __name__ == "__main__":
    num = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicate(num))