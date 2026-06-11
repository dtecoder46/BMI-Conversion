prompt = input(
    "Welcome to the BMI Converter! Do you want to convert to pounds or BMI?: ")

if prompt == "pounds":
    BMI = float(input("enter your BMI in kg/m^2: "))
    height = float(input("enter your height in inches: "))

    weight = (BMI/703) * (height**2)

    print(f"Your weight is {weight} pounds")


elif prompt == "BMI":
    # BMI
    mass = float(input("enter your mass in pounds: "))
    height = float(input("enter your height in inches: "))

    BMI = (mass/height**2) * 703

    print(f"Your BMI is {BMI} kg/m^2")

else:
    print("Invalid input, choose one of the two options")
