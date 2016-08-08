balance = float(raw_input("Enter opening balance: ... "))
payment = float(raw_input("Enter monthly payment: ... "))
pymt = 1
print '          Amount Remaining'
print 'Pymt#          Paid        Balance'
print '-----          ------      -----------'
while (balance - payment * pymt) >= 0:
    pymt = pymt + 1
    print '%4d%15.2f%15.2f' % (pymt - 1, payment, (balance - payment * (pymt - 1)))