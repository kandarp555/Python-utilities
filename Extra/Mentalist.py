a = input("Are you ready? (yes or no)\n")
if a.lower() == "yes":
    x = int(input("Enter a number (length > 2 digits):\n"))
    print("Now, add the digits of the number together")
    y = int(input("Enter the sum of the digits:\n"))
    print("Great! Now subtract", y, "from the original number")
    print("Have you done it?")
    print("If yes, add the digits of the result together until you get a single-digit number")
    print("If you've done that, find the corresponding alphabet (e.g., 1 = A)")
    z = input("Have you found the alphabet corresponding to the digit? (yes or no)\n")
    if z.lower() == "yes":
        print("Now, think of a country that starts with that letter.")
        A = input("Have you thought of a country? (yes or no)\n")
        if A.lower() == "yes":
            B = input("Is 'India' the country you're thinking of? (yes or no)\n")
            if B.lower() == "yes":
                print("I guessed it! 😉\nBy the way, nice choice.")
            else:
                C = input("Tell me the last letter of that country's name:\n")
                if C.lower() == "a":
                    print("Now I'm sure, you're thinking of 'Indonesia'")
                elif C.lower() == "d":
                    print("Now I'm sure, you're thinking of 'Iceland' or 'Ireland'")
                elif C.lower() == "n":
                    print("Now I'm sure, you're thinking of 'Iran'")
                elif C.lower() == "q":
                    print("Now I'm sure, you're thinking of 'Iraq'")
                elif C.lower() == "l":
                    print("Now I'm sure, you're thinking of 'Israel'")
                elif C.lower() == "y":
                    print("Now I'm sure, you're thinking of 'Italy'")
else:
    print("Nice to meet you. Goodbye!")
