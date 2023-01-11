'''
You are given an m x n integer grid accounts
where accounts[i][j] is the amount of money
the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank.

Return the wealth that the richest customer has.

A customer's wealth is the amount of money
they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.

Explanation:

1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
'''


class Solution:
    def maximumWealth(accounts):
        return max(sum(value) for value in accounts)
    print(maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
