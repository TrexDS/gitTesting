weight = float(input("Weight(KG): \n"))
#weight should be kg
height = float(input("Height(CM): \n"))
#height should be cm
BMI = weight / (height/100)**2

if BMI <= 18.5:
    print("Underweight")
elif BMI <= 25.0:
    print("Normal")
elif BMI <= 30.0:
    print("Overweight")
elif BMI <= 45.0:
    print("Obese")
else:
    print("hello world")

