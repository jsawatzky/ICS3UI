########################
## FACTORING TOOLBOX  ##
##                    ##
## By: Justin Hardy,  ##
##     Simon Petrov & ##
##     Jacob Sawatzky ##
########################

##########
## MAIN ##
##########

#The main factoring method that the user will call
#Programmer: Jacob
def factor(expr):

    #Get ris of spaces
    expr = formatIn(expr)

    #Check if the expression is valid
    valid = isValid(expr)
    if valid != "":
        return valid

    #Get all the terms
    terms = getTerms(expr)

    #Split the terms into coefficients and variables
    coeffs = []
    varis = []
    for term in terms:
        coeff, vari = getCoeffAndVar(term)
        coeffs.append(coeff)
        varis.append(vari)

    #Common factor the coefficents and give starting values
    coeff, coeffs = commonFactorCoeffs(coeffs)
    if coeffs[0] < 0:
        coeff = "-" + coeff
        coeffs = factorNegative(coeffs)
    vari = ""
    factored = "dnf"
    #Check if the expression is a difference of squares
    if len(terms) == 2 and len(varis[0]) == 3 and varis[0].endswith("^2") and varis[1] == "" and terms[1][0] == "-":
        
        factored = diffOfSquares(coeffs, varis)

    #Checks if the expression can be trinomial factored
    elif len(terms) == 3 and len(varis[0]) == 3 and varis[0].endswith("^2") and len(varis[1]) == 1 and varis[0][0] == varis[1] and varis[2] == "":
        
        factored = trinomialFactor(coeffs, varis)

    #If no other factoring was successful then common factor the variables
    if factored == "dnf":

        vari, varis = commonFactorVaris(varis)

        #Get the expression after common factoring with brackets arounnd it
        factored = "(" + str(coeffs[0]) + varis[0]
        for i in range(1, len(terms)):
            factored += getStr(coeffs[i]) + varis[i]
        factored += ")"

    #If the factored from without brackets is the same as the expression the it doesn't factor
    if factored.strip('()') == expr:
        return "The expression " + expr + " does not factor"
    #If it successfuly factored then add the factored out
    #coefficients and varibles to the front, format it and then return it to the user
    else:
        return formatOut(coeff + vari + factored)

###############
## FACTORING ##
###############

#Common factors the coefficients
#Programmer: Justin
def commonFactorCoeffs(coeffs):

    #Gets a positive version of the coefficients to find the smallest number
    tempCoeffs = getPositives(coeffs)

    #Gets the biggest possible common factor by finding the smallest number
    largest = min(tempCoeffs)

    #Goes through all numbers between the number and 2
    #from largest to smallest in order to find the biggest common factor
    for i in range(largest, 1, -1):
        
        numSuccess = 0
        #Goes through all coefficents
        for i2 in range(0, len(coeffs)):
            #If the number divides evenly into the coefficicent add a success
            if coeffs[i2] % i == 0:
                numSuccess = numSuccess + 1

        #If the number divided evenly into all numbers the
        #divide all the coefficients by the number and return
        #the number and the new coefficients
        if numSuccess == len(coeffs):
            for n in range(len(coeffs)):
                temp = int(coeffs[n] / i)
                coeffs[n] = temp
            return (str(i), coeffs)

    #If no number evenly goes into all coefficients, return the same coefficients and an empty string
    return ("", coeffs)

#Factors out a negative from the coeffs
#Programmer: Jacob
def factorNegative(coeffs):

    #Switches the sign of all coefficients
    for i in range(len(coeffs)):

        coeffs[i] *= -1

    return coeffs

#Trinomial factors the coefficents and variables
#Programmer: Simon
def trinomialFactor(coeffs, varis):

    #Gets the a, b and c value along with the variable being used
    a = coeffs[0]
    b = coeffs[1]
    c = coeffs[2]
    vari = varis[1]

    #Gets the multiples of a and c
    aMulti = getMultiples(a)
    cMulti = getMultiples(c)

    #Goes through all multiples and cross multiplies them
    for x1, y1 in aMulti:
        for x2, y2 in cMulti:
            xy = x1*y2
            yx = y1*x2
            #If the two products add to b then return the factored from
            if xy + yx == b:
                return "(" + str(x1) + vari + getStr(x2) + ")(" + str(y1) + vari + getStr(y2) + ")"

    #If no comination of multiples added to be the return the it does not factor
    return "dnf"

#Does difference of squares factoring
#Programmer: Justin
def diffOfSquares(coeffs, varis):

    #Adds a "0" to the middle of the coefficients
    #and a single variable that match the first one
    #to the variables
    coeffs.insert(1, 0)
    varis.insert(1, varis[0][0])

    #Trinomial factors the new coefficients and variables and returns it
    return trinomialFactor(coeffs, varis)

#############
## UTILITY ##
#############

#Gets all the terms from the expression
#Programmer: Justin
def getTerms(expr):

    terms = []

    #Add a plus sign to the from if there is no negative sign
    if expr[0] != "-":
        expr = "+" + expr

    #Add a plus and a minus the the end of the expression to avoid a negative index
    expr += "+-"

    #Keep taking terms until there are none left
    while expr != "+-":

        #Remove the sign from the start of the expression
        sign = expr[0]
        expr = expr[1:]

        #Find the start of the next term
        nextTermI = min(expr.find("+"), expr.find("-"))

        #Add everything up to the next term along with the sign to the array
        terms.append(sign + expr[:nextTermI])


        #Remove the term from the expression
        expr = expr[nextTermI:]

    return terms

#Splits the varialble from the coefficient and return them in a tuple
#Programmer: Jacob
def getCoeffAndVar(term):

    #Gets the index of the variable
    xI = findVarI(term)

    #If there is no variable, set the variable index to the length of the term
    if xI == -1: xI = len(term)

    #Get the coefficient and add a "1" if its just a sign
    coeff = term[:xI]
    if coeff == "+": coeff = "+1"
    elif coeff == "-": coeff = "-1"

    return (int(coeff), term[xI:])

#Gets all possible multiples of a number
#Programmer: Jacob
def getMultiples(num):

    multiples = []

    #Goes through a range of number between:
    #1 and the number. if the number is positive
    #the number and -1. if the number is negative
    for i in range(min(1, num), max(0, num+1)):

        #Check if the number if divisible by the current number
        #and if it is add the current number and the number divided by the current number
        #along with the opposites of each to the array
        if num % i == 0:
            multiples.append((int(num/i), i))
            multiples.append((int(num/i)*-1, i*-1))

    return multiples

#Gets the first index of a variable in the given term
#Programmer: Jacob
def findVarI(term):

    #Goes through each character in the term
    for i in range(len(term)):

        #Checks if the character is a letter and if it is
        #return the current index
        if term[i].isalpha() == True:

            return i

    return -1

#Gets a copy of the coefficients with all numbers positive
#Programmer: Simon
def getPositives(coeffs):

    new = []

    #Goes through each coefficient
    for i in range(0, len(coeffs)):

        #If the number is negative, make it positive
        if coeffs[i] < 0:
            possitive = coeffs[i] * -1
            new.append(possitive)
        else:
            new.append(coeffs[i])

    return new

#Gets the string version of number with its sign for putting in the factored form
#Programmer: Simon
def getStr(num):

    num = str(num)
    #Add a plus sign if the number is positive
    if num[0] != "-":
        num = "+" + num

    return num

#Formats the input for factoring by removing spaces
#Programmer: Jacob
def formatIn(Input):

    #Remove all spaces
    Input = Input.replace(" ", "")

    return Input

#Formats the factored expression for output to the user
#Programmer: Jacob
def formatOut(output):

    #get rid of anything to the exponent 1
    output = output.replace("^1", "")

    rest = output
    #Go through each "1" in the string
    for i in range(output.count("1")):
        
        i1 = rest.find("1")

        #Check if its before a variable but not part of another number
        #and remove it if it is
        if rest[i1+1].isalpha() == True and rest[i1-1].isdigit() == False:

            output = output.replace(rest[i1:i1+2], rest[i1+1], 1)

        rest = rest[i1+1:]

    bI = output.find("(")
    temp = output[bI:]
    #Find the middle of the string
    middle = int(len(temp)/2)

    #Check if both halves are equal and if the are
    #remove one half and square it
    if temp[:middle] == temp[middle:]:
        output = output[:bI] + temp[:middle] + "^2"

    return output

#Checks if the given expression is a valid expression
#Programmer: Jacob
def isValid(expr):

    #Check for an equation
    if expr.find("=") != -1:
        return "INVALID ENTRY!!! You must enter an expression! (No equals signs)"
    #Check for a single term
    elif max(expr.find("+"), expr.find("-")) == -1:
        return "INVALID ENTRY!!! An expression must have more the one term."
    #Check for invalid characters
    elif expr.replace("^", "").replace("+", "").replace("-", "").isalnum() == False:
        return "INVALID ENTRY!!! You have invalid characters in your expression. Only '^', '+', '-', letters and numbers are allowed."
    else:
        return ""

###########
## EXTRA ##
###########

#Common factors the variables
#Programmer: Jacob
def commonFactorVaris(varis):

    variCoeff = ""

    commonVaris = []
    counts = []

    for vari in varis[0]:
        
        if vari.isalpha() == False:
            continue
        
        numSuccess = 0
        count = []
        #Finds the exponent of the current variable
        try:
            if varis[0][varis[0].find(vari)+1] == "^":
                count.append(int(varis[0][varis[0].find(vari)+2]))
            else:
                count.append(1)
        except IndexError:
            count.append(1)

        #Goes through all other variable sets
        for i in range(1, len(varis)):

            #Checks if the current variable is in the current variable set
            if varis[i].find(vari) != -1:
                
                numSuccess += 1
                #Finds the exponent of the current variable in the current variable set
                try:
                    if varis[i][varis[i].find(vari)+1] == "^":
                        count.append(int(varis[i][varis[i].find(vari)+2]))
                    else:
                        count.append(1)
                except IndexError:
                    count.append(1)

        #Checks if current variable was present in all variable sets
        if numSuccess == len(varis)-1:

            commonVaris.append(vari)
            counts.append(count)

    #Goes through every common variable
    for i in range(len(commonVaris)):

        #Gets the lowest exponent
        num = min(counts[i])

        #Gets string of the varialble that is being removed
        variCoeff += commonVaris[i]
        if num != 1:
            variCoeff += "^" + str(num)

        #Goes through each variable set
        for i2 in range(len(varis)):

            vari = varis[i2]

            #Gets the index of the common variable in the current variable set
            variI = vari.find(commonVaris[i])

            try:
                #Checks the the variable is to an exponent
                if vari[variI+1] == "^":
                    num2 = int(vari[variI+2])
                    start, end = vari[:variI], vari[variI:]
                    #If the exponent of the common variable is the same as the
                    #current exponent then remove the variable
                    if num2 == num:
                        end = end.replace(end[:3], "")
                    else:
                        #Lower the value of the exponent
                        end = end.replace(str(num2), str(num2-num), 1)
                    vari = start+end
                else:
                    #Remove variable if no exponent
                    vari = vari.replace(commonVaris[i], "")
            #Catch if variable is at end of string to remove variable
            except IndexError:
                vari = vari.replace(commonVaris[i], "")

            varis[i2] = vari

    return (variCoeff, varis)
