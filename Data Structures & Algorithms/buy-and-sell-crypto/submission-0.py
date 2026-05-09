class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mip=prices[0]
        map=0
        for price in prices:
            if price<mip:
                mip = price
            map  = max(map,price - mip)
        return map
