# In this notebook, we focus on solving the following problem:
#
# QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in
# decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the
# card containing a given number by turning over as few cards as possible. Write a function to help
# Bob locate the card.


# ## The Method
#
# Upon reading the problem, you may get some ideas on how to solve it and your
# first instinct might be to start writing code. This is not the optimal strategy, and
# you may end up spending a longer time trying to solve the problem due to coding errors,
# or may not be able to solve it at all.
#
# Here's a systematic strategy we'll apply for solving problems:
#
# 1. State the problem clearly. Identify the input & output formats.
# 2. Come up with some example inputs & outputs. Try to cover all edge cases.
# 3. Come up with a correct solution for the problem. State it in plain English.
# 4. Implement the solution and test it using example inputs. Fix bugs, if any.
# 5. Analyze the algorithm's complexity and identify inefficiencies, if any.
# 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
#
# _"Applying the right technique"_ is where the knowledge of common data structures and algorithms comes in handy.


# ## Solution
#
#
# ### 1. State the problem clearly. Identify the input & output formats.
#
# You will often encounter detailed word problems in coding challenges and interviews.
# The first step is to state the problem clearly and precisely in abstract terms.
#
# <img src="https://i.imgur.com/mazym6s.png" width="480">
#
# In this case, for instance, we can represent the sequence of cards as a list of numbers.
# Turning over a specific card is equivalent to accessing the value of the number at the
# corresponding position the list.

# The problem can now be stated as follows:
#
# #### Problem
#
# > We need to write a program to find the position of a given number in a
# list of numbers arranged in decreasing order. We also need to minimize the number of times we access
# elements from the list.
#
# #### Input
#
# 1. `cards`: A list of numbers sorted in decreasing order. E.g. `[13, 11, 10, 7, 4, 3, 1, 0]`
# 2. `query`: A number, whose position in the array is to be determined. E.g. `7`
#
# #### Output
#
# 3. `position`: The position of `query` in the list `cards`. E.g. `3` in the above case (counting from `0`)
#
#
#
# Based on the above, we can now create the signature of our function:

# pass statement do nothing in the body
def locate_card(cards, query):
    pass


# **Tips**: Interviewer will look for
#
# * Name your function appropriately and think carefully about the signature
# * Discuss the problem with the interviewer if you are unsure how to frame it in abstract terms
# * Use descriptive variable names, otherwise you may forget what a
# variable represents


# ### 2. Come up with some example inputs & outputs. Try to cover all edge cases.
#
# Before we start implementing our function, it would be useful to come up with some example
# inputs and outputs which we can use later to test out problem. We'll refer to them as *test cases*.
#
# Here's the test case described in the example above.

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3

# We can test our function by passing the inputs into function and comparing the result with the expected
# output.

result = locate_card(cards, query)
print(result)

print(result == output)
# Obviously, the two result does not match the output as we have not yet implemented the function.
#
# We'll represent our test cases as dictionaries to make it easier to test them once we write implement our function.
# For example, the above test case can be represented as follows:
test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}
