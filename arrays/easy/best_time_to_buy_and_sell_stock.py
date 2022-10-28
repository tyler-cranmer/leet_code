'''
121. Best Time to Buy and Sell Stock EASY

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104



'''
import math

def maxProfits_brute(prices: list) -> int:
    max_profit = 0
    N = len(prices)
    for i in range(N):
        for j in range(i+1,N):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit

''' time: 0(n^2) space: O(1)'''

def maxProfits(prices: list)-> int:
    min_price = math.inf
    max_profit = 0
    N = len(prices)
    for i in range(N):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit

''' time: 0(n) space: O(1)'''

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    prices2 = [7,6,4,3,1]

    print(maxProfits(prices))
    print(maxProfits(prices2))
