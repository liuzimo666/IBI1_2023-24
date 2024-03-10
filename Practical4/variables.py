# Before any training
a = 40
# After the month of running training
b = 36
# After a second month of running and strength training
c = 30
# the time improvement from running only as the difference between a and b
d = a-b
# the time improvement from running and strength training as the difference between	b and c
e = b-c
if d > e:
    # Running only had a greater improvement
    print(f"The time improvement from running only is greater than the time improvement from running and strength training.")
    print(f"Therefore, the running-only training regime had a greater improvement on running time.")
else:
    # Running and strength training had a greater improvement
    print(f"The time improvement from running and strength training is greater than the time improvement from running only.")
    print(f"Therefore, the combined running and strength training regime had a greater improvement on running time.")








# Create variables X and Y
X = True
Y = False
# Create variable W which encodes the Boolean variable 'either X or Y'
W = X or Y
# Truth table for W:
# X | Y | W
# T | T | T
# T | F | T
# F | T | T
# F | F | F
# Comment: The truth table for W shows that W is True when either X or Y (or both) are True.
#          When both X and Y are False, W is also False.
print("X:", X)
print("Y:", Y)
print("W:", W)