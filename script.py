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
