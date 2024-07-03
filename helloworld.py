print(4 * 3 / 2 * 2**2)
print(5**2 // 7 == (not (2 // 5 == 5)))
print(3 == 3.0000000000000001)


def count_even(n):
    count = 0
    n1 = list(str(n))
    for i in n1:
        if int(i) % 2 == 0:
            count += 1
    return count


print(count_even(n=(int(input("Num:")))))


#
def count_even(number):
    count = 0
    while number != 0:
        digit = number % 10
        if digit % 2 == 0:
            count += 1
        number //= 10
    return count


for i in range(11):
    print(i, end=" ")

# i+=2
# while i<=9:
#     print("Value of I is:")
# print('moon')
i = 0
while i <= 9:
    print("Value of i is:", i)
    i += 1


def div_or_diff(x, y):
    diff = x - y
    div = x / y
    if div <= 10:
        return f"The result is: {div.__round__(2)}"
    else:
        return f"The result is: {diff}"


result = div_or_diff(x=int(input("Num1:")), y=int(input("Num2:")))
print(result)


def product_of_even_and_odd(n):
    sum_of_even = 0
    sum_of_odd = 0
    for i in range(n):
        if i % 2 == 0:
            sum_of_even += i
        else:
            sum_of_odd += i
    product = sum_of_even * sum_of_odd
    return f"Product is: {product}"


print(product_of_even_and_odd(n=int(input("Num:"))))


def min_value(x, y, z):
    min_value1 = x
    if y < min_value1 and y < z:
        return y
    elif z < min_value1 and z < y:
        return z
    else:
        return min_value1


print(min_value(x=int(input("Num1:")), y=int(input("Num2:")), z=int(input("Num3:"))))


def product_of_even(n):
    product = 1
    for i in range(1, n):
        if i % 2 == 0:
            product *= i
    return product


print(product_of_even(n=int(input("Num:"))))


def exchange_digit(n):
    n1 = list((n))
    n2 = n1[1:]
    n3 = n2 + [n1[0]]
    return int(str(n3))


print(exchange_digit(str(123)))


def exchange_digit(n):
    n1 = list(str(n))
    n2 = n1[1:]
    n3 = n2 + [n1[0]]
    return int("".join(n3))


def exchange_digits(n):
    n1 = list(n)
    n2 = n1[0:-1]
    n3 = [n1[-1]] + n2
    x = "".join(n3)
    return x


print(exchange_digits(str(3245678)))


def is_armstrong_number(num):
    num_str = str(num)
    sum_of_cubes = sum(int(digit) ** 3 for digit in num_str)
    return sum_of_cubes == num


for num in range(0, 1000):
    if is_armstrong_number(num):
        print(num)


def is_armstrong_number(num):
    return sum(int(digit) ** 3 for digit in str(num)) == num


for num in range(1000):
    if is_armstrong_number(num):
        print(num)


def elevator(sequence):
    cur_floor = 0
    for floor in sequence:
        if floor == "^":
            cur_floor += 1
        elif floor == "v" and cur_floor > 0:
            cur_floor -= 1
    return cur_floor


print(elevator("v^vv^"))
txt = input(("Enter a string:"))
if txt == txt[::-1]:
    print("The string is a palindrome")
else:
    print("Not a palindrome")
fruit = "banana"
for i in range(len(fruit)):
    print(fruit[i])


def calculate(a, b):
    print(f"The sum of {a} and {b} is: {a + b}")


print(calculate(3, 4))
#
# age = 21
# first_name = 'Adam'
# print('My name is %sand I am %d'%(first_name, age))

n = 6
for i in range(1, n):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

n = 5
for i in range(n, 0, -1):
    print("*" * i)

n = 5
for i in range(1, n):
    print(" " * (n - i), end="")
    print("* " * i)
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    print("* " * i)

n = 5
for i in range(n - 1):
    for k in range(i, n):
        print(" ", end=" ")
    for k in range(i + 1):
        print("*", end=" ")
    print()
for i in range(n):
    for k in range(i + 1):
        print(" ", end=" ")
    for k in range(i, n):
        print("*", end=" ")
    print()

# Named constants to represent the grade thresholds
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# Get a test score from the user.
score = int(input("Enter your test score: "))

# Determine the grade.
if score >= A_SCORE:
    print("Your grade is A.")
else:
    if score >= B_SCORE:
        print("Your grade is B.")
    else:
        if score >= C_SCORE:
            print("Your grade is C.")
        else:
            if score >= D_SCORE:
                print("Your grade is D.")
            else:
                print("Your grade is F.")
