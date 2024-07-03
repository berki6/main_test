name = 'johnny'
age = 55

print(f'Hi {name}. You are {age} years old!')
print('Hi {}. You are {} years old!'.format('johnny', 55))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in my_list:
    sum1 = sum(my_list)
print(sum1)

counter = 0
for item in my_list:
    counter = counter + item
print(counter)


W = float(input('My weight: '))
H = float(input('My height:'))
my_BMI = W / (H*H)
print('My BMI: ', my_BMI.__round__(4))
if my_BMI >= 25.0:
    print('Oh, You\'re overweight. Do exercises.')
elif 18.5 <= my_BMI <= 24.9:
    print('You are at a healthy range continue the good job.')
else:
    print('you are underweight. You have got to gain some fat.')
