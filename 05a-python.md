# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples contain an ordered sequence of values such that the values can be identified by the index. They also both allow for duplicated values in their sequence. However, lists are mutable and can be altered while tuples are immutable. Because tuples cannot be altered, they will work as keys in a dictionary while lists do not. 

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both lists and sets contain a sequence of values however lists contain a mutable ordered sequence of values which can contain duplicate values whereas sets contain unordered immutable sequences of values that do not include duplication.

>> #### List Examples

>> For example, you can use a list to store the names of drinks Brittney purchased from Starbucks in October like:
```python
>>> list_oct_orders = ['pumpkin_spice_latte', 'pumpkin_spice_latte', 'pumpkin_spice_latte', 'coffee', 'pumpkin_spice_latte']

>>> print(list_oct_orders)
['pumpkin_spice_latte', 'pumpkin_spice_latte', 'pumpkin_spice_latte', 'coffee', 'pumpkin_spice_latte']
```
>> To find the first order in the above list, you can retreive the element at index 0
```python
>>> print(list_oct_orders[0])
'pumpkin_spice_latte'
```
>> #### Set Examples
>> But if you were only interested in the distinct types of drinks Brittney ordered in October, you could make a set of the above list like:
```python
>>> set_oct_orders = set(list_oct_orders)

>>> print(set_oct_orders)
set(['coffee', 'pumpkin_spice_latte'])
```
>> In the set above you can't retrieve Britteny's first order like we did in the list because it is an unordered sequence of unique values and doesn't support indexing. If you're only interested in finding drinks contained in either a list or set of Brittney's orders then searching elements in a set is slightly more performant. 

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's `lambda` is an operator for building anonymous functions in a single line. This can be helpful when a simple/short function is needed once. For example, if you wanted to create a function to check if a list of drink orders contains a pumkin spice latte, you could use the following:
```python
>>> ordered_psl = lambda x: 'Oh yay!' if 'pumpkin_spice_latte' in x else 'Nope...'

>>> print(ordered_psl(list_oct_orders))
Oh yay!
```

>> Say you had the following list of tuples with all your friend's favorite fall drinks and wanted to sort them
```python
>>> friends_favs = [('Brit','pumpkin_spice_latte'), ('Correy','coffee'), ('Anne','green_tea')]

>>> print(friends_favs)
[('Brit','pumpkin_spice_latte'), ('Correy','coffee'), ('Anne','green_tea')]
```
>> If you call the `sorted()` function on this list as is, you will find the tuples have been sorted by your friend's names (or, the 0 index in the tuple)
```python
>>> print(sorted(friends_favs))
[('Anne', 'green_tea'), ('Brit', 'pumpkin_spice_latte'), ('Correy', 'coffee')]
```
>> But if you pass a lambda expression into the `key` argument of the `sorted` function, you can specify that you want to sort the list of tuples on the second element (the fav drinks!)
```python
>>> print(sorted(friends_favs, key=lambda x: x[1]))
[('Correy', 'coffee'), ('Anne', 'green_tea'), ('Brit', 'pumpkin_spice_latte')]
```
---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions let you create a new list by iterating over a sequence of values and perform some sort of transformation or computation on every element that meets the filter criteria.

>> So since I'm already leaning hard into this Starbucks drinks motif, I'm just going to keep going with it :smirk: :coffee: We have our list of our friends favorite drinks above, but say we wanted to loop through all of them to see if they were seasonal drinks or not. We could first create a set with all the seasonal drinks we want to check against:
```python
>>> seasonal_drink_set = {'pumpkin_spice_latte', 'peppermint_latte', 'gingerbread_latte'}

>>> print(friends_favs) # As a reminder of our list of friend's fav drinks
[('Brit', 'pumpkin_spice_latte'), ('Correy', 'coffee'), ('Anne', 'green_tea')]
```

>> #### List Comprehensions
>> We could then use a list comprehension to iterate over our list of friend favs to create a new list of the drinks that are not seasonal drinks:
```python
>>> non_seasonal_favs = [x[1] for x in friends_favs if x[1] not in seasonal_drinks]

>>> print(non_seasonal_favs)
['coffee', 'green_tea']
```
>> An equivalent operation using `map` and `filter` might be:
```python
>>> print(list(map(lambda x: x[1], filter(lambda y: y[1] not in seasonal_drinks, friends_favs))))
['coffee', 'green_tea']
```

>> #### Set Comprehensions
>> We can basically do the same computation above but store the output as a set instead of a list:
```python
>>> set_comprehension_example = {x[1] for x in friends_favs if x[1] not in seasonal_drinks}

>>> print(set_comprehension_example)
{'coffee', 'green_tea'}
```

>> #### Dictionary Comprehensions
>> Similarly, we can create a dictionary using a dictionary comprehension if we wanted to store our friend's names with their non-seasonal fav drinks:
```python
>>> dict_comprehension_example = {x[0]:x[1] for x in friends_favs if x[1] not in seasonal_drinks}

>>> print(dict_comprehension_example)
{'Anne': 'green_tea', 'Correy': 'coffee'}
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





