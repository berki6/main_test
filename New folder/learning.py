# selfish = 'me me me'
# print(selfish[::-1].upper())
# name = 'bere'
# age = 50
# relation_stat = 'single'
#
# relation_stat = 'it\'s complicated'
#
# print(relation_stat)
# birth_yr = input('what year were you born?')
#
# age = 2023 - int(birth_yr)
#
# print(f'your age is {(age)}.')

def pascal_triangle(n):
  for i in range(n):
    for j in range(i+1):
      print(" ", end="")
      if j==0 or j==i:
        print("*", end="")
      else:
        print("*", end="")
    print()
n = 5
pascal_triangle(n)

x = "cat"
print(x[10:])





