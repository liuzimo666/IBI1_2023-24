def calculate_chocolate_bars(total_money, price):
    # calculate how many bars can buy 
    bars = total_money // price
    # calculate the remaining money
    change = total_money % price
    # return
    return bars, change

total_money = 100  # assume the total money is 100 
price = 7  # assume the price of bar is 7

bars_bought, money_left = calculate_chocolate_bars(total_money, price)

# print the result
print(f"you can buy {bars_bought} bars.")
print(f" you will left with{money_left} .")
