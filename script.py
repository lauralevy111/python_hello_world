print("hello, world")


/interest calculator code
amount = float(input('Principal amount ?'))
roi = float(input('Rate of Interest ?'))
yrs = int(imput('Duration (no. of years) ?'))

total = (amount * pow(1 +(roi/100), yrs))
interest = total - amount

print('\nInterest = %0.2f' %interest)

ACID= '00045SMA332'

accData = [ACID, str(amount), str(roi),str(yrs)]

print(accData)
print(len(accData))


accData_verbose = [ACID, str(amount), str(roi),str(yrs), bool(active), float(balance)]

accData_str = str(amount)+', '+str(roi)

print(accData_str)

//create dictionary
accType = {'MaxYrs': 10, 'TaxRate': .06}
accType['min_balance']=100
print("the account's minimum balance may be : "+accType['min_balance'])
