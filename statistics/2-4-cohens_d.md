[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> To compute Cohen's _d_ for the difference between first baby weights and other baby weights, I separate the baby weights into groups by birth order

```python
import nsfg
import thinkstats2

# Read in NSFG pregnancy data and isolate live births
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

# Identify first babies and separate from others
first_babies = live.loc[live['birthord']==1, 'totalwgt_lb']
other_babies = live.loc[live['birthord']!=1, 'totalwgt_lb']

print('Average first baby weight is {}'.format(first_babies.mean()))
print('Average other baby weight is {}'.format(other_babies.mean()))
```

```
Average first baby weight is 7.201094430437772
Average other baby weight is 7.325855614973262
```

>> To compute the Cohen Effect Size, I used the following function:

```python
import math

# Define calculation for Cohen Effect Size
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()

    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

print('Cohen Effect Size for diff in birth weight is {}'.format(CohenEffectSize(first_babies, other_babies)))
```

```
Cohen Effect Size for diff in birth weight is -0.088672927072602
```

>> While this effect size is small, it is slightly greater than Cohen's _d_ for the difference in pregnancy length between first babies and other babies which is only .029:
```python
# Find Cohen's d for diff in preg lenght for first babies and other babies

# Identify preg length for first babies and separate from others
first_babies = live.loc[live['birthord']==1, 'prglngth']
other_babies = live.loc[live['birthord']!=1, 'prglngth']

print('Average first baby preg length is {}'.format(first_babies.mean()))
print('Average other baby preg length is {}'.format(other_babies.mean()))

print('Cohen Effect Size for diff in preg length is {}'.format(CohenEffectSize(first_babies, other_babies)))
```

```
Average first baby preg length is 38.60095173351461
Average other baby preg length is 38.52291446673706
Cohen Effect Size for diff in preg length is 0.028879044654449883
```



