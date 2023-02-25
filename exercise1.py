# -*- coding: utf-8 -*-
"""
The program should print two roots of the quadratic equation of the form

a x² + b x + c = 0

The roots must be stored in a tuple named 'solutions' and printed at the very end of the program.
"""

# This is sample input data

a = 1
b = 3
c = 2

# This is a tuple for results. You should override it with actual results

solutions = ()

# DO NOT CHANGE ANYTHING ABOVE THIS LINE!!!


# Put your code here...
if a == 0:
    x = -c/b
    solutions = (x, )
else:
    D = b**2 - 4*a*c 
    if D == 0:
        x = -b/(2*a)
        solutions = (x, )
    elif D > 0:
        x1 = (-b + D**0.5)/(2*a)
        x2 = (-b - D**0.5)/(2*a)
        solutions = (x1, x2)

# At the end, the results are printed to the screen
print(solutions)
