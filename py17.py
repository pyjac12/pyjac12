celsius = int(input("Please enter an integer value for degrees celsius. "))
 
 
def fahrenheit(cel):
    # The second argument of round() is 1 since we only want the Fahrenheit temperature to be displayed with 1 number
    # after the decimal point
    return round((1.8 * cel + 32), 1)
 
 
print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")
