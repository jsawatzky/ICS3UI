from factoring import factor

normalTestCases = ["4x^2-9     ",
                   "4x^2 + 12x + 9",
                   "4y^2-12y+9",
                   "-4x^2+12x-9",
                   "8x^2-14x-15",
                   "x^2+x-12",
                   "4x^2+12x-9",
                   "7x^2-2x+16",
                   "2x^2+4x+6",
                   "8x^2-8x-6",
                   "10x^2-15x-25"]

extraTestCases = ["81x+27y-9z",
                  "3x^3-5x^5+6x^2"]

invalidTestCases = ["y=3x-2+7y",
                    "3x         ",
                    "5, + 6t;"]

allTestCases = [("NORMAL TEST CASES:", normalTestCases),
                ("EXTRA TEST CASES:", extraTestCases),
                ("INVALID TEST CASES:", invalidTestCases)]

for name, testCases in allTestCases:

    print(name)
    
    for eqtn in testCases:

        try:
            factored = factor(eqtn)
        except Exception as e:
            factored = "ERROR!!! " + str(e)

        print(eqtn + "\tfactors to:\t" + factored)

    print("\n")
