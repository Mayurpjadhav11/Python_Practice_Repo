import numpy as np
from sklearn.neural_network import MLPClassifier

# Training data: [Age (normalized), Salary (normalized)]
X = np.array([
    [0.2, 0.3],  # young, low salary → no
    [0.5, 0.8],  # mid-age, good salary → yes
    [0.6, 0.4],  # mid-age, low salary → maybe
    [0.9, 0.9],  # older, high salary → yes
    [0.1, 0.2],  # very young, low salary → no
])

# Labels: 1 = will buy, 0 = won't buy
y = np.array([0, 1, 0, 1, 0])

# Create the model: 1 neuron (no hidden layers), sigmoid activation
model = MLPClassifier(
    hidden_layer_sizes=(),   # No hidden layers → single neuron
    activation='logistic',   # Sigmoid function
    solver='sgd',            # Stochastic Gradient Descent
    learning_rate_init=0.1,  # Learning rate
    max_iter=1000,           # Number of training epochs
    random_state=42          # For reproducibility
)

# Train the model
model.fit(X, y)

# Test predictions
test_inputs = np.array([
    [0.2, 0.3],  # Expected: 0
    [0.5, 0.8],  # Expected: 1
    [0.6, 0.4],  # Expected: 0 or uncertain
    [0.9, 0.9],  # Expected: 1
])

predictions = model.predict_proba(test_inputs)[:, 1]  # probability of class 1
binary_preds = model.predict(test_inputs)  # 0 or 1

# Show results
for i in range(len(test_inputs)):
    print(f"Input: {test_inputs[i]}, Probability of buying: {predictions[i]:.4f}, Prediction: {binary_preds[i]}")
