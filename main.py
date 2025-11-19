
import binomialTree
import BlackScholes
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.display import display

# Pre Defining variables for ease of use
K = 10
r = 0.02
sigma = 0.25
T = 0.25
S = 10


# Question 1.a: Running Binomial Tree using different values of N to compute C

N = [
    10,
    100,
    1000,
    10000
]

binomialTree_solutions = [
    binomialTree.binomialTree(K, r, sigma, T, S, n) for n in N
]

print("Question 1.A")
print("The Binomial Tree Solutions")
for i in range(len(N)):
    print(f"For N: {N[i]}, BTS: {binomialTree_solutions[i]}")

# Question 1.b Using Black Scholes formula to compute the price C

blackScholes_solution = BlackScholes.blackScholes(S, K, r, sigma, T)


print("\n\nQuestion 1.B")
print(f"The Black Scholes Formula Solution: {blackScholes_solution}")

# Question 1.c Creating a Table E, that represents the difference between
# results of binomial tree and black scholes results

E = [
    [n for n in N],
    [bts for bts in binomialTree_solutions],
    [abs(bts - blackScholes_solution) for bts in binomialTree_solutions]
]

error_df = pd.DataFrame()
error_df["Number of Timesteps"] = E[0]
error_df["Binomial Tree Solution"] = E[1]
error_df["Error (|E|)"] = E[2]

print("\n\nQuestion 1.C")
display(error_df)


# Question 1.d plotting ln|E| vs ln N
lnE = np.log(np.array(E[2], dtype=float))
lnN = np.log(np.array(N, dtype=float))

A, B = np.polyfit(lnN, lnE, 1)


print("\n\nQuestion 1.D")
print(f"ln|E| = {A} * ln N + {B}")
print(f"where,")
print(f"    A = {A}")
print(f"    B = {B}")

plt.plot(lnE, lnN)
plt.xlabel("ln|E|")
plt.ylabel("ln N")
plt.title("Question 1.D:  ln|E| vs ln N")
plt.show()

# Question 1.e Finding the Convergence rate

print("\n\nQuestion 1.E")
print("Regression (ln|E| vs ln N):")
print(f"ln|E| ≈ {A} * ln N + {B}")
print(f"Convergence rate ≈ {-A} (that is, |E| ~ N^({A}))")