# Задание 1
import math


numer_one = int(input('enter number one : '))
numer_two = int(input('enter number two : '))

print(f' summ number {numer_one} and number {numer_two} = {numer_one + numer_two}')
print(f' minus number {numer_one} and number {numer_two} = {numer_one - numer_two}')
print(f' multiplications number {numer_one} and number {numer_two} = {numer_one * numer_two}')
print(f' division number {numer_one} and number {numer_two} = {numer_one / numer_two}')
print(f' remainder from division number {numer_one} and number {numer_two} = {numer_one % numer_two}')
print(f' raising the number {numer_one} to the power of {numer_two} = {numer_one ** numer_two}')

# Задание 2
radius_circle = float(input('enter radius of circle : '))
print(f' circumference = {2 * math.pi * radius_circle}')
print(f' area of circle = {math.pi * radius_circle ** 2}')

# Задание 3
data_1 = input('enter coordinate point one (x1, y1) :')
coordinate_X1 , coordinate_Y1 = map(int,data_1.split(','))
data_2 = input('enter coordinate point two (x2, y2) :')
coordinate_X2 , coordinate_Y2 = map(int,data_2.split(','))
distance = ((coordinate_X2 - coordinate_X1) ** 2 + (coordinate_Y2 - coordinate_Y1) ** 2 ) ** 0.5
print(f'Distance between points : {distance}')

