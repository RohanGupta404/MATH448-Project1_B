import numpy as np


def binomialTree(K, r, sigma, T, S, N):

    t = T / N

    # up and down factors
    u = np.exp(sigma * np.sqrt(t))
    d = 1 / u

    # Risk neutral probability
    probability = ( np.exp(r * t) - d ) / ( u - d )

    # Price of stock at maturity
    ST = [
        S * (u**i) * (d**(N-i)) for i in range(N+1)
    ]

    # Call payoffs
    C_vals = [
        max(s - K, 0) for s in ST
    ]

    # Discount per step
    discount = np.exp(-r * t)

    # Backward induction
    for i in range(N-1, -1, -1):
        for j in range(i+1):

            C_vals[j] = discount * (probability * C_vals[j+1] + (1 - probability)*C_vals[j])


    return C_vals[0]
