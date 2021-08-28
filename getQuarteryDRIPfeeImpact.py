# Assume reinvestments on March ~12, June ~12, September ~12, & December ~12
# The shareholder in question held enough shares such that dividends always exceeded the base quarterly fee.
# Assume dividends always exceed base DRIP fee. Merck pays well, and they have an effectively flawless payment history.
# Ignoring the 4.8% reverse split in 2021. Reasonable given ignoring older fees + trading fees completely ignored.

from datetime import datetime
from datetime import timedelta
from datetime import date

TAsingleQuarterlyReinvestmentFee = 2
queryDate = datetime(2000, 12, 31) # begin holding shares
MRKpriceNow = 76.30

totalImpact = 0
totalSharesAssumingReinvestedWithRestOfReinvestment = 0
inFile = open('MRK.csv')
readFile = inFile.read()
readFile = readFile.strip()
readFile = readFile.split('\n')
inFile.close()

for lines in readFile[1:]:
  lines = lines.split(',')
  if(datetime.strptime(lines[0], "%Y-%m-%d") > queryDate):
    queryDate += timedelta(days = 91) # ignore 1 day offset/yr @ 90.25 days/quarter
    totalSharesAssumingReinvestedWithRestOfReinvestment += TAsingleQuarterlyReinvestmentFee / float(lines[4])
totalImpact = totalSharesAssumingReinvestedWithRestOfReinvestment * MRKpriceNow
print(totalImpact)