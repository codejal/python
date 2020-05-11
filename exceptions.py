'''except ValueError as msg:
    print("not valid value")
    print(msg)
except ZeroDivisionError:
    print("age cannot be zero")'''

from timeit import timeit
try:
    file = open("py.py")
    age = int(input("age: "))
    x = 10/age
except (ValueError, ZeroDivisionError):
    print("age cannot be zero")
else:
    print("no exception find")
finally:
    file.close()
# for multiple error python will run the first
# except block respective to error


# withs as code closes fliexternal links as soon as it is left
try:
    with open("py.py") as file, open("py2.py") as target:  # open multiple file
        print("fileopened")
    age = int(input("age: "))
    x = 10/age
except (ValueError, ZeroDivisionError):
    print("age cannot be zero")
else:
    print("no exception find")


# raising error
def xfac(age):
    if age <= 0:
        raise ValueError("age cant be 0 or less")
    return 10/age


try:
    xfac(-2)
except ValueError as err:
    print(err)
# error raising has cost of time
code1 = """
def xfac(age):
    if age <=0:
        raise ValueError("age cant be 0 or less")
    return 10/age

try:
    xfac(-2)
except ValueError as err:
    pass    
"""

code2 = """
def xfac(age):
    if age <=0:
        return None
    return 10/age

x=xfac(-2)
if x== None:
    pass
"""

print("code1=", timeit(code1, number=10000))
print("code2=", timeit(code2, number=10000))
'''
code1= 0.11394510000000224
code2= 0.05537010000000109
we can see that raising error slows the code almost twice the time '''
