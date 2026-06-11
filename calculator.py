import math
import cmath
import statistics
import random
import numpy as np
import sympy as sp
import networkx as nx

history = []

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Power")
    print("6.Modulus")
    print("7.Floor Division")
    print("8.Square Root")
    print("9.Expression Calculator")

    print("63.Show History")

    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/...): ")
    
    if choice == '1':
        result = num1 + num2
        print(result)
        print(num1,"+",num2,"=", num1+num2)
        history.append(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = num1 - num2
        print(result)
        print(num1,"-",num2,"=", num1-num2)
        history.append(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = num1 * num2
        print(result)
        print(num1,"*",num2,"=", num1*num2)
        history.append(f"{num1} * {num2} = {result}")
    elif choice == '4':
        result = num1 / num2
        print(result)
        print(num1,"/",num2,"=", num1/num2)
        history.append(f"{num1} / {num2} = {result}")
    elif choice == '5':
        result = num1 ** num2
        print(result)
        print(num1,"**",num2,"=", num1**num2)
        history.append(f"{num1} ** {num2} = {result}")
    elif choice == '6':
        result = num1 % num2
        print(result)
        print(num1,"%",num2,"=", num1%num2)
        history.append(f"{num1} % {num2} = {result}")
    elif choice == '7':
        result = num1 // num2
        print(result)
        print(num1,"//",num2,"=", num1//num2)
        history.append(f"{num1} // {num2} = {result}")
    elif choice == '8':
        result = math.sqrt(num1)
        print("Square root of",num1,"is", result)
        history.append(f"Square root of {num1} = {result}")
    elif choice == '9':
        expression = input("Enter expression: ")
        try:
            result = eval(expression)
            print(expression,"=", result)
            history.append(f"{expression} = {result}")
        except:
            print("Invalid expression.")
    elif choice == '10':
        result = math.log(num1)
        print("Logarithm of",num1,"is", result)
        history.append(f"Logarithm of {num1} = {result}")
    elif choice == '11':
        result = num1 ** num2
        print(num1,"e^",num2,"=", result)
        history.append(f"{num1} ** {num2} = {result}")
    elif choice == '12':
        result = math.factorial(int(num1))
        print("Factorial of",num1,"is", result)
        history.append(f"Factorial of {num1} = {result}")
    elif choice == '13':
        result = math.gcd(int(num1), int(num2))
        print("GCD of",num1,"and",num2,"is", result)
        history.append(f"GCD of {num1} and {num2} = {result}")
    elif choice == '14':
        def lcm(x, y):
            return abs(x * y) // math.gcd(x, y)
        result = lcm(int(num1), int(num2))
        print("LCM of",num1,"and",num2,"is", result)
        history.append(f"LCM of {num1} and {num2} = {result}")
    elif choice == '15':
        result = math.sin(num1)
        print("Sin of",num1,"is", result)
        history.append(f"Sin of {num1} = {result}")
    elif choice == '16':        
        result = math.cos(num1)
        print("Cos of",num1,"is", result)
        history.append(f"Cos of {num1} = {result}")
    elif choice == '17':
        result = math.tan(num1)
        print("Tan of",num1,"is", result)
        history.append(f"Tan of {num1} = {result}")
    elif choice == '18':
        result = 1/math.tan(num1)
        print("Cot of",num1,"is", result)
        history.append(f"Cot of {num1} = {result}")
    elif choice == '19':
        result = 1/math.cos(num1)
        print("Sec of",num1,"is", result)
        history.append(f"Sec of {num1} = {result}")
    elif choice == '20':
        result = 1/math.sin(num1)
        print("Csc of",num1,"is", result)
        history.append(f"Csc of {num1} = {result}")
    elif choice == '21':
        result = math.hypot(num1, num2)
        print("Hypotenuse of",num1,"and",num2,"is", result)
        history.append(f"Hypotenuse of {num1} and {num2} = {result}")
    elif choice == '22':
        def permutation(n, r):
            return math.factorial(n) // math.factorial(n - r)
        result = permutation(int(num1), int(num2))
        print("Permutation of",num1,"and",num2,"is", result)
        history.append(f"Permutation of {num1} and {num2} = {result}")
    elif choice == '23':
        def combination(n, r):
            return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
        result = combination(int(num1), int(num2))
        print("Combination of",num1,"and",num2,"is", result)
        history.append(f"Combination of {num1} and {num2} = {result}")
    elif choice == '24':
        result = abs(num1)
        print("Absolute value of",num1,"is", result)
        history.append(f"Absolute value of {num1} = {result}")
    elif choice == '25':
        result = round(num1)
        print("Rounded value of",num1,"is", result)
        history.append(f"Rounded value of {num1} = {result}")
    elif choice == '26':
        result = math.ceil(num1)
        print("Ceil value of",num1,"is", result)
        history.append(f"Ceil value of {num1} = {result}")
    elif choice == '27':
        result = math.floor(num1)
        print("Floor value of",num1,"is", result)
        history.append(f"Floor value of {num1} = {result}")
    elif choice == '28':
        result = random.uniform(num1, num2)
        print("Random number between",num1,"and",num2,"is", result)
        history.append(f"Random number between {num1} and {num2} = {result}")
    elif choice == '29':
        percentage = (num1 / num2) * 100
        print(num1,"is", percentage,"% of",num2)
        history.append(f"{num1} is {percentage}% of {num2}")
    elif choice == '30':
        average = (num1 + num2) / 2
        print("Average of",num1,"and",num2,"is", average)
        history.append(f"Average of {num1} and {num2} = {average}")
    elif choice == '33':
        result = statistics.variance([num1, num2])
        print("Variance of",num1,"and",num2,"is", result)
        history.append(f"Variance of {num1} and {num2} = {result}")
    elif choice == '34':
        result = (num1 - statistics.mean([num1, num2])) / statistics.stdev([num1, num2])
        print("Z-Score of",num1,"is", result)
        history.append(f"Z-Score of {num1} = {result}")
    elif choice == '35':
        temp_c = (num1 - 32) * 5.0/9.0
        print(num1,"Fahrenheit is", temp_c,"Celsius")
        history.append(f"{num1} Fahrenheit is {temp_c} Celsius")
    elif choice == '36':
        length_m = num1 * 0.3048
        print(num1,"Feet is", length_m,"Meters")
        history.append(f"{num1} Feet is {length_m} Meters")
    elif choice == '37':
        weight_kg = num1 * 0.453592
        print(num1,"Pounds is", weight_kg,"Kilograms")
        history.append(f"{num1} Pounds is {weight_kg} Kilograms")
    elif choice == '38':
        time_s = num1 * 3600
        print(num1,"Hours is", time_s,"Seconds")
        history.append(f"{num1} Hours is {time_s} Seconds")
    elif choice == '39':
        area_m2 = num1 * 0.092903
        print(num1,"Square Feet is", area_m2,"Square Meters")
        history.append(f"{num1} Square Feet is {area_m2} Square Meters")
    elif choice == '40':
        volume_l = num1 * 3.78541
        print(num1,"Gallons is", volume_l,"Liters")
        history.append(f"{num1} Gallons is {volume_l} Liters")
    elif choice == '41':
        speed_kmh = num1 * 1.60934
        print(num1,"Miles per Hour is", speed_kmh,"Kilometers per Hour")
        history.append(f"{num1} Miles per Hour is {speed_kmh} Kilometers per Hour")
    elif choice == '42':
        pressure_pa = num1 * 101325
        print(num1,"Atmospheres is", pressure_pa,"Pascals")
        history.append(f"{num1} Atmospheres is {pressure_pa} Pascals")
    elif choice == '43':
        energy_j = num1 * 4.184
        print(num1,"Calories is", energy_j,"Joules")
        history.append(f"{num1} Calories is {energy_j} Joules")
    elif choice == '44':
        power_w = num1 * 745.7
        print(num1,"Horsepower is", power_w,"Watts")
        history.append(f"{num1} Horsepower is {power_w} Watts")
    elif choice == '45':
        data_gb = num1 * 1024
        print(num1,"Megabytes is", data_gb,"Gigabytes")
        history.append(f"{num1} Megabytes is {data_gb} Gigabytes")
    elif choice == '46':
        currency_usd = num1 * 0.85
        print(num1,"Euros is", currency_usd,"US Dollars")
        history.append(f"{num1} Euros is {currency_usd} US Dollars")
    elif choice == '47':
        print("Sin of",num1,"is", math.sin(num1))
        print("Cos of",num1,"is", math.cos(num1))
        print("Tan of",num1,"is", math.tan(num1))
        history.append(f"Sin of {num1} is {math.sin(num1)}")
        history.append(f"Cos of {num1} is {math.cos(num1)}")
        history.append(f"Tan of {num1} is {math.tan(num1)}")
    elif choice == '48':
        print("Inverse Sin of",num1,"is", math.asin(num1))
        print("Inverse Cos of",num1,"is", math.acos(num1))
        print("Inverse Tan of",num1,"is", math.atan(num1))
        history.append(f"Inverse Sin of {num1} is {math.asin(num1)}")
        history.append(f"Inverse Cos of {num1} is {math.acos(num1)}")
        history.append(f"Inverse Tan of {num1} is {math.atan(num1)}")
    elif choice == '49':
        print("Hyperbolic Sin of",num1,"is", math.sinh(num1))
        print("Hyperbolic Cos of",num1,"is", math.cosh(num1))
        print("Hyperbolic Tan of",num1,"is", math.tanh(num1))
        history.append(f"Hyperbolic Sin of {num1} is {math.sinh(num1)}")
        history.append(f"Hyperbolic Cos of {num1} is {math.cosh(num1)}")
        history.append(f"Hyperbolic Tan of {num1} is {math.tanh(num1)}")
    elif choice == '50':
        num_asinh = float(input("Enter the value for Inverse Hyperbolic Sin: "))
        num_acosh = float(input("Enter the value for Inverse Hyperbolic Cos: "))
        num_atanh = float(input("Enter the value for Inverse Hyperbolic Tan: "))
        print("Inverse Hyperbolic Sin of",num_asinh, "is", math.asinh(num_asinh))
        print("Inverse Hyperbolic Cos of", num_acosh, "is", math.acosh(num_acosh))
        print("Inverse Hyperbolic Tan of", num_atanh, "is", math.atanh(num_atanh))
        history.append(f"Inverse Hyperbolic Sin of {num_asinh} is {math.asinh(num_asinh)}")
        history.append(f"Inverse Hyperbolic Cos of {num_acosh} is {math.acosh(num_acosh)}")
        history.append(f"Inverse Hyperbolic Tan of {num_atanh} is {math.atanh(num_atanh)}")
    elif choice == '51':
        matrix1 = np.array([[num1, num2], [num2, num1]])
        matrix2 = np.array([[num2, num1], [num1, num2]])
        print("Matrix 1:\n", matrix1)
        print("Matrix 2:\n", matrix2)
        print("Matrix Addition:\n", matrix1 + matrix2)
        print("Matrix Subtraction:\n", matrix1 - matrix2)
        print("Matrix Multiplication:\n", np.dot(matrix1, matrix2))
        history.append(f"Matrix 1: {matrix1}")
        history.append(f"Matrix 2: {matrix2}")
        history.append(f"Matrix Addition: {matrix1 + matrix2}")
        history.append(f"Matrix Subtraction: {matrix1 - matrix2}")
        history.append(f"Matrix Multiplication: {np.dot(matrix1, matrix2)}")
    elif choice == '52':
        vector1 = np.array([num1, num2])
        vector2 = np.array([num2, num1])
        print("Vector 1:", vector1)
        print("Vector 2:", vector2)
        print("Dot Product:", np.dot(vector1, vector2))
        print("Cross Product:", np.cross(vector1, vector2))
        history.append(f"Vector 1: {vector1}")
        history.append(f"Vector 2: {vector2}")
        history.append(f"Dot Product: {np.dot(vector1, vector2)}")
        history.append(f"Cross Product: {np.cross(vector1, vector2)}")
    elif choice == '53':
        data = [num1, num2]
        print("Mean:", statistics.mean(data))
        print("Median:", statistics.median(data))
        print("Mode:", statistics.mode(data))
        print("Standard Deviation:", statistics.stdev(data))
        print("Variance:", statistics.variance(data))
        history.append(f"Mean: {statistics.mean(data)}")
        history.append(f"Median: {statistics.median(data)}")
        history.append(f"Mode: {statistics.mode(data)}")
        history.append(f"Standard Deviation: {statistics.stdev(data)}")
        history.append(f"Variance: {statistics.variance(data)}")
    elif choice == '54':
        print("Random number between",num1,"and",num2,"is", random.uniform(num1, num2))
        history.append(f"Random number between {num1} and {num2} = {random.uniform(num1, num2)}")
    elif choice == '55':
        x = sp.symbols('x')
        expression = num1 * x**2 + num2 * x + 1
        print("Derivative of", expression, "is", sp.diff(expression, x))
        history.append(f"Derivative of {expression} is {sp.diff(expression, x)}")
    elif choice == '56':
        matrix = np.array([[num1, num2], [num2, num1]])
        print("Matrix:\n", matrix)
        print("Determinant:", np.linalg.det(matrix))
        print("Inverse:\n", np.linalg.inv(matrix))
        history.append(f"Matrix:\n {matrix}")
        history.append(f"Determinant: {np.linalg.det(matrix)}")
        history.append(f"Inverse:\n {np.linalg.inv(matrix)}")
    elif choice == '57':
        x = sp.symbols('x')
        equation = sp.Eq(num1 * x**2 + num2 * x + 1, 0)
        print("Solutions to the equation", equation, "are", sp.solve(equation, x))
        history.append(f"Solutions to the equation {equation} are {sp.solve(equation, x)}")
    elif choice == '58':
        complex_number = complex(num1, num2)
        print("Complex number:", complex_number)
        print("Magnitude:", abs(complex_number))
        print("Phase:", cmath.phase(complex_number))
        history.append(f"Complex number: {complex_number}")
        history.append(f"Magnitude: {abs(complex_number)}")
        history.append(f"Phase: {cmath.phase(complex_number)}")
    elif choice == '59':
        n = sp.symbols('n')
        print("Prime factors of", num1, "are", sp.primefactors(int(num1)))
        history.append(f"Prime factors of {num1} are {sp.primefactors(int(num1))}")
    elif choice == '60':
        a_input = input("Enter elements of set A (comma-separated):")
        b_input =input("Enter elements of set B(comma-separated):")
        A = sp.FiniteSet(*[sp.Integer(x.strip()) for x in a_input.split(',')])
        B = sp.FiniteSet(*[sp.Integer(x.strip()) for x in b_input.split(',')])
        print("Union of sets A and B is", sp.Union(A, B))
        print("Intersection of sets A and B is", sp.Intersection(A, B))
        history.append(f"Union of sets A and B is {sp.Union(A, B)}")
        history.append(f"Intersection of sets A and B is {sp.Intersection(A, B)}")
    elif choice == '61':
        G = nx.Graph()
        G.add_edge(num1, num2)
        print("Graph edges:", G.edges())
        history.append(f"Graph edges: {G.edges()}")
    elif choice == '62':    
        print("Value of pi is", math.pi)
    elif choice == '63':
        print("History:")
        for item in history:
            print(item)
    else:
        print("Invalid input")






