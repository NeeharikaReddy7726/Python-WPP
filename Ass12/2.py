# 2. Write a Pandas program to convert all the string values to upper, lower cases in a given
# pandas series. Also find the length of the string values.
# s = pd.Series ([‘X’, ‘Y’, ‘T’, ‘Aaba’, ‘Baca’, ‘CABA’, None, ‘bird’, ‘horse’, ‘dog’])
import pandas as pd,string
s = pd.Series (['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA',None, 'bird', 'horse', 'dog'])
up=[];lo=[];length=[]
df = pd.DataFrame({
    'uppercase': s.fillna('').apply(lambda x: x.upper()),
    'lowercase': s.fillna('').apply(lambda x: x.lower()),
    'length_of_str': s.fillna('').apply(len)
})
print(df)