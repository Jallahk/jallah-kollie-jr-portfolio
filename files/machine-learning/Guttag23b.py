from Guttag23a import *

# # Code on page 525

#print(wwc.loc[wwc['Winner'] == 'Sweden'])
#Logical operators:  & = and, | = or, - = not
#print(wwc.loc[(wwc['Winner'] == 'Sweden') | (wwc['Loser'] == 'Sweden')])

"""Exercise: Write an expression that returns a DataFrame containing games
             in which the USA but not France played."""

print(wwc.loc[(wwc['Winner'] == 'USA') | -(wwc['Loser'] == 'France')])

# # Code on page 526
def get_country(df, country):
    """df a DataFrame with series labeled Winner and Loser
        country a str
        returns a DataFrame with all rows in which country appears
        in either the Winner or Loser column"""
    return df.loc[(df['Winner'] == country) | (df['Loser'] == country)]

#print(get_country(wwc,'Sweden'))

#print(get_country(get_country(wwc, 'Sweden'),'Germany'))

#The isin method filters a DataFrame by selecting only those rows with a specified value
#(or element of a specified collection of values) in a specified column. 

def get_games(df, countries):
    return df[(df['Winner'].isin(countries) |
                df['Loser'].isin(countries))]
#print(get_games(wwc,['Sweden']))

"""Exercise: Print a DataFrame containing only the games in which
             Sweden played either Germany or Netherlands."""
print(get_games(wwc,['Sweden']))

# # Code on page 527
print(wwc['W Goals'].sum())
print(wwc['W Goals'].mean())
print(wwc['W Goals'].std())
print((wwc[wwc['Winner'] == 'Sweden']['W Goals'].sum() +
        wwc[wwc['Winner'] == 'Sweden']['L Goals'].sum()))

# print((wwc['W Goals'].sum() - wwc['L Goals'].sum())/len(wwc['W Goals']))

"""Exercise:  Write an expression that computes the total number of goals
              scored in all of the rounds."""

"""Exercise:  Write an expression that computes the total number of goals
              scored by the losing teams in the quarter finals."""
