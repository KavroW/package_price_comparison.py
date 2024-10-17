oneWeight = float(input('Enter weight for package 1: '))
onePrice = float(input('Enter price for package 1: '))
twoWeight = float(input('Enter weight for package 2: '))
twoPrice = float(input('Enter price for package 2: '))

oneValue = onePrice/oneWeight
twoValue = twoPrice/twoWeight

if oneValue < twoValue:
    print('Package 1 has the best price.')
elif twoValue < oneValue:
    print('Package 2 has the best price.')
else:
    print('Package 1 and Package 2 have the same price.')