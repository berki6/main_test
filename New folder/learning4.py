# age = int(input("Enter your age: "))  # Get the age from the user
#
# if age < 10:
#     admission_rate = 0  # Admission is free for anyone under age 10
# elif 10 <= age <= 18:
#     admission_rate = 100  # Admission for anyone between the ages 10 and 18 is 100 Birr
# else:
#     admission_rate = 300  # Admission for anyone age 18 or older is 300 Birr
#
# print(f"Your admission rate is {admission_rate} Birr.")


# grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94] # List of quiz grades
#
# total = sum(grades) # Calculate the sum of all grades
#
# num_students = len(grades) # Calculate the number of students
#
# average = total / num_students # Calculate the average by dividing the sum by the number of students
#
# print("The class average is:", round(average, 2)) # Print the average grade rounded to two decimal places

# for n in range(100):
#     if n == 10:
#         break
#     print(n)
# n = 10
# while n > 0:
#     print(n)
#     n -= 1
#     if n == 4:
#         break

# age = int(input("What's your age? "))
# match age:
#     case 0:
#         print("You're a newborn.")
#     case n if n < 18:
#         print("You're a minor.")
#     case n if n >= 18 and n < 65: # 18 <= n < 65
#         print("You're an adult.")
#     case _:
#         print("You're a senior citizen.")

# day = input("Enter the day: ")
# match day:
#     case "Mon" | "Tue" | "Wed" | "Thu" | "Fri":
#         print("It's a weekday")
#     case "Sat" | "Sun":
#         print("It's a weekend")
#     case _:
#         print("Invalid day")

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# op = (input("Enter operator: "))
# match op:
#     case '+':
#         print(f'{num1} + {num2} = ', num1 + num2)
#     case '-':
#         print(f'{num1} - {num2} = ', num1 - num2)
#     case '*':
#         print(f'{num1} * {num2} = ', num1 * num2)
#     case '/':
#         print(f'{num1} / {num2} = ', num1 / num2)
#     case _:
#         print("Invalid")

# # First, ask the player about their CPU
# cpuModel = input("Please enter your CPU model: ")
# # The match statement evaluates the variable's value
# match cpuModel:
#     case "celeron": # We test for different values and print different messages
#         print ("Forget about it and play Minesweeper instead...")
#     case "core i3":
#         print ("Good luck with that ;)")
#     case "core i5":
#         print ("Yeah, you should be fine.")
#     case "core i7":
#         print ("Have fun!")
#     case _: # the underscore character is used as a catch-all.
#         print ("Is that even a thing?")

# def add_numbers(num1, num2):
#     sum = num1 +num2
#     return sum
#
# x = 5
# y = 4
# print(add_numbers(x,y))

# def find_square(num):
#   return num ** 2
#
# square = find_square(3)
# print(square)
# print("The square of 6 is ", find_square(6))

# def absolute_fun(x):
#     if x > 0:
#         return x
#     else:
#         return -x
# print(absolute_fun(-8) + 55)
#
# def greet_user(first_name, last_name):
#   print(f"Hi {first_name} {last_name}.")
#
# greet_user("John", "Snow")
# greet_user("Mohammed", "Ali")
# greet_user("Steve", "Jobs")

# def eligible_to_vote(name, age=18):
#     if age < 18:
#         print(f"{name}! You’re too young")
#     elif age == 18:
#         print(f"{name}! You’re good to vote")
#     else:
#         print(f"{name}! You’re eligible")
#
#
# eligible_to_vote("Bere", age=12)


def append_item(item, item_list = []):
 item_list.append(item)
 return item_list

append_item("laptop", item_list= [])
# append_item('smart phone')