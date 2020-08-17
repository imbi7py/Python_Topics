'''
Created on Oct 14, 2019

@author: tongq
'''
class Solution(object
    ___ profitableSchemes(self, G, P, group, profit
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        dp = [[0]*(G+1) ___ _ in range(P+1)]
        dp[0][0] = 1
        ___ p, g in zip(profit, group
            ___ i in range(P, -1, -1
                ___ j in range(G-g, -1, -1
                    dp[min(i+p, P)][j+g] += dp[i][j]
        r_ su.(dp[P])%(10**9 + 7)
    
    ___ profitableSchemes_DFS_TLE(self, G, P, group, profit
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        res = [0]
        self.dfs(0, group, profit, G, P, [], 0, res)
        r_ res[0]
    
    ___ dfs(self, ind, group, profit, G, P, curGroup, curProfit, res
        __ curProfit >= P and su.(curGroup) <= G:
            res[0] += 1
        ___ i in range(ind, le.(group)):
            curProfit += profit[i]
            curGroup.append(group[i])
            self.dfs(i+1, group, profit, G, P, curGroup, curProfit, res)
            curGroup.p..
            curProfit -= profit[i]
    
    ___ test(self
        testCases = [
            [
                5, 3, [2,2], [2,3]
            ],
            [
                10, 5, [2,3,5], [6,7,8]
            ],
        ]
        ___ G, P, group, profit in testCases:
            res = self.profitableSchemes(G, P, group, profit)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
