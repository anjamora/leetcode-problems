class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        mprofit = 0
        for i in prices:
            if i < buy:
                buy = i
                sell = i
            elif i > sell:
                sell = i
                if (sell - buy) >= mprofit: 
                    mprofit = sell - buy
        
        return mprofit