def get_number():
    "Returns a float number"
    number = float(input("Enter a float number: "))
    return number

while True:
    try:
        print(get_number())
    except TypeError:
        print("You entered a wrong value.")
    except :
         print("Unknown Error.")
         
