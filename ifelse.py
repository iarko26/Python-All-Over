import time
timestamp=int(time.strftime("%H"));
if timestamp<12:
    print("Good Morning!")
elif timestamp>12 and timestamp<17:
    print("Good Afternoon!")
elif timestamp >17 and timestamp<20:
    print("Good Evening!")
else:
    print("Good Night!")
    

