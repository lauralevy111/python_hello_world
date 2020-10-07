print("hello, world")


/interest calculator code
amount = float(input('Principal amount ?'))
roi = float(input('Rate of Interest ?'))
yrs = int(imput('Duration (no. of years) ?'))

total = (amount * pow(1 +(roi/100), yrs))
interest = total - amount

print('\nInterest = %0.2f' %interest)

accId = '00045SMA332'

accData = [accId, str(amount), str(roi),str(yrs)]
