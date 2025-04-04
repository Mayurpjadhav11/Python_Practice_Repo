import numpy as np

# Step 1: Inputs (2 features)
inputs = np.array([1.0, 2.0])  # x1 = 1.0, x2 = 2.0

# Step 2: Weights (2 weights for 2 inputs)
weights = np.array([0.5, -0.6])  # w1 = 0.5, w2 = -0.6

# Step 3: Bias
bias = 0.1

# Step 4: Linear combination
z = np.dot(inputs, weights) + bias

# Step 5: Activation function (sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Step 6: Output
output = sigmoid(z)

print(f"Neuron output: {output:.4f}")