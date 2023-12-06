# one sample t - test

def one_sample_t_test():
    import numpy as np
    from scipy import stats
    # Population Mean
    mu = 10
    # Sample Size
    N1 = 21
    # Degrees of freedom
    dof = N1 - 1
    # Generate a random sample with mean = 11 and standard deviation = 1
    x = np.random.randn(N1) + 11
    # Using the Stats library, compute t-statistic and p-value
    t_stat, p_val = stats.ttest_1samp(a=x, popmean = mu) 
    print("t-statistic = " + str(t_stat))
    print("p-value = " + str(p_val))
    if p_val<0.05:
        print("Reject null hypo")
    else:
        print("Retain null hypo") 

def two_sample_t_test():
    # Sample Sizes
    N1, N2 = 21, 25
    # Degrees of freedom
    dof = min(N1,N2) - 1
    # Gaussian distributed data with mean = 10.5 and var = 1
    x = np.random.randn(N1) + 10.5
    # Gaussian distributed data with mean = 9.5 and var = 1
    y = np.random.randn(N2) + 9.5
    ## Using the internal function from SciPy Package
    t_stat, p_val = stats.ttest_ind(x, y)
    print("t-statistic = " + str(t_stat))
    print("p-value = " + str(p_val))
    if p_val<0.05:
        print("Reject null hypo")
    else:
        print("Retain null hypo")