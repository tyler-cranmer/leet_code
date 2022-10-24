'''
https://leetcode.com/problems/longest-palindromic-substring/ MEDIUM

Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
 '''

# brute force
# def longestPalindrome(s: str) -> str:
#     N = len(s)
#     max_p = ''
#     if N == 1:
#         return s
#     for i in range(N):
#         p = i + 1
#         while p <= N:
#             current = s[i:p]
#             if current == current[::-1] and len(current) > len(max_p):
#                 max_p = current
#                 p += 1
#             else:
#                 p += 1     
#     return max_p

def longestPalindrome(s: str) -> str:
    N = len(s)
    if N <= 1:
        return s
    max_length = 1
    st, end = 0, 0

    #odd length
    for i in range(N-1):
        left = i
        right = i
        while left >= 0 and right < N:
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        current_length = right - left - 1
        if(current_length > max_length):
            max_length = current_length
            st = left + 1
            end = right - 1
    #even length
    for i in range(N-1):
        left = i
        right = i + 1
        while left >= 0 and right < N:
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        current_length = right - left - 1
        if(current_length > max_length):
            max_length = current_length
            st = left + 1
            end = right - 1

    return s[st:end+1]

   

if __name__ == '__main__':
    # s = "yfikrcvmuegdciuqahlsjesplljlswxaejgdzhubzqkiroxyhtjvazcwcnsvdzjiainmiyobyfclyugttaswlntwukkfbebcdaxdpaxwqenkxxphxdcgrnpruoaetvunwyskswvvmjmltncsdukwzlpfodhgxkjvzppwpvmqlfbojgbdiryleskemhjfoxxzjqihcykpgzhaugwwbqtddjzpmrgdncgzsttqenmbnnavfjkiennwxtguywoaiuungqpyfcffzmljfianapawiayywuvazrnxouvndzqbmmyntkkdyykgodjbeojtpnsyhfrltuazgznddaaibupephvgrcjpzvjttmhtnydwvrpgijselaukwrcosxpcbptebalkheymuyblffahvbszotmutmmqhlgoskuoejvavlprvgyozpylsnqhqrnqpabgbwzwxyibpmsauxcfnbtwwbosksuzqzmobijytxxtyjibomzqzusksobwwtbnfcxuasmpbiyxwzwbgbapqnrqhqnslypzoygvrplvavjeouksoglhqmmtumtozsbvhafflbyumyehklabetpbcpxsocrwkualesjigprvwdynthmttjvzpjcrgvhpepubiaaddnzgzautlrfhysnptjoebjdogkyydkktnymmbqzdnvuoxnrzavuwyyaiwapanaifjlmzffcfypqgnuuiaowyugtxwnneikjfvannbmneqttszgcndgrmpzjddtqbwwguahzgpkychiqjzxxofjhmekselyridbgjobflqmvpwppzvjkxghdofplzwkudscntlmjmvvwsksywnuvteaourpnrgcdxhpxxkneqwxapdxadcbebfkkuwtnlwsattguylcfyboyimniaijzdvsncwczavjthyxorikqzbuhzdgjeaxwsljllpsejslhaquicdgeumvcrkify"
    s = "aab"
    print(longestPalindrome(s))
    