def main():
    a=float(input("Enter the temperature in degrees Fahrenheit: "))
    b=float (((a-32)*5)/9)
    print (a,"degrees Fahrenheit in degrees Celcius is",b)

    c=str(input("Do you want to do this again: Y or N? "))
    if c == 'y':
        main()
    else:
        print ("Goodbye.")
main()
