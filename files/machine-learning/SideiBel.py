import pandas as pd

sbdf = pd.read_csv('SidiBelregion.csv')
print(sbdf)

sbdf = sbdf.rename(columns = {' RH':'RH', 'Classes  ':'Classes',' Ws':'Ws'})
print(sbdf.columns)

firecount = 0
for d in sbdf['Classes']:
    if 'n' not in d:
        firecount+=1
print(firecount/len(sbdf.index))