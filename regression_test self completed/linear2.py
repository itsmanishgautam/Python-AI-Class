import random
import matplotlib.pyplot as plt

# Generate random dataset
random.seed(0)
X = [[random.uniform(0, 2)] for _ in range(100)]
y = [[4 + 3 * x[0] + random.gauss(0, 1)] for x in X]

train_ratio = 0.8
train_size = int(len(X) * train_ratio)
X_train = X[:train_size]
y_train = y[:train_size]
X_test = X[train_size:]
y_test = y[train_size:]

# Add bias term to training and testing data
def add_bias_term(X):
    return [[1] + x for x in X]

X_train_b = add_bias_term(X_train)
X_test_b = add_bias_term(X_test)

def transpose(matrix):
    return list(map(list, zip(*matrix)))

def matmul(A, B):
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in transpose(B)] for A_row in A]

def inverse_2x2(matrix):
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    det = a * d - b * c
    return [[d / det, -b / det], [-c / det, a / det]]

X_train_b_T = transpose(X_train_b)
X_train_b_T_X_train_b = matmul(X_train_b_T, X_train_b)
X_train_b_T_X_train_b_inv = inverse_2x2(X_train_b_T_X_train_b)
X_train_b_T_y_train = matmul(X_train_b_T, y_train)
theta_best = matmul(X_train_b_T_X_train_b_inv, X_train_b_T_y_train)

print(f"Coefficient: {theta_best[1][0]}")
print(f"Intercept: {theta_best[0][0]}")

y_test_pred = matmul(X_test_b, theta_best)

mse = sum((y_test[i][0] - y_test_pred[i][0]) ** 2 for i in range(len(y_test))) / len(y_test)
print(f"Mean squared error: {mse}")

plt.plot([x[1] for x in X_train_b], [y[0] for y in y_train], "b.", label="Training data")
plt.plot([x[1] for x in X_test_b], [y[0] for y in y_test], "g.", label="Test data")
plt.plot([x[1] for x in X_test_b], [y[0] for y in y_test_pred], "r-", linewidth=2, label="Predicted line")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.title("Linear Regression from Scratch")
plt.show()
