# formatted strings
name = 'Johnny'
age = 55

print(f'Hi {name}. You are {age} years old.')
print('Hi {}. You are {} years old.'.format('johnny', '55')) #.format is the old python 2 way
print('Hi {}. You are {} years old.'.format(name, age))