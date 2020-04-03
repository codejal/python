def fizz_buzz(number):
    if number % 3 == 0 and number % 5 != 0:
        return "fizz"
    if number % 3 != 0 and number % 5 == 0:
        return "buzz"
    if number % 3 == 0 and number % 5 == 0:
        return " fizz buzz"
    else:
        return number


number = int(input("enter the number : "))
print(fizz_buzz(number))
