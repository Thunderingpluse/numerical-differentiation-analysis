# Numerical Differentiation Analysis

## Aim
To analyze and compare first and second-order derivatives calculated using Forward, Backward, and Central Finite Difference schemes against analytical solutions across varying step sizes ($h$).

## Theory
Numerical differentiation approximates derivatives of a function using finite difference schemes:

### 1st Order Derivatives
- **Forward Difference ($O(h)$)**: 
  $$f'(x) \approx \frac{f(x+h) - f(x)}{h}$$
- **Backward Difference ($O(h)$)**: 
  $$f'(x) \approx \frac{f(x) - f(x-h)}{h}$$
- **Central Difference ($O(h^2)$)**: 
  $$f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}$$

### 2nd Order Derivatives
- **Forward Difference ($O(h)$)**: 
  $$f''(x) \approx \frac{f(x+2h) - 2f(x+h) + f(x)}{h^2}$$
- **Backward Difference ($O(h)$)**: 
  $$f''(x) \approx \frac{f(x) - 2f(x-h) + f(x-2h)}{h^2}$$
- **Central Difference ($O(h^2)$)**: 
  $$f''(x) \approx \frac{f(x+h) - 2f(x) + f(x-h)}{h^2}$$

The script plots both the calculated derivative values and their relative errors as a function of step size $h$ (from $0.1$ to $1.0$).

## File Structure
- `1_2_order_derivatives.py` - Primary script containing SymPy-based exact calculation, numerical schemes, table generation, and error analysis plotting.
- `v0.py`, `v2.py`, `v3.py` - Alternative development iterations.
- `output.txt` - Text printout containing tabular comparison of derivative values and errors.
- `Figure_1.png` - Visual plot containing four graphs: 1st and 2nd order values and relative errors against step size $h$.

## How to Run
Ensure you have the required dependencies:
```bash
pip install numpy sympy matplotlib
python 1_2_order_derivatives.py
```
