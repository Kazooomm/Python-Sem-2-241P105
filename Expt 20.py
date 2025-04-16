
import numpy as np

def analyze_array(data):
    data = np.array(data)
    
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data, ddof=1)  # Sample standard deviation
    variance = np.var(data, ddof=1)  # Sample variance
    
    # Correlation requires 2D data (reshape for single variable)
    correlation_matrix = np.corrcoef(np.vstack([data, data]))  # Hack for 1D input
    
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Variance: {variance}")
    print(f"Correlation Coefficients:\n{correlation_matrix}")
    
    return mean, median, std_dev, variance, correlation_matrix

# Example usage
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
analyze_array(data)
