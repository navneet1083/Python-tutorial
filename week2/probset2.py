__author__ = 'navneet'


# paying credit card debt
# balance=5000.00
# annualInterestRate=0.18
# monthlyPaymentRate=0.02
balance = 3329
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
#
monthlyInterestRate=(annualInterestRate/12.0)
totalMinMonthlyPayment=0.00

#g = float("{0:.2f}".format(x))

minMonthlyPayment=10.00
actualBalance=balance

while totalMinMonthlyPayment <= actualBalance:
    minMonthlyPayment=float("{0:.2f}".format(minMonthlyPayment+10.00))
    actualBalance=balance

    for month in range(1,13):
        # minMonthlyPayment=float("{0:.2f}".format(monthlyPaymentRate*balance))
        # minMonthlyPayment=minMonthlyPayment+10
        previousBalance=float("{0:.2f}".format(actualBalance-minMonthlyPayment))
        interest=float("{0:.2f}".format(monthlyInterestRate*previousBalance))

        totalMinMonthlyPayment=float("{0:.2f}".format(totalMinMonthlyPayment+minMonthlyPayment))

        # print("Month is : "+str(month)+" Balance is : "+str(balance)+" Minimum Payment : "+str(minMonthlyPayment)
        #       +" Unpaid Balance : "+str(previousBalance)+" Interest : "+str(interest))

        # print('Month: '+str(month))
        # print('Minimum monthly payment: '+str(minMonthlyPayment))


        # Updating balance
        actualBalance=previousBalance+interest
        # print('Remaining balance: '+str(balance))

    print('Total paid:'+str(totalMinMonthlyPayment))
    print('Remaining balance:'+str(actualBalance))

print('Lowest Payment : '+str(minMonthlyPayment))