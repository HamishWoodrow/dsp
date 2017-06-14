# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists can display any type of data (strings, ints, floats, lists), this attribute is shared with tuples which can also contain any data type.  However, lists are mutable and tuples are immutable (meaning they cannot be altered).  Tuples are defined by key value pairs where lists are defined by indexes. 
Tuples would be used as keys in dictionaries, since each tuple contains two values the key which references the data (value/s).


---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are unordered collections of elements, lists are ordered collections of elements.  Sets cannot contain duplicate elements, each element is unique.  This is not the case for lists.  Sets are also unordered collections of data, whereas lists keep order.  Lists and sets are similar in the fact that they can contain integers, strings in the elements and they are used to hold data.  
Sets are used often in eliminating duplicates and for comparisons of data sets where the objective is to see common elements between two collections.  Sets are faster when looking for values and finding if a particular element is a member of the data set.
Lists are often used where order is important and there is an interest is storing all data even if it is non-unique, often lists are used where we need to iterate over the values.  They are great for storing data and iterating through it.

'''python
#Example of a set:
>>>cities = {'New York', 'London', 'Bombay', 'Tokyo'}
>>>'New York' in basket
True

#Example of a list:
>>>lsa=[1, 2, 2, 3, 3, 9, 421, 3425]
>>>lsa.sort()
>>>print (lsa)
[1, 2, 2, 3, 3, 9, 421, 3425]

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lamda is an annonymous function, which does not need defined separately and can be temporarily defined.  They are oftern useful when a quick function is required for single operations.  This can lead to a more readable and compact code.  It is often used in conjunction with filter, map, reduce.  In order to feed functions (generating conditions) to the expressions to manipulate lists.

'''python
sorted(['hippo','chicken','ox','lamb','horse'], key=lambda x: (x!='ox',x))
'''

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are very succinct ways to generate and transform lists, from a single expression allowing for conditions and loops to be used, much in the same way that mathematical sets are written out.

'''python
#examples of list comprehension
>>>[i**2 for i in range(21) if i%2 == 0] #prints the square of even numbers
#example with map and filter
>>>ev_sq=list(map(lambda x: x**2,list(filter(lambda x: x%2==0,range(21)))))
'''

Due to the use of Lambda the map method can be less efficient, but one of the main advantages of list comprehension is also how it is much clearer.



---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 DAYS

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 DAYS

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

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





