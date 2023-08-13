def tangent(c, p, x, s):
    y = 0
    for n in range(len(c)):
        y = y + c[n] * pow(x, p[n])
        # distribute
        mx = str(s) + "x"
        b = s * -x + y

    tangentEq = "y = " + str(mx) + " + " + str(b)
    return tangentEq


def main():
    # inputs
    f = input("What function would you like to differentiate? (please put a 1 in front of terms without a coefficient)")
    xValue = input("At what x-value would you like to evaluate the derivative?")

    function = []
    terms = []
    derTerm = []
    termLength = []
    operatorPosition = []
    operatorPosition2 = []
    operatorPosition3 = []
    operators = []
    powerPosition = []
    power = []
    coefficient = []
    derPwr = []
    derCoeff = []
    xPosition = []

    # used for future calculations
    operatorPosition.append(0)
    operatorPosition3.append(0)

    # finding operator positions to prepare for term division
    for n in range(len(f)):
        function.append(f[n])
        if (f[n] == "+"):
            operatorPosition.append(n)
            operatorPosition2.append(n)
            operatorPosition3.append(n + 1)
            operatorPosition.append(n + 1)
            operators.append(f[n])
        elif (f[n] == "-"):
            operatorPosition.append(n)
            operatorPosition2.append(n)
            operatorPosition3.append(n + 1)
            operatorPosition.append(n + 1)
            operators.append(f[n])
        elif (f[n] == "^"):
            if (f[n - 1] == "x"):
                powerPosition.append(n + 1)
        elif (f[n] == "x"):
            # problem: does not account for coefficients > 1 digit
            # possible solutions: apply similar logic as power solution
            if (f[n + 1] == "^"):
                xPosition.append(n)


    operatorPosition.append(len(function))
    operatorPosition2.append(len(function))

    # creating terms for use in derivative calculation using operator positions
    m = 0
    n = 1

    while m < len(operatorPosition):
        index1 = operatorPosition[m]
        index2 = operatorPosition[n]
        term = f[index1:index2]
        terms.append(term)
        m = m + 2
        n = n + 2

    # take derivative of each term
    for n in range(0, len(powerPosition)):
        pwr = f[powerPosition[n]:operatorPosition2[n]]
        power.append(pwr)
        coeff = f[operatorPosition3[n]:xPosition[n]]
        coefficient.append(coeff)
        # converting strings in list to int
        for n in range(len(power)):
            power[n] = int(power[n])
        for n in range(len(coefficient)):
            coefficient[n] = int(coefficient[n])
        derpwr = power[n] - 1
        derPwr.append(derpwr)
        dercoeff = coefficient[n] * power[n]
        derCoeff.append(dercoeff)

    # cleaning up coefficient and power information
    difference = len(power) - len(powerPosition)
    del power[0:difference]
    difference2 = len(coefficient) - len(xPosition)
    del coefficient[0:difference2]

    del derCoeff[len(coefficient):len(derCoeff)]
    del derPwr[len(power):len(derPwr)]

    # create derivative function
    for n in range(len(derCoeff)):
        term = str(derCoeff[n]) + "x^" + str(derPwr[n])
        derTerm.append(term)
    for n in range(len(operators)):
        derTerm[n] = derTerm[n] + " " + operators[n] + " "

    derivative = " "
    for n in range(len(derTerm)):
        derivative = derivative + derTerm[n]

    # create original function

    for n in range(len(operators)):
        terms[n] = terms[n] + " " + operators[n] + " "

    originalF = " "
    for n in range(len(terms)):
        originalF = originalF + terms[n]

    # printing user's output
    print("This was your original function:")
    print(" ")
    print("f(x) = " + originalF)
    print(" ")
    print("This is your derivative function:")
    print(" ")
    print("f'(x) = " + derivative)
    print(" ")

    # compute x-value
    xValue = int(xValue)
    slopeVal = 0

    for n in range(len(derCoeff)):
        slopeVal = slopeVal + derCoeff[n] * pow(xValue, derPwr[n])

    print("This is the slope of the function, f(x), at x = " + str(xValue) + ":")
    print(" ")
    print(slopeVal)
    print(" ")
    print("The tangent line equation for the chosen point on the function is: ")
    print(" ")
    print(tangent(coefficient, power, xValue, slopeVal))


main()
