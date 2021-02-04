import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

df = pd.read_csv("FuelConsumption.csv")

# take a look at the dataset
print(df.head)
df.describe()
data = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
data.head(9)
individual_bars = data[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
individual_bars.hist()
plt.show()

randdata = np.random.rand(len(df)) < 0.8
train = data[randdata]
test = data[randdata]

plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.title("Linear relation between Engie Size and CO2 Emission")
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

from sklearn import linear_model
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit (train_x, train_y)
# The coefficients
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)

plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
plt.title("LINEAR REGRESSION")
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_hat = regr.predict(test_x)

mse=np.mean((test_y_hat - test_y) ** 2)
mae=np.mean(np.absolute(test_y_hat - test_y))
r2= r2_score(test_y_hat , test_y)
print("Mean absolute error: %.2f" %mae)
print("Residual sum of squares (MSE): %.2f" % mse)
print("R2-score: %.2f" % r2)

plt.scatter('Mean Absolute Error: ', mae)
plt.scatter('Mean Squared Error: ', mse)
plt.scatter('R2-score: ', r2)
plt.title("Errors")
plt.show()
