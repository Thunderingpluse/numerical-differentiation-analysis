#Solving difference schemes using Taylor series formulation

import math
import sympy as sp

# 1. Define the Math Equation
def my_equation(x):
    return 2*x**2                       #point_x = 4    | step_dx = 0.2
    #return sp.sin(2 * sp.pi * x)       #point_x = 0.25 | step_dx = 0.1
    
# 2. Calculation Logic for 1st, 2nd and 3rd order derivatives
def calculate_derivatives(func, x, h):
    # First Order Derivative
    f1_fwd = float((func(x + h) - func(x)) / h)
    f1_bwd = float((func(x) - func(x - h)) / h)
    f1_cnt = float((func(x + h) - func(x - h)) / (2 * h))

    # Second Order Derivative
    f2_fwd = float((func(x + 2*h) - 2*func(x + h) + func(x)) / (h**2))
    f2_bwd = float((func(x) - 2*func(x - h) + func(x - 2*h)) / (h**2))
    f2_cnt = float((func(x + h) - 2*func(x) + func(x - h)) / (h**2))

    # Third Order Derivative
    f3_fwd = float((func(x + 3*h) - 3*func(x + 2*h) + 3*func(x + h) - func(x)) / (h**3))
    f3_bwd = float((func(x) - 3*func(x - h) + 3*func(x - 2*h) - func(x - 3*h)) / (h**3))
    f3_cnt = float((func(x + 2*h) - 2*func(x + h) + 2*func(x - h) - func(x - 2*h)) / (2 * h**3))

    return {"1st": {"Forward": f1_fwd, "Backward": f1_bwd, "Central": f1_cnt},
            "2nd": {"Forward": f2_fwd, "Backward": f2_bwd, "Central": f2_cnt},
            "3rd": {"Forward": f3_fwd, "Backward": f3_bwd, "Central": f3_cnt}}

# 3. Exact Answers using Sympy
def get_exact_values(expr_func, point_x):
    x_sym = sp.Symbol('x')
    expr = expr_func(x_sym)
    
    # Calculate symbolic derivatives
    d1 = sp.diff(expr, x_sym)
    d2 = sp.diff(d1, x_sym)
    d3 = sp.diff(d2, x_sym)
    
    # Evaluate at point_x
    val1 = float(d1.subs(x_sym, point_x))
    val2 = float(d2.subs(x_sym, point_x))
    val3 = float(d3.subs(x_sym, point_x))
    
    return {"1st": val1, "2nd": val2, "3rd": val3}

# For Output
print(" ")
print("Function : f(x) = 2x^2")
point_x = float(input("Enter point x: "))
step_dx = float(input("Enter step size dx (h): "))

results = calculate_derivatives(my_equation, point_x, step_dx)
exacts = get_exact_values(my_equation, point_x)

for order in ["1st", "2nd", "3rd"]:
    print(f"\n{order} Order Derivative")
    print(f"{'METHOD':<25} | {'RESULT':<15}")
    
    for method, value in results[order].items():
        print(f"{method + ' Difference':<25} | {value:<15.3f}")
    
    print(f"{'Exact Answer':<25} | {exacts[order]:<15.3f}")

print(" ")
