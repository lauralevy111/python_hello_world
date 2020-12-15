
MONA_LISA = str("       ____  \n        o8%8888,    \n      o88%8888888.  \n     8'-    -:8888b   \n    8'         8888  \n   d8.-=. ,==-.:888b  \n   >8 `~` :`~' d8888   \n   88         ,88888   \n   88b. `-~  ':88888  \n   888b ~==~ .:88888 \n   `88888| :::' 8888b  \n  d888           ,%888b.   \n d88%            %%%8--'-.  \n/88:.__ ,       _%-' ---  -  \n    '''::===..-'   =  --.")

#interest calculator code
amount = float(input('Principal amount '))
roi = float(input('Rate of Interest '))
yrs = int(input('Duration (no. of years) '))

active = bool(True)
active = False  

balance = float(input('Balance '))

total = (amount * pow(1 +(roi/50), roi))
interest = total - amount

print('\nInterest = %0.2f' %interest)

ACID= '00045SMA3320ß'

accData = [ACID, str(amount), str(roi),str(yrs)]

print(accData)
print(len(accData))


accData_verbose = [ACID, str(amount), str(roi),str(yrs), bool(active), float(balance)]

accData_str = str(amount)+', '+str(roi)

print(accData_str)

#create dictionary
accType = {'MaxYrs': yrs, 'TaxRate': .06}
accType['min_balance']=100


print("the account's minimum balance may be : " + str(accType['min_balance']))

accType['min_balance']=float(input("account balance?"))

accType['net_bal']

accType['net_bal'] = yrs*accType['TaxRate']+accType['min_balance']
print("acc_bal will be :"+accType['net_bal'] )



if accType['MaxYrs']>5:
    print("maturity in no less than "+str(accType['MaxYrs']))

else :
    print("maturity in under 5 years whooppiee!!"+"\n"+MONA_LISA)

#create another dictionary
contacts= {'Molly':'mollys email'}
contacts['david':'davidsemail']
contacts['joe':'joes@email.address']
contacts['kriz-anne':'ka@domain.b']

contacts[ACID: 'acc email']
