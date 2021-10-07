def stock_prof(a):
    '''
    algo
    set  minprice = first element of array
    set profit = 0
    m_i=0
    iterate over the array from 1

    if a[i] < minprice:
        minprice = a[i]

    if a[i] - minprice > profit:
        profit = a[i] - minprice


    :param a:
    :return:
    '''


array = [1, 2, 3, 4, 3, 2, 1, 2, 5]
result = find_buy_sell_stock_prices(array)
print("Buy Price: " + str(result[0]) + ", Sell Price: " + str(result[1]))

array = [8, 6, 5, 4, 3, 2, 1]
result = find_buy_sell_stock_prices(array)
print("Buy Price: " + str(result[0]) + ", Sell Price: " + str(result[1]))