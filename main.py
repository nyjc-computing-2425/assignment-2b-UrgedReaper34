num = input('Enter a number (decimal only): ')
# type your code here

dp = str(len(num[num.index(".") + 1:]))


# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
