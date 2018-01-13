[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> The distribution of 1000 random values between 0-1 looks pretty evenly distributed and the CDF looks pretty linear at x=y

```python
import random
import thinkstats2
import thinkplot

random_list = []
for i in range(0, 1001):
    random_list.append(random.random())

# plot PMF for 1000 random values between 0-1
random_pmf = thinkstats2.Pmf(random_list)

thinkplot.Hist(random_pmf, width=.001)
thinkplot.Show(xlabel='Random', ylabel='PMF')

# plot CDF for 1000 random values
random_cdf = thinkstats2.Cdf(random_list)

thinkplot.Cdf(random_cdf)
thinkplot.Show(xlabel='Random', ylabel='CDF')
```
