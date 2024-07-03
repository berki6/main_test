# first_name = input('First name:')
# last_name = input('Last name:')
# age = int(input("age:"))
# print(f'My name is {first_name} {last_name} and I am {age} years old.')
# value =  range(100)
# count = 0
# for x in value:
#     if x % 2 == 0:
#         count +=x
#     else:
#         continue
# print(count)

# count = 0
# sum = 0
# for number in range(0, 8):
#     if number % 2 == 0:
#         # count +=1
#         sum += number
#         # print(number)
# print(f"we have count even numbers and they add to {sum}.")

# x = input("Enter num1:")
# y = input("Enter num2:")
# z = input("Enter num3:")
# max_value = x
# if y > max_value:
#     max_value = y
#     print(f"Max value is {y}")
#     if z > max_value:
#         max_value = z
#         print(f"Max value is {z}")
#     else:
#         max_value = x
#         print(f"Max value is {x}")

#
# lis_t = ([0,0,0,0,0,0,0,0,0,0,1],
#          [0,0,0,0,0,0,0,0,0,1,1],
#          [0,0,0,0,0,0,0,0,1,1,1],
#          [0,0,0,0,0,0,0,1,1,1,1],
#          [0,0,0,0,0,0,1,1,1,1,1],
#          [0,0,0,0,0,1,1,1,1,1,1],
#          [0,0,0,0,1,1,1,1,1,1,1],
#          [0,0,0,1,1,1,1,1,1,1,1],
#          [0,0,1,1,1,1,1,1,1,1,1])
# for row in lis_t:
#     for num in row:
#         if num == 0:
#             print(' ', )
#         else:
#              print('*', end='')
# def fact_orial(num):
#     if num <0:
#         return -1
#     elif num==0:
#         return 1
#     else:
#         result = 1
#         for i in range(1,num+1):
#             result *=i
#             return result
# fact_orial(5)


from abc import ABC, abstractmethod

class TextPrinter(ABC):
    @abstractmethod
    def print_text(self):
        pass

class PlainTextPrinter(TextPrinter):
    def __init__(self, text):
        self.text = text

    def print_text(self):
        print(self.text)

class TextDecorator(TextPrinter):
    def __init__(self, text_printer):
        self.text_printer = text_printer

    def print_text(self):
        self.text_printer.print_text()

class BoldTextDecorator(TextDecorator):
    def print_text(self):
        print(f"<b>{self.text_printer.print_text()}</b>")

class ItalicTextDecorator(TextDecorator):
    def print_text(self):
        print(f"<i>{self.text_printer.print_text()}</i>")

# Client code
if __name__ == "__main__":
    plain_printer = PlainTextPrinter("Hello, world!")
    bold_printer = BoldTextDecorator(plain_printer)
    italic_bold_printer = ItalicTextDecorator(bold_printer)

    plain_printer.print_text()
    bold_printer.print_text()
    italic_bold_printer.print_text()

