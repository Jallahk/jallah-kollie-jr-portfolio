from pyexpat import features

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#load data
data = pd.read_csv('realest.csv')
#shows the first few lines of the data
print(data.head())
#check basic info of the data
print(data.info())
#checks for massive values/missing values
print(data.isnull().sum())

#remove rows/columns with empty data
data = data.dropna()

'''# select the features that we will use to train model
#features are things that is going to affect the target
#features have a strong relationship with the target
# code below Calculate correlations with the target variable if had to decide what 
the features are
correlation_matrix = data.corr()
print(correlation_matrix['SalePrice'].sort_values(ascending=False))
'''
features = ['Bedroom', 'Space','Room', 'Lot', 'Bathroom','Garage','Condition']

#the target is what you want your end goal to be/ what you want the machine to predict
target = 'Price'

#prepare x and y
X = data[features]
Y = data[target]

#split into training and testing data
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2,random_state=42)

#initiallize the model
model = LinearRegression()

#trains the model
model.fit(X_train,Y_train)

#checks model coefficient and intercept
print('Coefficient: ',model.coef_)
print('intercept: ', model.intercept_)


#predicts on the test set
y_pred = model.predict(X_test)

#calculate metrics
mse = mean_squared_error(Y_test,y_pred)
r2 = r2_score(Y_test, y_pred)

print('Mean Squared error: ', mse)
print('R2 Score: ', r2)

#plot actual value vs predicted prices difference between the two
plt.scatter(Y_test,y_pred)
plt.xlabel("Actual Prices")
plt.ylabel('predicted Prices')
plt.title('Actual vs Predicted Prices')
plt.show()


















#if you have features with different values, ex: hundreds vs thousands
#you can scale it to get a better model
'''from sklearn.preprocessing import StandardScaler

# Initialize scaler
scaler = StandardScaler()

# Scale the features
X = scaler.fit_transform(X)

# Optional: Scale the test data separately
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)'''
