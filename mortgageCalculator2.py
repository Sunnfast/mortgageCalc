'''
Program 2: A Simple Mortgage Calculator, v2.0
Simone Christen
'''
outputTxt = open("mortgageOutput.txt", "a+") # allows reading and writing

# 1. Choose a dollar amount to be borrowed, as a whole number.
print(
  "Enter principal amount to be borrowed: \n (Note: payback period assumed to be 30 years.)"
)
p = float(input())  # convert user input to a float
n = 30 * 12  # since we are determining the number of monthly payment on a borrowed amount over 30 years

# 2. Specify an annual percent interest rate, as a floating-point number.
print("Enter the annual percent interest rate:")
aR = float(input()) / 100  # convert to a float to avoid a type error
r = aR / 12  # to get monthly interest rate

# 3. Calculate the monthly payment in dollars, as a floating-point number, using the formula
monthlyPayment = (p * (1 + r)**n * r) / ((1 + r)**n - 1)

# Output the prompts and input for amount borrowed, the annual percent interest rate (without formatting) and the payback period (in years).  Make sure you write the output to the output file this time and not to the console screen.
L1 = ["Amount borrowed: ", str(p), "\n"] # turn each line into a variable
outputTxt.writelines(L1) # write it all together in one line at a time
L2 = ["Annual interest rate: ", str(aR*100), "\n"]
outputTxt.writelines(L2)
L3 = ["Payback period: ", str(n/12) , "\n"]
outputTxt.writelines(L3)
L4 = ["Monthly payment = ", str(monthlyPayment), "\n"]
outputTxt.writelines(L4)
outputTxt.close() # not super sure why but it seems I need to close and reopen to do another operation

outputTxt = open("mortgageOutput.txt", "r+") # reopen to read it all out
print(outputTxt.read()) # wrap the read method in a print statement to output written contents of outputTxt
outputTxt.close()
