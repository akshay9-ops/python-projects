def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return print("Leap Year")
            else:
                return print("Not Leap Year")
        else:
            return print("Leap Year")
    else:
        return print("Not Leap Year")


is_leap(2000)