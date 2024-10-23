import numpy as np
import matplotlib.pyplot as plt

# generating dataset
X = np.random.randn(500,1)
y = 15 * X + 100 + (np.random.randn(500, 1)*8)

plt.scatter(X, y)
plt.xlabel('feature')
plt.ylabel('target')
plt.grid(True)
plt.show()

def fit(X, y):
    p = 0
    q = 0
    x_mean = X.mean()
    y_mean = y.mean()
    for i in range(X.shape[0]):
        p += (X[i] - x_mean) * (y[i] - y_mean)
        q += (X[i] - x_mean)**2
    m = p/q
    b = y_mean - x_mean * m

    return m, b

def predict(x, m, b):
    return m * x + b

# mean square error
def mse(y_true, y_pred):
    err = 0
    for i in range(len(y_true)):
        err += (y_true[i] - y_pred[i]) ** 2
    return err / len(y_true)

def r2_score(y_true, y_pred):
    ssr = ((y_true - y_pred)** 2).sum()
    ssm = ((y_true - y_true.mean()) ** 2).sum()
    return 1 - ssr/ssm

xTrain, xTest = X[:400], X[400:]
yTrain, yTest = y[:400], y[400:]

m, b = fit(xTrain, yTrain)
print(f'm = {m[0]},\tb = {b[0]}')
print(mse(yTest, predict(xTest, m, b)))
print(r2_score(yTest, predict(xTest, m, b)))

plt.scatter(X, y)
x1, x2 = X.min(), X.max()
y1 = predict(x1, m, b)
y2 = predict(x2, m, b)
plt.plot([x1,x2], [y1,y2], color='red', label='Regression Line')
plt.legend(loc='upper left', labelcolor='black')
plt.xlabel('feature')
plt.ylabel('target')
plt.grid(True)
plt.show()