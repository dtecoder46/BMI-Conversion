prompt = input(
    "Welcome to the BMI Converter! Do you want to convert to pounds or BMI?: ")

if prompt == "pounds":
    print("placeholder")

elif prompt == "BMI":
    # BMI
    mass = int(input("enter your mass in pounds: "))
    height = int(input("enter your height in inches: "))

    BMI = (mass/height**2) * 703

    print(f"Your BMI is {BMI} kg/m^2")

else:
    print("Invalid input, choose one of the two options")
