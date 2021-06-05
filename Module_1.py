# Module 1 - Thory Of computation Project
# Mina Isaac - Mina Ezzat - Fady Fawzy
# -----------------------------------------------------------------
# libraries Of Project

import rstr
import re

#  Enter Regular expression
regular_expression = input("Enter Correct Regular Expression :\n")

#  print strings that accepted From this Regular Expression
print("Examples for regex :\n",rstr.xeger(regular_expression))

#  check string acceptance
print("\n To check string acceptance Press [ y ] \n")
check_string = input()

# check if the string accepted or not
if check_string == 'y':

        string=input("Enter A string To check:\n")

        if re.fullmatch(regular_expression,string):
            print("String is accepted")
        else:
            print ("String is not accepted")
