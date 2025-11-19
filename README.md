# Math 448 Project 1 B — Option Pricing

## How to Run
To reproduce all results for the project, run:

python `main.py`

Make sure all Python files are in the same directory.

The project is organized into three files:
- `main.py`
- `BlackScholes.py`
- `binomialTree.py`

---

## Black–Scholes Formula

To use the Black–Scholes pricing function, ensure `BlackScholes.py` is in the same directory.

Example:

```python
import BlackScholes
BlackScholesResult = BlackScholes.blackscholes(S, K, r, sigma, T)
```

Parameters:
- `S` — Current stock price
- `K` — Strike price
- `r` — Risk-free interest rate
- `sigma` — Volatility
- `T` — Time to maturity

---

## Binomial Tree

To use the binomial tree implementation, ensure `binomialTree.py` is in the same directory.

Example:

```python
import binomialTree
BinomialResult = binomialTree.binomialTree(K, r, sigma, T, S, N)
```

Parameters:
- `K` — Strike price
- `r` — Risk-free interest rate
- `sigma` — Volatility
- `T` — Time to maturity
- `S` — Current stock price
- `N` — Number of time steps

---

## Requirements

Install required libraries using:

```
pip install -r requirements.txt
```

`requirements.txt` contains:

```
numpy
pandas
matplotlib
ipython
```

---

## Output

Running `main.py` will:
- compute binomial tree prices for multiple values of N
- compute Black–Scholes prices
- calculate absolute errors
- perform the log–log regression for the convergence rate
- generate plots using matplotlib
