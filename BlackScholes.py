import numpy as np


def phi(x):

    # Abramowitz Stegun approximation constants
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    p = 0.3275911

    sign = 1
    if x < 0:
        sign = -1
    x = abs(x) / np.sqrt(2.0)

    t = 1.0 / (1.0 + p*x)
    y = 1.0 - (((((a5 * t + a4) * t + a3) * t + a2) * t + a1) * t) * np.exp(-x * x)

    return 0.5 * (1.0 + sign * y)


def blackScholes(S, K, r, sigma, T):

    d1 = (np.log(S/K) + (r + (sigma**2)/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    C = S*phi(d1) - K * np.exp(-r*T) * phi(d2)

    return C

