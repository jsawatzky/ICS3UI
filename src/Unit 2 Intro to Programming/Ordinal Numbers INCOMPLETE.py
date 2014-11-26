while 5 > 4:
    n = input("Enter a positive integer from 0-100: ")

    if n == "1":
        suffix = "st"
        
    elif n == "2":
        suffix = "nd"

    elif n == "3":
        suffix = "rd"

    else:
        suffix = "th"

    print (n + suffix)

