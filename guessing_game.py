secret_number = 7
guess = float(input("Guess a number: "))


if guess == secret_number:
    print("Correct!")
elif guess< secret_number:
    print ("Guess too low")
else:
    print("Guess too high")
while guess!= secret_number:
    print ("Guess Again")
    if guess == secret_number:
        print ("Correct")
    elif guess< secret_number:
        print("Guess too low")
    else:
        print("Guess too high")
    guess=float(input("Guess a number"))
