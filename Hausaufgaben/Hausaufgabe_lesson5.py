one_value = input('enter first logik value (True or False) : ').strip().capitalize() == 'True'
two_value = input('enter second logik value (True or False) : ').strip().capitalize() == 'True'
print(f"Result of logical (and) : {one_value and two_value}")
print(f"Result of logical (or) : {one_value or two_value}")
print(f"Result of logical NOT (first value):: {not one_value}")
print(f"Result of logical NOT (second value):: {not two_value}")
print(f'Result of equality comparison: {one_value == two_value}')
print(f'Result of the comparison for inequality: {one_value != two_value}')




