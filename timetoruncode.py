### Roughly how long will it take a Python program using this approach to count days between 12 Dec 2913 and 12 Dec 2012 ###


### How to measure the time it takes to run code ###

import time

time.clock()
days = 0

for i in range(36500): #~36500 days
    days +=1

end = time.clock()
print end #in seconds
