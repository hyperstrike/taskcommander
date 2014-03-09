
#!/usr/bin/env python
import datetime
from datetime import datetime

######################################################################
# Please note this will not run from command line but will work when 
# copy/pasta in python terminal
######################################################################

myTimestamp = str(datetime.now()).split(" ") #splits output into list of date [0], and time [1] strs

myDate = myTimestamp[0] 
myTime = myTimestamp[1]

myDate = myDate.split("-") #splits date into year/month/day list of strs
myYear = myDate[0]
myMonth = myDate[1]
myDay = myDate[2]

myTime = myTime.split(":") #splits time into hour/minute/second/ms (6 decimals)
myHour = myTime[0]
myMinute = myTime[1]
mySecond = myTime[2]

print("Parsed Timestamp: ", myYear, myMonth, myDay, myHour, myMinute, mySecond)


