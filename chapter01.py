# Think Python 2
# Chapter 01, page 8

km = 10
miles = km/1.61
time = 42*60 +42

pace = time/miles
pace_min = round(pace/60)
pace_sec = round(pace%60)

mph = miles/(time/60**2)

print("*** CHAPTER 01 EXERCISES ***")
print("1.2.1 There are", time, "seconds in 42 minutes 42 seconds")
print("1.2.2 There are", round(miles,2), "miles in 10km")
print("1.2.3 If you run a 10km race in 42 minutes 42 seconds")
print("..... Your average pace is", pace_min, "minutes", pace_sec, "seconds per mile")
print("..... Your average speed is", round(mph,2), " miles per hour")