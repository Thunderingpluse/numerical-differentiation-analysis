import math
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# 1. Math Equation
def my_equation(x):
    return 2*x**2

# 2. Calculation Logic
def calculate_derivatives(func, x, h):
    # First Order Derivative
    f1_fwd = (func(x + h) - func(x)) / h
    f1_bwd = (func(x) - func(x - h)) / h
    f1_cnt = (func(x + h) - func(x - h)) / (2 * h)

    # Second Order Derivative
    f2_fwd = (func(x + 2*h) - 2*func(x + h) + func(x)) / (h**2)
    f2_bwd = (func(x) - 2*func(x - h) + func(x - 2*h)) / (h**2)
    f2_cnt = (func(x + h) - 2*func(x) + func(x - h)) / (h**2)

    return {"1st": {"Forward": f1_fwd, "Backward": f1_bwd, "Central": f1_cnt},
        "2nd": {"Forward": f2_fwd, "Backward": f2_bwd, "Central": f2_cnt}}

def get_exact_values(expr_func, point_x):
    x_sym = sp.Symbol('x')
    expr = expr_func(x_sym)
    d1 = sp.diff(expr, x_sym)
    d2 = sp.diff(d1, x_sym)
    return {"1st": float(d1.subs(x_sym, point_x)),"2nd": float(d2.subs(x_sym, point_x))}

# Main Execution
print("\nNumerical Differentiation Analysis")
print("Function: f(x) = 2x^2")
point_x = float(input("Enter evaluation point x: "))
step_h = float(input("Enter step size h: "))

# Single Calculation for Table
res_table = calculate_derivatives(my_equation, point_x, step_h)
exacts = get_exact_values(my_equation, point_x)

# Print Table
for order in ["1st", "2nd"]:
    print(f"\n{order} Order Derivative Table")
    print(f"{'METHOD':<20} | {'RESULT':<12} | {'ERROR':<20}")
    for method, val in res_table[order].items():
        err = val - exacts[order]
        print(f"{method + ' Difference':<20} | {val:<12.3f} | {err:<20.3f}")
    print(f"{'Exact Answer':<20} | {exacts[order]:<12.3f} | {'0.000':<20}")

# Plotting Logic
print("\nGenerating comparison plots")
h_plot = np.arange(0.1, 1.1, 0.1) # Linear range from 0.1 to 1.0

# Storage for plotting
plot_data = {"1st": {"fwd": [], "bwd": [], "cnt": [], "err_fwd": [], "err_bwd": [], "err_cnt": []},
            "2nd": {"fwd": [], "bwd": [], "cnt": [], "err_fwd": [], "err_bwd": [], "err_cnt": []}}

for h in h_plot:
    res = calculate_derivatives(my_equation, point_x, h)
    for order in ["1st", "2nd"]:
        fwd, bwd, cnt = res[order]["Forward"], res[order]["Backward"], res[order]["Central"]
        exact = exacts[order]
        
        plot_data[order]["fwd"].append(fwd)
        plot_data[order]["bwd"].append(bwd)
        plot_data[order]["cnt"].append(cnt)
        
        # If exact is 0, we use absolute error to avoid division by zero
        denom = exact if abs(exact) > 1e-9 else 1.0
        plot_data[order]["err_fwd"].append((exact - fwd) / denom)
        plot_data[order]["err_bwd"].append((exact - bwd) / denom)
        plot_data[order]["err_cnt"].append((exact - cnt) / denom)

# Visual Setup
plt.rcParams['font.family'] = 'times new roman'
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
m_colors = {'fwd': 'C0', 'bwd': 'C1', 'cnt': 'C2'}

# 1st Order Plots
# Top Left: 1st Order Values
axs[0,0].plot(h_plot, plot_data["1st"]["fwd"], 'o-', color=m_colors['fwd'], mfc='white', label='Forward Difference')
axs[0,0].plot(h_plot, plot_data["1st"]["bwd"], 'o-', color=m_colors['bwd'], mfc='white', label='Backward Difference')
axs[0,0].plot(h_plot, plot_data["1st"]["cnt"], 'o-', color=m_colors['cnt'], mfc='white', label='Central Difference')
axs[0,0].set_title("1st Order: Derivative Value vs h", fontweight='bold')
axs[0,0].set_ylabel("f'(x)")
axs[0,0].grid(True, alpha=0.3)
axs[0,0].legend()

# Bottom Left: 1st Order Error
axs[1,0].plot(h_plot, plot_data["1st"]["err_fwd"], 'o-', color=m_colors['fwd'], mfc='white', label='Forward Difference')
axs[1,0].plot(h_plot, plot_data["1st"]["err_bwd"], 'o-', color=m_colors['bwd'], mfc='white', label='Backward Difference')
axs[1,0].plot(h_plot, plot_data["1st"]["err_cnt"], 'o-', color=m_colors['cnt'], mfc='white', label='Central Difference')
axs[1,0].set_title("1st Order: Relative Error vs h", fontweight='bold')
axs[1,0].set_ylabel("Error % (Fraction)")
axs[1,0].set_xlabel("h")
axs[1,0].grid(True, alpha=0.3)
axs[1,0].legend()

# 2nd Order Plots
# Top Right: 2nd Order Values
axs[0,1].plot(h_plot, plot_data["2nd"]["fwd"], 'o-', color=m_colors['fwd'], mfc='white', label='Forward Difference')
axs[0,1].plot(h_plot, plot_data["2nd"]["bwd"], 'o-', color=m_colors['bwd'], mfc='white', label='Backward Difference')
axs[0,1].plot(h_plot, plot_data["2nd"]["cnt"], 'o-', color=m_colors['cnt'], mfc='white', label='Central Difference')
axs[0,1].set_title("2nd Order: Derivative Value vs h", fontweight='bold')
axs[0,1].set_ylabel("f''(x)")
axs[0,1].grid(True, alpha=0.3)
axs[0,1].legend()

# Bottom Right: 2nd Order Error
axs[1,1].plot(h_plot, plot_data["2nd"]["err_fwd"], 'o-', color=m_colors['fwd'], mfc='white', label='Forward Difference')
axs[1,1].plot(h_plot, plot_data["2nd"]["err_bwd"], 'o-', color=m_colors['bwd'], mfc='white', label='Backward Difference')
axs[1,1].plot(h_plot, plot_data["2nd"]["err_cnt"], 'o-', color=m_colors['cnt'], mfc='white', label='Central Difference')
axs[1,1].set_title("2nd Order: Relative Error vs h", fontweight='bold')
axs[1,1].set_ylabel("Error % (Fraction)")
axs[1,1].set_xlabel("h")
axs[1,1].grid(True, alpha=0.3)
axs[1,1].legend()

plt.suptitle(f"Numerical Differentiation Analysis at x = {point_x}\nFunction: f(x) = 2x^2", fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()