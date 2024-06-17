# README.md

## Overview

This project uses TensorFlow/Keras for text classification using an Embedding layer and a neural network for binary classification.

## Features

- **Data**: Loads text data and labels from `label_only_numeric_exported_data.csv`.
- **Preprocessing**: Tokenizes text, converts to sequences, and pads them for uniform length.
- **Model**: Embedding layer, GlobalAveragePooling1D, Dense layers for classification.
- **Training**: Model trained with binary crossentropy loss and adam optimizer.
- **Prediction**: Function to predict labels for user-input sentences.

## Usage

1. **Dataset**: Ensure `label_only_numeric_exported_data.csv` has `StringData` and `Labels`.
2. **Execution**: Run `main.py` with necessary dependencies installed.
3. **Prediction**: Use `predict_user_input` function for custom sentence predictions after training.

## Example

### Input
```
Enter a sentence: This movie is great!
```

### Output
```
Predicted Labels: [1]
```

## Training

- Model trained for 10 epochs with 20% validation split.
- Evaluates model performance on entire dataset, displaying loss and accuracy.

---

This concise README summarizes your TensorFlow/Keras text classification project, focusing on functionality, usage, and customization options. Adjust details based on specific project requirements or updates.