# 5. Given a dataset of concerts, count the number of concerts per (artist, venue), per year
# month. Make the resulting table be a wide table - one row per year month with a column
# for each unique (artist, venue) pair. Use the cross product of the artists and venues Series
# to determine which (artist, venue) pairs to include in the result.

import pandas as pd

df = pd.read_csv("lab/assignment 11/data.csv")

# Step 1: Convert 'date' to datetime and extract 'year' and 'month'
df['date'] = pd.to_datetime(df['date'])
df['year_month'] = df['date'].dt.to_period('M')  # Year-Month period

# Step 2: Count concerts per (artist, venue) and year_month
concert_count = df.groupby(['year_month', 'artist', 'venue']).size().reset_index(name='concert_count')

# Step 3: Pivot the table to get a wide format (artist-venue pairs as columns)
wide_table = concert_count.pivot_table(index='year_month', columns=['artist', 'venue'], values='concert_count', aggfunc='sum', fill_value=0)

print(wide_table)
