# 1. What is the expected output of the following python code given?

data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter (lambda x: x>4, data)
print(list(result))

# 2. Write a python code using lambda function to check every element of a list is an integer of string?

check_elements = lambda lst: all(map(lambda x: isinstance(x, (int, str)), lst))

# Example usage
my_list = [1, 'guvi', 5, 'zen', '36']
result = check_elements(my_list)

if result:
    print("All elements are either integers or strings.")
else:
    print("There are elements that are not integers or strings.")

# 3. Using python Lambda function create a Fibonacci series of 1 to 50 elements?
    
def fibonacci(count):
    fib_list = [0, 1]
 
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
                                         range(2, count)))
 
    return fib_list[:count]
 
print(fibonacci(50))

# 4. Write a python function to validate the regular expressions of the following-
# a. Email Adress 
# b. Mobile numbers of Bangladesh 
# c. Telephone numbers of USA 
# d. 16 charecters Alpha-Numeric password composed alphabets of Upper case, Lower case, Special charecters, Numbers.

import re

def validate_email(email):
   if "@" not in email:
    return False
   if "." not in email:
    return False
    local_part, domain_name = email.split("@")

    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]*$", local_part):
     return False

    if not re.match(r"^[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]*$", domain_name):
     return False

    return True