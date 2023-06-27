# algorithm:
# if odd number, use the expression 3x + 1
# if even, divide by 2
# repeat

number = int(input("Enter starting number: "))
while True:
    if number % 2 == 0:
        number = number/2
    else:
        number = 3 * number + 1

    print(number)


    # checking to see if it matches
    # this is because if it reaches 1 it becomes an infinite loop (1 -> 4 -> 2 -> 1), and we dont want to explode anyones computer
    if number == 1:
        break