# README.md

## Linear Regression from Scratch

This project implements linear regression using Python from scratch, focusing on generating synthetic data, training the model, evaluating performance, and visualizing results using matplotlib.

### Overview

The project performs the following steps:

1. **Data Generation**:
   - Generates a synthetic dataset for regression tasks.
   - Randomly creates X (input) and y (output) variables with added noise.

2. **Model Training**:
   - Implements linear regression using the normal equation approach.
   - Adds a bias term to the input data.
   - Computes optimal weights (coefficients) to minimize the squared error between predicted and actual values.

3. **Evaluation**:
   - Computes predictions on a test set using the trained model.
   - Calculates mean squared error (MSE) to assess model performance.

4. **Visualization**:
   - Plots the training data points.
   - Plots the test data points.
   - Displays the predicted regression line based on the trained model.

### Usage

- **Execution**: Run `main.py` with Python and required dependencies (`random` and `matplotlib`) installed.
- **Output**: Displays coefficients, intercept, and MSE after execution.
- **Plot**: Shows a graphical representation of the data points and the predicted regression line.

### Example

#### Output
```
Coefficient: 2.976
Intercept: 4.007
Mean squared error: 1.128
```

#### Plot

- Blue dots represent training data.
- Green dots represent test data.
- Red line represents the predicted regression line.

### Customization

- Modify dataset parameters and noise levels to explore different scenarios.
- Customize plot labels, titles, and styles using matplotlib features according to specific preferences.
