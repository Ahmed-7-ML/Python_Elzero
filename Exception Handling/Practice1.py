#                    Exercise 1: Handling ZeroDivisionError                        #
# Imagine you have two numbers and
# want to determine what happens when you divide one number by the other.
# To do this, you need to create a Python function called safe_divide. 
# You give this function two numbers, a 'numerator' and a 'denominator'.
# The 'numerator' is the number you want to divide,and the
#'denominator' is the number you want to divide by.
# Use the user input method of Python to take the values.

# The function should be able to do the division for you and give you the result.
# But here's the catch: if you try to divide by zero (which is not allowed in math), 
#the function should be smart enough to catch that and 
# tell you that it's not possible to divide by zero. Instead of showing an error, 
# it should return None,
#  which means 'nothing' or 'no value', and print "Error: Cannot divide by Zero.


def safe_divide(a,b):
    try:
        a = a/b
        return a
    except ZeroDivisionError:
        print("Error: Cannot divide by Zero")
        return None



a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))
print(safe_divide(a,b))