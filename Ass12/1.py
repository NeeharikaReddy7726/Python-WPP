# 1. Write a Pandas program to create
import pandas as pd
from datetime import datetime,date,time

# a) Date time object for Jan 15 2012.
d1=pd.Timestamp('2012-01-15')
print("a) Date time object for Jan 15 2012:",d1)

# b) Specific date and time of 9:20 pm.
d2=pd.Timestamp('2006-11-21 21:20')
print("b) Specific date and time of 9:20 pm:",d2)

# c) Local date and time.
d3=pd.Timestamp.now()
print("c) Local date and time:",d3)

# d) A date without time.
d4=pd.to_datetime(date.today())
print("d) A date without time:",d4.date())

# e) Current date.
d5=pd.Timestamp.today().date()
print("e) Current Date:", d5)

# f) Time from a date time
dt6 = pd.Timestamp('2025-04-10 14:45:30')
print("f) Time from DateTime:", dt6.time())

# g) Current local time
dt7 = datetime.now().time()
print("g) Current Local Time:", dt7)


