import pandas as pd

# # Code on page 512
wwc = pd.read_csv('wwc2019_q-f.csv')
print(wwc)
#print(wwc.to_string())

# # Code on page 513
# for i in wwc.index:
#     print(i)

# # Code on page 514   
#for c in wwc.columns:
#     print(c)
    
# print(wwc.values)

# # Code on page 515
#creating a DataFrame
# print(pd.DataFrame())

#rounds = ['Semis', 'Semis', '3rd Place', 'Championship']
#print(pd.DataFrame(rounds))

# print(pd.DataFrame({'Round': rounds}))

#rounds = ['Semis', 'Semis', '3rd Place', 'Championship']
#teams = ['USA', 'Netherlands', 'Sweden', 'USA']
#df = pd.DataFrame({'Round': rounds, 'Winner': teams})
# print(df)
#
# Adding columns
# Code on page 516
#df['W Goals'] = [2, 1, 0, 0]
# print(df)

# df['W Goals'] = [2, 1, 2, 2]
# print(df)

#Dropping columns
#print(df.drop('Winner', axis = 'columns'))

#Adding rows
# # Code on page 517
#quarters_dict = {'Round': ['Quarters']*4,
 #                 'Winner': ['England', 'USA', 'Netherlands', 'Sweden'],
 #               'W Goals': [3, 2, 2, 2]}
#df = pd.concat([pd.DataFrame(quarters_dict), df], sort = False) 
# print(df.to_string())

# print(pd.concat([pd.DataFrame(quarters_dict), df], sort = True).to_string())

# # Code on page 518
#print(df.reset_index(drop = True).to_string())

#print(df.set_index('Round').to_string())

#print(wwc['Winner'].to_string())

# # Code on page 519
# print(wwc['Winner'][3])

# winners = ''
# for w in wwc['Winner']:
#     winners += w + ','
# print(winners[:-1])

"""Exercise: Write a function that returns the sum of the goals scored by the winners."""

#print(wwc[['Winner', 'Loser']].to_string())

# # Code on page 520
#print(wwc[['Round','Winner','Loser','W Goals','L Goals']].to_string())

#print(wwc[1:2]) #select rows by slicing, but not wwc[1]

#Select using loc and iloc
# print(wwc.loc[3])

# # Code on page 521
# print(wwc.loc[[1,3,5]])

# print(wwc.loc[3:7:2])

# print(wwc.loc[6:])

# # Code on page 522
# print(wwc.loc[:2])

"""Exercise: Write an expression that selects all even numbered rows in wwc."""

# print(wwc.loc[0:2, 'Round':'L Goals':2])

"""Exercise: Write an expression that generates the DataFrame

    Round		Winner		W Goals 	Loser 	 L Goals
1	Quarters	USA				2		France	    1
2	Quarters 	Netherlands		2		Italy		0
"""
wwc_by_round = wwc.set_index('Round')
# print(wwc_by_round.to_string())

# # Code on page 523
# print(wwc_by_round.loc['Semis'])

# print(wwc_by_round.loc[['Semis', 'Championship']])

# print(wwc_by_round.loc['Quarters':'Semis':2])

#print(wwc_by_round.iloc[[1,2]])

