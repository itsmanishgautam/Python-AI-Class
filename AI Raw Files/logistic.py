import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def initialize_parameters(self, num_features):
        self.weights = np.zeros((num_features, 1))
        self.bias = 0

    def fit(self, X, y):
        m, num_features = X.shape
        self.initialize_parameters(num_features)

        for _ in range(self.num_iterations):
            # Compute predictions
            linear = np.dot(X, self.weights) + self.bias
            predictions = self.sigmoid(linear)

            # Compute gradients
            dw = (1 / m) * np.dot(X.T, (predictions - y))
            db = (1 / m) * np.sum(predictions - y)

            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        linear = np.dot(X, self.weights) + self.bias
        predictions = self.sigmoid(linear)
        return (predictions > 0.5).astype(int)

# Define the dataset
X_train = np.array([
    [19, 19000],
    [35, 20000],
    [26, 43000],
    [27, 57000],
    [19, 76000],
    [27, 58000],
    [27, 84000],
    [32, 150000],
    [25, 33000],
    [35, 65000],
    [26, 80000],
    [26, 52000],
    [20, 86000],
    [32, 18000],
    [18, 82000],
    [29, 80000],
    [47, 25000],
    [45, 26000],
    [46, 28000],
    [48, 29000],
    [45, 22000],
    [47, 49000],
    [48, 41000],
    [45, 22000],
    [46, 23000],
    [47, 20000],
    [49, 28000],
    [47, 30000],
    [29, 43000],
    [31, 18000],
    [31, 74000],
    [27, 137000],
    [21, 16000],
    [28, 44000]
])

y_train = np.array([
    0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    1, 0, 0
])

# Normalize features
X_train[:, 0] = (X_train[:, 0] - np.mean(X_train[:, 0])) / np.std(X_train[:, 0])
X_train[:, 1] = (X_train[:, 1] - np.mean(X_train[:, 1])) / np.std(X_train[:, 1])

# Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
X_test = np.array([
    [32, 170000],
    [40, 38000],
    [45, 75000]
])

# Normalize test features
X_test[:, 0] = (X_test[:, 0] - np.mean(X_train[:, 0])) / np.std(X_train[:, 0])
X_test[:, 1] = (X_test[:, 1] - np.mean(X_train[:, 1])) / np.std(X_train[:, 1])

predictions = model.predict(X_test)
print("Predictions:", predictions)

print("Shape of dw:", dw.shape)
print("Shape of self.weights:", self.weights.shape)
