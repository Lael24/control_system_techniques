"""
Title: Understanding Binomial Normalization in Python

Description:
Binomial normalization is a statistical technique used to adjust probabilities in binomial distributions, particularly in cases where there might be uncertainty or prior knowledge influencing the outcomes. In this script, we implement a Python function to perform binomial normalization and demonstrate its application.

"""

# Define the binomial normalization function
def bin_norm(H, N, p_B, pH_B):
    """
    Calculate binomial normalization.

    Parameters:
    - H: Number of successes
    - N: Total number of trials
    - p_B: Probability of event B
    - pH_B: Probability of H given B

    Returns:
    - Normalized probability
    """

    # Calculate the complement probability of event B
    p_notB = 1. - p_B
    # Calculate the number of failures
    T = N - H
    # Calculate the complement probability of H given B
    pT_B = 1. - pH_B
    
    # Calculate the normalized probability using the binomial normalization formula
    return (
        (pH_B ** H * pT_B ** T * p_B)
        / ((pH_B ** H * pT_B ** T * p_B) + ((.5 ** N) * p_notB))
    )

# Example usage
exp1 = bin_norm(33, 50, 1/100, .6)  # Calculate normalized probability with initial parameters
print("Normalized probability (exp1):", exp1)

exp2 = bin_norm(33, 50, 0.0853, .6)  # Calculate normalized probability with updated parameters
print("Normalized probability (exp2):", exp2)

"""
Explanation:
- The bin_norm function takes four parameters: H (number of successes), N (total number of trials), p_B (probability of event B), and pH_B (probability of H given B).
- Inside the function, we first calculate the complement probabilities and the number of failures.
- Then, we apply the binomial normalization formula to compute the normalized probability.
- In the example usage, we demonstrate how to use the function to calculate normalized probabilities for two scenarios: exp1 and exp2.
- By adjusting the parameters, we can see how the normalized probability changes, reflecting our updated beliefs or knowledge about the system.
"""

