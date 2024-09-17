# username: str = input('user name')
# password: str = input('password')
# password_len = len(password)
# hidden_password = '*' * len(password)
# print(f'{username} , your password {hidden_password} is {len(password)} letters long ')

# print(list(range(3)))

# new_sentence = ' '.join(['hi ','my ','name ','is ','Mike.'])
#
# print(new_sentence)

# basket = [1,2,3,4]
# a,s,*other,e = [1,2,3,4,7,8,6]
# print(a)
# print(s)
# print(other)
# print(e)

# weapons = None
# print(weapons)
# dictionary = ({"a": [1, 3, 5], "b": 2, "c": 3}, {(2, 3, 4): [1, 3, 5], True: 2, "c": 3})
# print(dictionary[0]["a"][::2])
# i = int(input("Enter the number\n"))
# if i % 2 == 0:
#     print("Num is even")
# else:
#     print("Num is odd")
# for i in range(10):
#     a = 243
#     print(i * a)
# fruits = ["apple", "banana", "mango"]
# print(list(fruits[1]))
# print(type(fruits))
from math import pi


def print_circum(r):
    circum = 2 * pi.__round__(5) * r
    print(f"The circemference of the circlre for which the given radus is {circum}.")


print_circum(
    4
)  # The circemference of the circlre for which the given radus is 25.13272.
print_circum(
    6
)  # The circemference of the circlre for which the given radus is 37.699079999999995.
print_circum(
    9
)  # The circemference of the circlre for which the given radus is 56.54862.
