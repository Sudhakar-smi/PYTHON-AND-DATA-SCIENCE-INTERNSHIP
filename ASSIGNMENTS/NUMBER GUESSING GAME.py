import random

low = 0
high = 100
gues = 0

number = random.randint(low, high)

while True:
    guess = int(input(f"Enter a number between ({low}-{high}): "))
    
    gues += 1

    if guess < number:
        print(f"{guess} is too low")

    elif guess > number:
        print(f"{guess} is too high")

    else:
        print(f"{guess} is correct")
        break

    print(f"This round took you {gues} guesses")