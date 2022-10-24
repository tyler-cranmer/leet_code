''' 
https://leetcode.com/problems/valid-anagram/ - EASY

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

'''

def isAnagram(s, t):
    dic = {}
    
    if len(s) != len(t):
        return False

    for i, ch in enumerate(s):
        if ch not in dic:
            dic[ch] = 1
        else:
            dic[ch] += 1
    for j, ch2 in enumerate(t):
        if ch2 not in dic:
            return False
        elif ch2 in dic:
            dic[ch2] -= 1
    max_value = max(dic.values())

    if max_value > 0:
        return False
    else: 
        return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    a = 'rat'
    b = 'car' 

    print(isAnagram(s, t))
    print(isAnagram(a,b))