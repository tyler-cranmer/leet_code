''' 
2. Add Two Numbers Medium

https://leetcode.com/problems/add-two-numbers/


You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

'''

class node:
    def __init__(self,val=None, next=None):
        self.val = val
        self.next = next
        
class linked_list:
    def __init__(self):
        self.head = None
        
    def append(self, val):
        new_node = node(val)
        
        if self.head == None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def display(self):
        elements = []
        current_node = self.head
        if current_node == None:
            return print("Empty List []")
        while current_node:
            elements.append(current_node.val)
            current_node = current_node.next
        print(elements)

def addTwoNumbers(l1: list, l2: list):
    dummy_head = node(0)
    carry = 0
    
    # while l1 != None or l1 != None or carry !=0:
    #     l1val = l1.val if l1 else 0
    #     l2val = l2.val if l2 else 0
    #     columnSum = l1val + l2val + carry
    #     carry = columnSum // 10
    #     newNode = node(colmnSum % 10)
    #     current_node.next = newNode
    #     current_node = newNode
    #     l1 = l1.next if l1 else None
    #     l2 = l2.next if l2 else None
    # return dummy_head.next

if __name__ == '__main__':
    l1 = linked_list()
    l2 = linked_list()
    l1.append(2)
    l1.append(4)
    l1.append(3)
    l2.append(5)
    l2.append(6)
    l2.append(4)
    l1.display()
    l2.display()
    print(addTwoNumbers(l1,l2))


