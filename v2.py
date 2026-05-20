#Solving difference schemes using Taylor series formulation
import math
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# 1. Math Equation
def my_equation(x):
    return 2*x**2       #point_x = 4    | step_dx = 0.2
    
# 2. Logic for 1st and 2nd order derivatives
def calculate_derivatives(func, x, h):
    # First Order Derivative
    f1_fwd = float((func(x + h) - func(x)) / h)
    f1_bwd = float((func(x) - func(x - h)) / h)
    f1_cnt = float((func(x + h) - func(x - h)) / (2 * h))

    # Second Order Derivative
    f2_fwd = float((func(x + 2*h) - 2*func(x + h) + func(x)) / (h**2))
    f2_bwd = float((func(x) - 2*func(x - h) + func(x - 2*h)) / (h**2))
    f2_cnt = float((func(x + h) - 2*func(x) + func(x - h)) / (h**2))

    return {"1st": {"Forward": f1_fwd, "Backward": f1_bwd, "Central": f1_cnt},
            "2nd": {"Forward": f2_fwd, "Backward": f2_bwd, "Central": f2_cnt}}

# 3. Exact Answers
def get_exact_values(expr_func, point_x):
    x_sym = sp.Symbol('x')
    expr = expr_func(x_sym)
    
    # Symbolic derivatives
    d1 = sp.diff(expr, x_sym)
    d2 = sp.diff(d1, x_sym)
    
    # Evaluate at point_x
    val1 = float(d1.subs(x_sym, point_x))
    val2 = float(d2.subs(x_sym, point_x))
    
    return {"1st": val1, "2nd": val2}

# Output
print(" ")
print("Function : f(x) = 2x^2")
point_x = float(input("Enter point x: "))
step_dx = float(input("Enter step size dx (h): "))

results = calculate_derivatives(my_equation, point_x, step_dx)
exacts = get_exact_values(my_equation, point_x)

for order in ["1st", "2nd"]:
    print(f"\n{order} Order Derivative")
    print(f"{'METHOD':<25} | {'RESULT':<15}")
    
    for method, value in results[order].items():
        print(f"{method + ' Difference':<25} | {value:<15.3f}")
    
    print(f"{'Exact Answer':<25} | {exacts[order]:<15.3f}")

# 4. Error Analysis Plot
print("\nGenerating Error Analysis Plot")
# Expanded range to show where round-off error (machine epsilon) dominates
h_values = np.arange(0.1, 1.1, 0.1)
errors_1st = {"Forward": [], "Backward": [], "Central": []}
errors_2nd = {"Forward": [], "Backward": [], "Central": []}

for h in h_values:
    res = calculate_derivatives(my_equation, point_x, h)
    
    # Errors for 1st order
    errors_1st["Forward"].append(abs(res["1st"]["Forward"] - exacts["1st"]))
    errors_1st["Backward"].append(abs(res["1st"]["Backward"] - exacts["1st"]))
    errors_1st["Central"].append(abs(res["1st"]["Central"] - exacts["1st"]))
    
    # Errors for 2nd order
    errors_2nd["Forward"].append(abs(res["2nd"]["Forward"] - exacts["2nd"]))
    errors_2nd["Backward"].append(abs(res["2nd"]["Backward"] - exacts["2nd"]))
    errors_2nd["Central"].append(abs(res["2nd"]["Central"] - exacts["2nd"]))

# Plots
plt.figure(figsize=(14, 6))

# Plot for 1st Order Errors
plt.subplot(1, 2, 1)
plt.plot(h_values, errors_1st["Forward"], 'r--', label='Forward Difference Error')
plt.plot(h_values, errors_1st["Backward"], 'b-.', label='Backward Difference Error')
plt.plot(h_values, errors_1st["Central"], 'g', linewidth=2, label='Central Difference Error')
plt.xlabel('Step Size (h)')
plt.ylabel('Absolute Error')
plt.title(f'1st Order Derivative')
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend()

# Plot for 2nd Order Errors
plt.subplot(1, 2, 2)
plt.plot(h_values, errors_2nd["Forward"], 'r--', label='Forward Difference Error')
plt.plot(h_values, errors_2nd["Backward"], 'b-.', label='Backward Difference Error')
plt.plot(h_values, errors_2nd["Central"], 'g', linewidth=2, label='Central Difference Error')
plt.xlabel('Step Size (h)')
plt.ylabel('Absolute Error')
plt.title(f'2nd Order Derivative')
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend()

plt.suptitle(f'Error Analysis of Numerical Derivatives at x = {point_x}\nFunction: f(x) = 2x^2')
plt.tight_layout()
plt.show()
print(" ")