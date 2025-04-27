# 4. Whenever your friends John and Judy visit you together, y’all have a party. Given a
# DataFrame with 10 rows representing the next 10 days of your schedule and whether John
# and Judy are scheduled to make an appearance, insert a new column
# called days_til_party that indicates how many days until the next party.
# days_til_party should be 0 on days when a party occurs, 1 on days when a party doesn’t
# occur but will occur the next day, etc.

import pandas as pd,random

df=pd.DataFrame({
    "Day":range(1,11),
    "John_appearance":[random.randint(0,1) for i in range(1,11) ] ,
    "Judy_appearance":[random.randint(0,1) for i in range(1,11) ] 
})
 
# Identify party days
df["party"] = df["John_appearance"] & df["Judy_appearance"]
df["days_til_party"] = "No party ahead"  # Default -> no party is found ahead

# Track the next party index
next_party = -1

# Loop from last to first row
for i in df.index[::-1]:
    if df.loc[i, "party"] == 1:
        df.loc[i, "days_til_party"] = 0
        next_party = i
    elif next_party != -1:
        df.loc[i, "days_til_party"] = next_party - i
    # Else it stays -> No party ahead

# Drop helper column
df.drop(columns=["party"], inplace=True)

print(df)