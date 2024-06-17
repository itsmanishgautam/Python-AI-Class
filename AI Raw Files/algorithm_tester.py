import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score

# Algorithm Identifier
class AlgorithmIdentifier:
    @staticmethod
    def identify(input_data, correct_output, model_type):
        if model_type == "linear_regression":
            return "linear_regression"
        elif model_type == "logistic_regression":
            return "logistic_regression"
        else:
            return "unknown"


class TestRunner:
    def __init__(self, model):
        self.model = model

    def run(self, input_data, iterations=1000):
        results = []
        for _ in range(iterations):
            self.model.fit(input_data['X'], input_data['y'])
            result = self.model.predict(input_data['X'])
            results.append(result)
        return results

# Validator
class Validator:
    @staticmethod
    def validate(results, expected_output, model_type):
        inconsistencies = []
        for result in results:
            if model_type == "linear_regression":
                if not np.allclose(result, expected_output, atol=1e-5):
                    inconsistencies.append(result)
            elif model_type == "logistic_regression":
                if not np.array_equal(result, expected_output):
                    inconsistencies.append(result)
        return len(inconsistencies) == 0, inconsistencies

# Reporter
class Reporter:
    @staticmethod
    def report(is_successful, inconsistencies):
        if is_successful:
            print("Algorithm is consistent and successful.")
        else:
            print(f"Algorithm failed. Inconsistencies found: {len(inconsistencies)} times.")

# Main Test Framework
class TestFramework:
    def __init__(self, model, input_data, expected_output, model_type):
        self.model = model
        self.input_data = input_data
        self.expected_output = expected_output
        self.model_type = model_type

    def run(self):
        # Identify the algorithm type
        algorithm_type = AlgorithmIdentifier.identify(self.input_data, self.expected_output, self.model_type)
        print(f"Identified Algorithm Type: {algorithm_type}")

        # Run the test
        test_runner = TestRunner(self.model)
        results = test_runner.run(self.input_data)

        # Validate the results
        is_successful, inconsistencies = Validator.validate(results, self.expected_output, self.model_type)

        # Report the results
        Reporter.report(is_successful, inconsistencies)

# Example usage for Linear Regression
X_linear = np.array([[1], [2], [4], [3], [5]])
y_linear = np.array([1, 3, 3, 2, 5])
model_linear = LinearRegression()
expected_output_linear = model_linear.fit(X_linear, y_linear).predict(X_linear)

input_data_linear = {'X': X_linear, 'y': y_linear}
test_framework_linear = TestFramework(model_linear, input_data_linear, expected_output_linear, "linear_regression")
test_framework_linear.run()

# Example usage for Logistic Regression
X_logistic = np.array([[0.1], [0.2], [0.4], [0.3], [0.5]])
y_logistic = np.array([0, 0, 1, 0, 1])
model_logistic = LogisticRegression()
expected_output_logistic = model_logistic.fit(X_logistic, y_logistic).predict(X_logistic)

input_data_logistic = {'X': X_logistic, 'y': y_logistic}
test_framework_logistic = TestFramework(model_logistic, input_data_logistic, expected_output_logistic, "logistic_regression")
test_framework_logistic.run()
