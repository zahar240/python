cube = []
cube_plus_17 = []
sum_multiple_7 = 0
sum_multiple_7_plus_17 = 0


for number in range(1, 1001, 2):
    cube.append(number ** 3)
    cube_plus_17.append(number ** 3 + 17)

for number in cube:
    digit_sum = 0
    number_7 = number
    while number > 0:
        digit_sum += number %10
        number //= 10
    if digit_sum %7 == 0:
        sum_multiple_7 += number_7

for number in cube_plus_17:
    digit_sum = 0
    number_7 = number
    while number > 0:
        digit_sum += number %10
        number //= 10
    if digit_sum %7 == 0:
        sum_multiple_7_plus_17 += number_7


print(sum_multiple_7)
print(sum_multiple_7_plus_17)