# CodeAbbey

## Minimum of Three

Main trick here is how to choose minimum efficiently.

Many solutions use 6 comparisons, like "if a < b and a < c then a is min" repeated three times for each variable. This looks bit too clumsy.

Simple and clear approach is to use additional variable:

```c
min=a;
if(min>b)
    min=b;
if(min>c)
    min=c;
// output min
```

We can even do without temporary variable as a matter of fact:

```c
if (a < b)
    b = a;
if (b < c)
    c = b;
// output c
```

## Rounding

```python
if abs(result - int(result)) >= 0.5:
    if result > 0:
        result = int(result) + 1
    else:
        result = int(result) - 1
else:
    result = int(result)
```
