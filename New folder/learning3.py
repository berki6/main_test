# is_old = True
# is_licenced = True
# if is_old:
#     print('you are old enough to drive!')
#     print('check check')
# elif is_licenced:
#     print('you can drive now. ')
# else:
#     print('no no')
#
# height = input('How tall are you in inches?')
# if float(height) >= 36:
#     print("You\'re tall enough to ride!")
# else:
#     print("You\'ll be able to ride when you're a little older")
#
# num = input("Enter a number:")
# if int(num) % 2 == 0:
#     print(f"{num} is even number")
# else:
#     print("It's odd number")
#
# x = 3456
# if x % 2 == 0:
#     print(x, ' is even')
#     if x % 5 == 0:
#         print(x, ' is divisible by 5')
#         print('Output only when x is divisible by both 2 & 5')
#     else:
#         print(x, 'is not divisible by 5')
#         print('Output only when x is divisible by 2, not by 5')
# else:
#     print(x, 'is odd')
#     print('No Indentation. Output in all cases')
#
# age = input('what is your age?')
# if int(age) < 10:
#     print('Entry is granted for free.')
#     else:
#     print('Access denied! ')
#     if int(age) > 10:
#
#     elif int(age) < 18:
#     print('Admission fee is 100 birr.')
#
# n = 0
# while n < 3:
#     print(n)
#     n += 1
# for i in range(3):
#     for j in range(2):
#         print(i, j)
#
import random
# https://gist.github.com/cwil323/9b1bfd25523f75d361879adfed550be2


def display_intro():
    title = "** A Simple Math Quiz **"
    print("*" * len(title))
    print(title)
    print("*" * len(title))


def display_menu():
    menu_list = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Integer Division", "5. Exit"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])
    print(menu_list[3])
    print(menu_list[4])


def display_separator():
    print("-" * 24)


def get_user_input():
    user_input = int(input("Enter your choice: "))
    while user_input > 5 or user_input <= 0:
        print("Invalid menu option.")
        user_input = int(input("Please try again: "))
    else:
        return user_input


def get_user_solution(problem):
    print("Enter your answer")
    print(problem, end="")
    result = int(input(" = "))
    return result


def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count = count + 1
        print("Correct.")
        return count
    else:
        print("Incorrect.")
        return count


def menu_option(index, count):
    number_one = random.randrange(1, 21)
    number_two = random.randrange(1, 21)
    if index == 1:
        problem = str(number_one) + " + " + str(number_two)
        solution = number_one + number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    elif index == 2:
        problem = str(number_one) + " - " + str(number_two)
        solution = number_one - number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    elif index == 3:
        problem = str(number_one) + " * " + str(number_two)
        solution = number_one * number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    else:
        problem = str(number_one) + " // " + str(number_two)
        solution = number_one // number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count


def display_result(total, correct):
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    print("You answered", total, "questions with", correct, "correct.")
    print("Your score is ", percentage, "%. Thank you.", sep="")


def main():
    display_intro()
    display_menu()
    display_separator()

    option = get_user_input()
    total = 0
    correct = 0
    while option != 5:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input()

    print("Exit the quiz.")
    display_separator()
    display_result(total, correct)

main()
