import numpy as np
import matplotlib.pyplot as plt

# Define function to compute L matrix
def L_matrix(h):
    """
    Computes the L matrix based on the given heights.
    
    Parameters:
        h (array): Array containing heights.
        
    Returns:
        array: L matrix computed based on the heights.
    """
    # Initialize L as a 3xN array, where N is the length of h
    L = np.zeros((3, len(h)))
    
    for i in range(len(h)):
        if h[i] <= 1750:
            # For h < 1750, L has specific values
            L[:, i] = np.array([h[i], 145 * h[i]**(1/3), 145 * h[i]**(1/3)])
        else:
            # For h >= 1750, L has values of 1750
            L[:, i] = np.array([1750, 1750, 1750])
    return L

# Define h array
h = np.arange(0, 20000 + 1)  # From 0 to 20000 ft

# Compute L matrix
L = L_matrix(h)

# Plot L matrix components
plt.figure(figsize=(10, 6))

# Plot each row of L
for i in range(3):
    plt.plot(h, L[i, :], label=f'L[{i+1},:]')

# Add labels and title
plt.xlabel('Height (ft)')
plt.ylabel('Values')
plt.title('L Matrix Components vs. Height')
plt.legend()
plt.grid(True)
plt.ylim(0, 2000)  # Limit y-axis for better visualization
plt.xlim(0, 2500)  # Limit x-axis for better visualization

plt.show()


