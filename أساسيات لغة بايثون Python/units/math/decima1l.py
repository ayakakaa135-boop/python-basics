import decimal

print(decimal.getcontext())

decimal1=decimal.Decimal(3)
decimal2 = decimal.Decimal('3.22')
decimal3 = decimal.Decimal(2*2)
print(decimal1,decimal2 ,decimal3)

decimals =[decimal1,decimal2,decimal3]
print( sum(decimals))
print(  max(decimals))
print( min(decimals))
print(decimal1.sqrt())