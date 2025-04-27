# 3. After accidentally leaving an ice chest of fish and shrimp in your car for a week while you
# were on vacation, you’re now in the market for a new vehicle. Your insurance didn’t cover
# the loss, so you want to make sure you get a good deal on your new car.
# Given a Series of car asking_prices and another Series of car fair_prices, determine which
# cars for sale are a good deal. In other words, identify cars whose asking price is less than
# their fair price.
# The result should be a list of integer indices corresponding to the good deals
# in asking_prices.

import pandas as pd

asking_prices=pd.Series([15000, 17000, 22000, 25000, 18200])
fair_prices =pd.Series( [14000, 17500, 21000, 24000, 18500])
 
good_deals=asking_prices[asking_prices<fair_prices].index.tolist()

print(good_deals)

