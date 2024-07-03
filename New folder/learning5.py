number1 = int(input("Number1:"))
number2 = int(input('Number2:'))
product = number1 * number2
sum = number1 + number2

if product <= 1000:
    print("product:", product)
else:
    print('sum:', sum)

def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2

# first condition
result = multiplication_or_sum(20, 30)
print("The result is", result)
