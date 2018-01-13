[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

*Question:*
In the BRFSS (see Section 5.4), the distribution of heights is
roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and
µ = 163 cm and σ = 7.3 cm for women.

In order to join Blue Man Group, you have to be male between 5’10” and
6’1” (see http://bluemancasting.com). What percentage of the U.S. male
population is in this range? Hint: use scipy.stats.norm.cdf.


>> If the distribution of heights for men is normal (with a mean of 178cm and std of 7.7cm) then we can find the percentage of males with heights between 5'10'' and 6'1'' with the following code:

```python
import scipy.stats

# Find the normal cdf for a dataset with average value of 178cm and std of 7.7cm
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
dist_cdf = dist.cdf(mu-sigma)

upper = 185.42000000000002 # 6'1'' converted to cm
lower = 177.8 # 5'10'' converted to cm

# Find P(X<upper)
upper_p = scipy.stats.norm.cdf(x=upper,loc=mu,scale=sigma)
print("Percentage with height less than 6'1'': {}".format(upper_p))

# Find P(X<lower)
lower_p = scipy.stats.norm.cdf(x=lower,loc=mu,scale=sigma)
print("Percentage with height less than 5'10'': {}".format(lower_p))

print("Percentage of men between 5'10'' and 6'1'': {}".format(upper_p - lower_p))
```

```
Percentage with height less than 6'1'': 0.8323858654963072
Percentage with height less than 5'10'': 0.48963902786483265
Percentage of men between 5'10'' and 6'1'': 0.34274683763147457
```

>> We find in the above solution that we could expect roughly 34.27% of U.S. males to be between 5'10'' - 6'1''