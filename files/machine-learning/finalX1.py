#CS235 Final Exam 1
#Name:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


#No additional imports are allowed

# Read the file
with open('finalData.txt', 'r') as file:
    lines = file.readlines()
    
    #chat gpt give me a new way to open and read the file :)

# Extract the hotness category which is the last instance of the data
hotness = [int(line.strip().split()[-1]) for line in lines]

#count the occurrences of each unique category
categories, counts = np.unique(hotness, return_counts=True)

# Create the bar graph
plt.figure(figsize=(10, 6))
plt.bar(categories, counts, color='red')
plt.xlabel('Hotness Category')
plt.ylabel('Number of Peppers')
plt.title('Number of Peppers in Each Hotness Category')
plt.show()

file.close()





# Load the data
with open('finalData.txt', 'r') as file2:
    lines = file2.readlines()

file2.close()

X = []
y = []

# Define a simple encoding for the categorical column
category_map = {'A': 0.0, 'B': 1.0, 'C': 2.0}

for line in lines:
    parts = line.strip().split()
    if len(parts) == 6:
        try:
            # Convert the value to a number
            cat_encoded = category_map[parts[2]]
            features = list(map(float, [parts[0], parts[1], parts[3], parts[4]]))
            features.insert(2, cat_encoded)  # Insert encoded category in the correct position
            X.append(features)
            y.append(int(parts[5]))
        except KeyError:
            print(f'Unexpected category value: {parts[2]}')
        except ValueError:
            print(f'Could not convert parts of this line to float: {line}')

X = np.array(X)
y = np.array(y)

# Train the model
model = LinearRegression()
model.fit(X, y)

# Output the model parameters
#print("Coefficients:", model.coef_)
#print("Intercept:", model.intercept_)


equation = 'y = '

for i, coef in enumerate(model.coef_):
    if i == 0:
        equation += f'{coef:.3f}x[{i}]'
        
    elif coef >= 0:
        equation += f'+ {coef:.3f}x[{i}] '
    else:
        equation += f'- {abs(coef):.3f}x[{i}] '

equation += f'+ {model.intercept_:.3f}'

print(equation)




#Load peppers.txt data 
with open("peppers.txt", "r") as file3:
    pepper_lines = file3.readlines()

category_map = {'A': 0.0, 'B': 1.0, 'C': 2.0}
pepper_features = []

for line in pepper_lines:
    parts = line.strip().split()
    if len(parts) == 5:
        try:
            cat_encoded = category_map[parts[2]]
            features = list(map(float, [parts[0], parts[1], parts[3], parts[4]]))
            features.insert(2, cat_encoded)  # Insert category encoding at the right index
            pepper_features.append(features)
        except KeyError:
            print(f'Unexpected category value: {parts[2]}')
        except ValueError:
            print(f'Could not convert parts of this line to float: {line}')

pepper_features = np.array(pepper_features)

#Predict with trained model
predictions = model.predict(pepper_features)

print('\nPepper     Classification')
print('--------------------------')
for i, pred in enumerate(predictions):
    print(f'{i+1}            {pred:.0f}')
