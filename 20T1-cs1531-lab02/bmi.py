kilo = float(input("What is your weight in kg? "))
if type(kilo) == int or type(kilo) == float:
    height = float(input("What is your height in m? "))
    if type(height) == int or type(height) == float or height > 0:
        BMI = float(kilo/height**2)
        result = "Your BMI is {0:.1f}"
        print(result.format(float(BMI)))
    else:
        print("Please type in a valid number")
else:
    print("Please type in a valid number")
