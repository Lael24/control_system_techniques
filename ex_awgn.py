import numpy as np
import matplotlib.pyplot as plt

# Parameters
duration = 1 * 60  # Duration in seconds (10 minutes)
sampling_rate = 1  # Sampling rate in Hz (samples per second)
N = duration * sampling_rate  # Total number of samples

# Generate AWGN
def awgn_nt(mean, st_dev, N):
    """
    Generates Additive White Gaussian Noise (AWGN).

    Parameters:
        mean (float): Mean of the Gaussian distribution.
        st_dev (float): Standard deviation of the Gaussian distribution.
        N (int): Number of samples to generate.

    Returns:
        array: Array containing AWGN samples.
    """
    awgn = np.random.normal(mean, st_dev, N)
    return awgn

mean = 0
st_dev = np.sqrt(0.01)

awgn = awgn_nt(mean, st_dev, N)

# Compute Fourier Transform of AWGN
def compute_ft(awgn):
    """
    Computes the Fourier Transform of a given signal.

    Parameters:
        awgn (array): Input signal.

    Returns:
        array: Fourier Transform of the input signal.
    """
    ft = np.fft.fft(awgn)
    return ft

FourierT_awgn = compute_ft(awgn)

# Plot AWGN and its Fourier Transform
time = np.arange(0, duration, 1/sampling_rate)  # Time array
plt.figure(figsize=(10, 6))
plt.plot(time, awgn, label='AWGN')
plt.plot(time, np.abs(FourierT_awgn), label='Fourier Transform of AWGN')

# Add labels and title
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Additive White Gaussian Noise (AWGN) and its Fourier Transform')
plt.legend()
plt.grid(True)

plt.show()
