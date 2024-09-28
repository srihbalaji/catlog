import json
import numpy as np

# The JSON data (you can also load this from a file)
data = {
    "keys": {
        "n": 4,
        "k": 3
    },
    "1": {
        "base": "10",
        "value": "4"
    },
    "2": {
        "base": "2",
        "value": "111"
    },
    "3": {
        "base": "10",
        "value": "12"
    },
    "6": {
        "base": "4",
        "value": "213"
    }
}

# Function to convert a value from a given base to base 10
def convert_to_base10(value, base):
    return int(value, base)

# Extract the points from the JSON
points = []
for key in ['1', '2', '3']:  # We only need 3 points as k = 3
    x = int(key)  # x value is the key
    base = int(data[key]["base"])  # Base for y
    y = convert_to_base10(data[key]["value"], base)  # y value after conversion
    points.append((x, y))

# Now points contains [(1, 4), (2, 7), (3, 12)]

# We need to set up the system of equations:
# ax^2 + bx + c = y for each point

# Coefficient matrix (LHS)
A = np.array([
    [points[0][0]**2, points[0][0], 1],  # 1^2, 1, 1
    [points[1][0]**2, points[1][0], 1],  # 2^2, 2, 1
    [points[2][0]**2, points[2][0], 1]   # 3^2, 3, 1
])

# Right-hand side (RHS)
B = np.array([points[0][1], points[1][1], points[2][1]])  # [4, 7, 12]

# Solve the system using numpy's linear algebra solver
coefficients = np.linalg.solve(A, B)

# The constant term 'c' is the last coefficient
a, b, c = coefficients
print(f"Constant term (c) of the polynomial is: {c}")
