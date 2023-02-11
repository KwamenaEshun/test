print ("Hi")


# 004
# Write a function that takes
# two strings as input and returns their concatenation.


def two_strings():
  first_string= str(input("enter the 1st string: "))
  second_string= str(input("enter the 2nd string: "))
  concatenation= first_string +" "+ second_string
  return f"The concatenation is {concatenation}."

print(two_strings())




# 005
# Write a function that takes
# a number as input and returns its factorial.

#def factorial_num():
#  num= float(input("enter the number: "))
#  factorial=[num*(num-1) + 1] - 9
 # return f"The factorial is {factorial}."

# print(factorial_num())






# 006
# Write a function that
# takes a string as input and returns the first character.



def return_char():
  string= str(input("enter the string: "))
  first_char= string[0]
  return f"the first character is {first_char}"

print(return_char())




# 008
# Write a function that takes
# a string as input and returns the last character.



def return_char():
  string= str(input("enter the string: "))
  last_char= string[-1]
  return f"the last character is {last_char}"

print(return_char())