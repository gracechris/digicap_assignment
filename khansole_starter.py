import random

# simply informing the computer to grant us random numbers
secret_number = random.randint(7, 9)
# the while loop is to help us identify whether the input user is high,low or correct
while True:
    # get user number
    input_user = int(input("Guess the number : "))
    # checking if the user number is greater than the secret number of the computer
    if input_user > secret_number:
        print("Your guess is too high")
        # checking if the user number is less than the secret number of the computer
    elif input_user < secret_number:
        print("Your guess is too low")
        # checking whether the user number is equal to the secret number
    else:
        print("Your guess is right")
        break
