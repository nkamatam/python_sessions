## Transforming and Reducing the data at the same time

Problem:

You want to run a function like sum(), min() or max() on a list/tuple but at the same time trasnform the data (filtering rows or midifying the data)

```
# Find the sum of all the odd numbers in the below list
list_1 = [1,2,3,4,5]

```

Solution:
```
# Find the sum of all the odd numbers in the below list
list_1 = [1,2,3,4,5]
sum( x for x in list_1 if x %2 != 0 )

```
One could have used a method like the below, but it is creating an intermediate tuple/list so not efficient.

```
sum(( x for x in list_1 if x %2 != 0) )
```


Problem:
Suppose you have two dictionaries - how to search them one after the other ? Ex: If the key is not found in the dict A, then get it from dict B.

```
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
```

Solution:

```
from collections import ChainMap
c = ChainMap(a,b)
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)

# The advantage of the Chainmap is that it is not creating a new dictionary, it is utilizing the two underlying dictionaries.


```


Problem:

Splitting a line of text based on a delimeters or based on a complex regex.


line = 'asdf fjdk; afed, fjek,asdf, foo'

How do we split the line based on a space or a comma or a semicolon?


Solution:

```
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
re.split(r'[;,\s]\s*', line)


```
Strings also have the split function, but re.split is obviously more powerful and used for more complex needs
