user_input = input("Your chosen number: ").split(' ')
user_input = str(user_input).split(' ')

print(user_input)
# I use .split(' ') to make '5 4 4 6 1' into ['5', '4', '4', '6', '1']
# Because now it will be easier to index it

number_pick = int(input("Num: "))
# If we enter 4, this will be the integer 4, not '4'

# And now we just take the element with our index - 1,
# because lists are zero-indexed
value = user_input[number_pick - 1]

print("Value: {}".format(value))  # Value: 6
