import numpy as np

print("🚀 Training started...")

# dummy training
X = np.random.rand(100, 1)
y = 2 * X + 1

# simple "model"
weight = 2
bias = 1

print("Model trained!")
print(f"Weight: {weight}, Bias: {bias}")