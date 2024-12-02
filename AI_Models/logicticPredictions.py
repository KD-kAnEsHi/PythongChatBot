import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt
from sklearn.linear_model import LogisticRegression

data = {
  "x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
  "y": [0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print(df.head())
print(df.shape)

X = df[['x']]
Y = df['y']
model = LogisticRegression()
model.fit(X, Y)

x_values = pd.DataFrame(np.linspace(X.min(), X.max(), 100), columns=['x'])
y_values = model.predict_proba(x_values).T[1]  # Probability of recovery (y = 1)


plt.scatter(X, Y, color = 'blue')
plt.plot(x_values, y_values, color='red', label='Logistic Regression')

plt.xlabel('Drug Dosage (x)')
plt.ylabel('Recovery (y)')
plt.title('Data Visualization')
plt.grid(True)
plt.show()


new_x = pd.DataFrame([[14.23]], columns=['x'])
predicted_class = model.predict(new_x)
print(f"Predicted class is: {predicted_class[0]}")


#If you're interested in the probability of belonging to each class, use the model.
# predict_proba() method instead of model.predict(). This will return an array of probabilities
# for each class.