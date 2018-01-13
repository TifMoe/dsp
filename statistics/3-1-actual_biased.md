[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> When we look at the actual distribution of the number of children in each family we see that the actual mean # of children is just over 1 child per family

```python
import nsfg
import thinkstats2

resp = nsfg.ReadFemResp()

# Find the actual mean # of kids in a list of respondent households
num_kids = resp['numkdhh']

num_kid_pmf = thinkstats2.Pmf(num_kids, label = 'actual')
print('Unbiased Pmf: \n{}'.format(num_kid_pmf))
print('The unbiased mean is {}'.format(num_kid_pmf.Mean()))
```

```
Unbiased Pmf:
Pmf({0: 0.46617820227659301, 1: 0.21405207379301322, 2: 0.19625801386889966, 3: 0.087138558157791451, 4: 0.025644380478869556, 5: 0.010728771424833181})
The unbiased mean is 1.024205155043831
```

>> If we were to have surveyed children under the age of 18 to find this distribution, it would have been biased to artificially inflate the representation of larger families and completely exclude families with no children.
>> This biased distribution has an increased mean of 2.4 children per family compared with the actual mean of 1.0
```python
from statistics import mean

# Find the biased mean # of kids in a list of respondent households
def BiasedDict(pdf):
    biased_pdf = {}

    for x, y in pdf.Items():
        biased_pdf[x] = y*x

    return biased_pdf

biased_num_kids = thinkstats2.Pmf(BiasedDict(num_kid_pmf), label = 'observed')
print('Biased Pmf: \n{}'.format(biased_num_kids))
print('The biased mean is {}'.format(biased_num_kids.Mean()))
```

```
Biased Pmf:
Pmf({0: 0.0, 1: 0.20899335717935616, 2: 0.38323965252938175, 3: 0.25523760858456823, 4: 0.10015329586101177, 5: 0.052376085845682166})
The biased mean is 2.403679100664282
```

>> We can plot both the biased and actual distribution of number of children with the code below:
```python
import thinkplot

thinkplot.PrePlot(2)
thinkplot.Pmfs([num_kid_pmf, biased_num_kids])
thinkplot.Show(xlabel='number of children', ylabel='PMF')
```

