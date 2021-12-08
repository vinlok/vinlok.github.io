
algo:

1. set low price to = 9999
2. max_profit = 0
3. now iterate on prices:

    if price > low:

        max_profit= max(price-low,max_profit)

    else:
        low=prices
