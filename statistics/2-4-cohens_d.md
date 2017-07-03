[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

```python
"""To compute the Cohen's d we will need to pool the variations,
the means are already calculated, this will need to calculate the variations"""
import math as math

var_wt_first = firsts.totalwgt_lb.var()
var_wt_other = others.totalwgt_lb.var()
first_n = len(firsts.totalwgt_lb)
other_n = len(others.totalwgt_lb)

pooled_var = (first_n*var_wt_first + other_n*var_wt_other)/(first_n+other_n)
pooled_std = math.sqrt(pooled_var)

d = (mean_wt_first-mean_wt_other)/pooled_std

print ('The Cohen\'s d for baby weights between first born and others is:', round(d,4))
```

>>The Cohen's d for baby weights between first born and others is: -0.0887
