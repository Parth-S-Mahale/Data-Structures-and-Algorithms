prices = [7,2,1,5,6,4,8]

def maxProfit(prices) -> int:
    n = len(prices)
    min_price = float("inf")
    max_profit = 0
    for i in range(0, n):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
        
    return max_profit

print(maxProfit(prices))