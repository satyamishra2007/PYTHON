x = 5

if x >= 0:
    print("Number is Positive number")

    if x % 2 == 0:
        print("Number is Even Number")
        if x < 10:
            print("Number is Even Number and is less than 10")

        elif x >= 10 and x <= 20:
            print("Number is Even Number and is less than 20")

        else:
            print("Number is Even Number and is greate than 20")

    else:
        print("Number is Odd Number")

        if x < 10:
            print("Number is Even Number and is less than 10")

        elif x >= 10 and x < 20:
            print("Number is Even Number and is less than 20")

        else:
            print("Number is Even Number and is greate than 20")

else:
    print("Number is Negative number")