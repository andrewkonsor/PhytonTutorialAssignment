
#################################################################
## Home Assignment - 3 ##
## Name: type your name here
## Due Date: May 1st, 2019, 11.59 in Blackboard
## Type your answers in this python file and submit in blackboard.
#################################################################

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'
print("hello world")
# Use indexing to print out the following:
# 'd'
print (s[0])
# 'o'
print (s[5])
# 'djan'
print (s[0:4])
# 'jan'
print (s[1:4])
# 'go'
print (s[4:len(s)])
# Bonus: Use indexing to reverse the string
print (s[::-1])

###############
## Problem 2 ##
###############

# Given this nested list:
l = [3, 7, [1, 4, 'hello']]
# Reassign "hello" to be "goodbye"

l[2][2]= 'goodbye'
print (l)
###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key': 'hello'}

d2 = {'k1': {'k2': 'hello'}}

d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}


###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
print (set(mylist))

###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
#"Hello my dog's name is Sammy and he is 4 years old"
print ("Hello my dog\'s name is " + str(name) + " and he is " + str(age) + " years old" )



# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 6 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):
    # CODE GOES HERE
    one = False
    two = False
    three = False

    for x in nums:
        if x==1:
            one = True
        elif x==2:
            two= True
        elif x==3:
            three = True
        if one and two and three:
            return True

    return False

print (arrayCheck ([1, 1, 2, 3, 1]))
print (arrayCheck ([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))


    #####################
    ## -- PROBLEM 7 -- ##
    #####################

    # Given a string, return a new string made of every other character starting
    # with the first, so "Hello" yields "Hlo".

    # For example:

    # stringBits('Hello') → 'Hlo'
    # stringBits('Hi') → 'H'
    # stringBits('Heeololeo') → 'Hello'


def stringBits(str):
  # CODE GOES HERE
  string=str[::2]
  return string

print (stringBits('Hello'))
print (stringBits('Hi'))
print (stringBits('Heeololeo'))
    #####################
    ## -- PROBLEM 8 -- ##
    #####################

    # Given two strings, return True if either of the strings appears at the very end
    # of the other string, ignoring upper/lower case differences (in other words, the
    # computation should not be "case sensitive").
    #
    # Note: s.lower() returns the lowercase version of a string.
    #
    # Examples:
    #
    # end_other('Hiabc', 'abc') → True
    # end_other('AbC', 'HiaBc') → True
    # end_other('abc', 'abXabc') → True


def end_other(a, b):
  # CODE GOES HERE
  sA=a.lower()
  sB=b.lower()
  print (sA)
  print (sB)
  print (str(len(a)))
  print (str(len(b)))
  if len(sA)>len(sB):
      temp = sA[len(sB):len(sA)]
      print (temp)
      return temp == sB 

  else:
      temp = sB[len(sA):len(sB)]
      print(temp)
      return temp == sA
      




print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
    #####################
    ## -- PROBLEM 9 -- ##
    #####################

    # Given a string, return a string where for every char in the original,
    # there are two chars.

    # doubleChar('The') → 'TThhee'
    # doubleChar('AAbb') → 'AAAAbbbb'
    # doubleChar('Hi-There') → 'HHii--TThheerree'


#def doubleChar(str):
  # CODE GOES HERE

    #####################
    ## -- PROBLEM 10 -- ##
    #####################

    # Read this problem statement carefully!

    # Given 3 int values, a b c, return their sum. However, if any of the values is a
    # teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
    # and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
    # takes in an int value and returns that value fixed for the teen rule.
    #
    # In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
    # Define the helper below and at the same indent level as the main no_teen_sum().
    # Again, you will have two functions for this problem!
    #
    # Examples:
    #
    # no_teen_sum(1, 2, 3) → 6
    # no_teen_sum(2, 13, 1) → 3
    # no_teen_sum(2, 1, 14) → 3


#def no_teen_sum(a, b, c):
  # CODE GOES HERE


#def fix_teen(n):
  # CODE GOES HERE

    #####################
    ## -- PROBLEM 11 -- ##
    #####################

    # Return the number of even integers in the given array.
    #
    # Examples:
    #
    # count_evens([2, 1, 2, 3, 4]) → 3
    # count_evens([2, 2, 0]) → 3
    # count_evens([1, 3, 5]) → 0


#def count_evens(nums):
  # CODE GOES HERE


