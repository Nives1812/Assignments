#!/usr/bin/env python
# coding: utf-8

# 1.What are the two values of the Boolean data type? How do you write them?
# 
# True and False are the only two values of Boolean data type. We write them as True and False with capital t and F at the start. We can use the Boolean datatype using comparison operation and logic operation. True is equal to 1 and False = 0

# In[ ]:


get_ipython().set_next_input('2. What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')
And, or, not are the three types of Boolean operators.


# In[ ]:


3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

Value 1 (V1)	Value 2(V2)	Boolean operator (AND) – V1 AND V2
True	True	True
True	False	False
False	True	False
False	False	False

Value 1 (V1)	Value 2(V2)	Boolean operator (OR) – V1 AND V2
True	True	True
True	False	True
False	True	True
False	False	False

Value 1 (V1)	Boolean operator (NOT) – V1 
True	False
False	True


# In[ ]:


get_ipython().set_next_input('4. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')

(5 > 4) and (3 == 5) - False
not (5 > 4) - False
(5 > 4) or (3 == 5)- True
not ((5 > 4) or (3 == 5)) - False
(True and True) and (True == False) -  False
(not False) or (not True) - True


# In[ ]:


get_ipython().set_next_input('5. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')

< (less than)
> (greater than)
== (equal to)
get_ipython().system('= (not equal to)')
<= (less than or equal to)
>= (greater than or equal to)


# In[ ]:


6. How do you tell the difference between the equal to and assignment operators? Describe a condition and when you would use one.

Equal is a comparison operator.  A condition to check if a is equal to b we use comparison operator. It returns true if comparison is correct and false when comparison is not correct.
A = 5
B = 8
Print (A == B)
Output: False
Assignment operators assigns the value to the variable like in the below example. A +=5. In this assignment the value of 5 is added to the variable a and assigned back to the variable itself. If a is 10, 5 gets added and the new of value of a is assigned as 15.


# In[ ]:


7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')

Ans: print (‘eggs’), print(‘bacon’) and print(‘ham’)  are the three blocks in the given code.


# In[ ]:


8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

spam = int(input())
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings')


# In[ ]:


get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')

We can use the interrupt the kernel button (with stop symbol). We can also use Ctrl + C.


# In[ ]:


get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')

The break statement terminates all the iteration in a loop and exits the loop
The continue skips the current iteration in the loop and does not exit the loop.


# In[ ]:


11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

All three conditions will return the same output from 0 to 9. The difference is in the way the range function is represented. 
Range (10) has the stop value as 10 with the start value as 0 and interval as 1 by default.
Range (0,10) has the start and stop value assigned as 0 and 10 respectively with interval of 1 between values.
Range (0,10,1) has the start and stop value assigned as 0 and 10 respectively with the interval of 1 between each value in the range.


# In[ ]:


12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

Using for loop:
for a in range(1,10+1):
    print (a)

Using while loop:
a = 1
while (a <= 10):
    print (a)
    a+=1


# In[ ]:


get_ipython().set_next_input('13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')

Import spam():
spam.bacon()

or

from spam import bacon()

